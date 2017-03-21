package com.ru.usty.scheduling;

import java.util.ArrayList;
import com.ru.usty.scheduling.process.ProcessExecution;

public class Scheduler {

	ProcessExecution processExecution;
	Policy policy;
	int quantum;
	ArrayList<Integer> processes;
	Thread timeSlice;
	Thread monitor;
	int currentProcess;

	/**
	 * Add any objects and variables here (if needed)
	 */


	/**
	 * DO NOT CHANGE DEFINITION OF OPERATION
	 */
	public Scheduler(ProcessExecution processExecution) {
		this.processExecution = processExecution;

		/**
		 * Add general initialization code here (if needed)
		 */
	}

	/**
	 * DO NOT CHANGE DEFINITION OF OPERATION
	 */
	public void startScheduling(Policy policy, int quantum) {

		this.policy = policy;
		this.quantum = quantum;
		this.processes = new ArrayList<Integer>();
		

		/**
		 * Add general initialization code here (if needed)
		 */

		switch(policy) {
		case FCFS:	//First-come-first-served
			System.out.println("Starting new scheduling task: First-come-first-served");
			/**
			 * Add your policy specific initialization code here (if needed)
			 */
			break;
		case RR:	//Round robin
			System.out.println("Starting new scheduling task: Round robin, quantum = " + quantum);
			/**
			 * Add your policy specific initialization code here (if needed)
			 */
			break;
		case SPN:	//Shortest process next
			System.out.println("Starting new scheduling task: Shortest process next");
			/**
			 * Add your policy specific initialization code here (if needed)
			 */
			break;
		case SRT:	//Shortest remaining time
			System.out.println("Starting new scheduling task: Shortest remaining time");
			/**
			 * Add your policy specific initialization code here (if needed)
			 */
			break;
		case HRRN:	//Highest response ratio next
			System.out.println("Starting new scheduling task: Highest response ratio next");
			/**
			 * Add your policy specific initialization code here (if needed)
			 */
			break;
		case FB:	//Feedback
			System.out.println("Starting new scheduling task: Feedback, quantum = " + quantum);
			/**
			 * Add your policy specific initialization code here (if needed)
			 */
			break;
		}

		/**
		 * Add general scheduling or initialization code here (if needed)
		 */

	}

	/**
	 * DO NOT CHANGE DEFINITION OF OPERATION
	 */
	public void processAdded(int processID) {

		switch(policy) {
		case FCFS:	//First-come-first-served
			firstComeFirstServe(true, processID);
			break;
		case RR:	//Round robin
			roundRobin(true, processID);
			break;
		case SPN:	//Shortest process next
			shortestProcessNext(true, processID);
			break;
		case SRT:	//Shortest remaining time
			shortestRemainingTime(true, processID);
			break;
		case HRRN:	//Highest response ratio next
			highestResponseRatioNext(true, processID);
			break;
		case FB:	//Feedback
			feedback(true, processID);
			break;
		}
	}

	/**
	 * DO NOT CHANGE DEFINITION OF OPERATION
	 */
	public void processFinished(int processID) {

		/**
		 * Add scheduling code here
		 */
		switch(policy) {
		case FCFS:	//First-come-first-served
			firstComeFirstServe(false, processID);
			break;
		case RR:	//Round robin
			roundRobin(false, processID);
			break;
		case SPN:	//Shortest process next
			shortestProcessNext(false, processID);
			break;
		case SRT:	//Shortest remaining time
			shortestRemainingTime(false, processID);
			break;
		case HRRN:	//Highest response ratio next
			highestResponseRatioNext(false, processID);
			break;
		case FB:	//Feedback
			feedback(false, processID);
			break;
		}
	}
	
	public void firstComeFirstServe(boolean adding, int processID) {
		if (adding) {
			if (processes.size() == 0) {
				processes.add(processID);
				processExecution.switchToProcess(processID);
			} else {
				processes.add(processID);
			}
		} else {
			processes.remove(0);
			System.out.println("Removed process: " + processID + ", processes: " + processes);
			if (processes.size() > 0) {
				System.out.println("Adding new process: " + processes.get(0) + ", processes: " + processes);
				processExecution.switchToProcess(processes.get(0));
			}
		}
	}
	
	public void roundRobin(boolean adding, final int processID) {
		if (adding) {
			if (processes.size() == 0) {
				processes.add(processID);
				this.currentProcess = 0;
				processExecution.switchToProcess(processes.get(this.currentProcess));
				createTimeSlice();
			} else {
				processes.add(processID);
			}
		} else {
			if (processes.size() > 0) {
				roundRobinSwitchProcess();
			}
			if (processes.indexOf(processID) <= this.currentProcess) {
				this.currentProcess -= 1;
			}
			processes.remove(processes.indexOf(processID));

		}
	}
	
	public void roundRobinSwitchProcess() {

		if (this.currentProcess == processes.size() - 1) {
			this.currentProcess = 0;
			processExecution.switchToProcess(processes.get(this.currentProcess));
		} else {
			this.currentProcess = this.currentProcess + 1;
			processExecution.switchToProcess(processes.get(this.currentProcess));
		}
		createTimeSlice();
	}
	
	public long getQuantum() {
		return this.quantum;
	}
	
	public void createTimeSlice() {
		
		if (this.timeSlice != null) {
			this.timeSlice.interrupt();
		}

		this.timeSlice = new Thread() {
			
		    public void run() {
		    	long startTime = System.currentTimeMillis();
		    	if (startTime + getQuantum() > System.currentTimeMillis()) {
					while ((startTime + getQuantum() > System.currentTimeMillis())) {}
					if (this.isInterrupted() != true) {
						roundRobinSwitchProcess();
					}
		    	}
		    }  
		};
		this.timeSlice.start();
	}
	
	public void shortestProcessNext(boolean adding, int processID) {
		if (adding) {
			if (processes.size() == 0) {
				processes.add(processID);
				processExecution.switchToProcess(processes.get(0));
			} else {
				int location = -1;
				int i = 1;
				while (i < processes.size() && location == -1) {
					if (processExecution.getProcessInfo(processes.get(i)).totalServiceTime > 
							processExecution.getProcessInfo(processID).totalServiceTime) {
						location = i;
					}
					i++;
				}
				if (location != -1) {
					processes.add(location, processID);
				} else {
					processes.add(processID);
				}
			}
		} else {
			processes.remove(processes.get(0));
			if (processes.size() > 0) {
				processExecution.switchToProcess(processes.get(0));
			}
		}
	}
	
	public void shortestRemainingTime(boolean adding, int processID) {
		if (adding) {
			if (processes.size() == 0) {
				processes.add(processID);
				processExecution.switchToProcess(processes.get(0));
				monitorRemainingTime();
			} else {
				insertByRemainingTime(processID);
			}
		} else {
			processes.remove(processes.get(0));
			if (processes.size() > 0) {
				processExecution.switchToProcess(processes.get(0));
			} else {
				this.monitor.interrupt();
			}
		}
	}
	
	public void insertByRemainingTime(int processID) {
		int location = -1;
		int i = 1;
		while (i < processes.size() && location == -1) {
			if (calculateRemainingTime(processes.get(i)) > calculateRemainingTime(processID)) {
				location = i;
			}
			i++;
		}
		if (location != -1) {
			processes.add(location, processID);
		} else {
			processes.add(processID);
		}
	}
	
	public long calculateRemainingTime(int processID) {
		return processExecution.getProcessInfo(processID).totalServiceTime 
				- processExecution.getProcessInfo(processID).elapsedExecutionTime;
	}
	
	public void monitorRemainingTime() {

		this.monitor = new Thread() {
			
		    public void run() {
		    	while (this.isInterrupted() != true) {
		    		if (processes.size() > 1) {
		    			System.out.println(processes);
		    			if (calculateRemainingTime(processes.get(0)) > calculateRemainingTime(processes.get(1))) {
		    				int currentProcess = processes.get(0);
		    				processes.remove(0);
		    				insertByRemainingTime(currentProcess);
		    				processExecution.switchToProcess(processes.get(0));
		    			}
		    		}
		    		try {
						sleep(10);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
		    	}
		    }  
		};
		this.monitor.start();
	}
	
	public void highestResponseRatioNext(boolean adding, int processID) {
		if (adding) {
			
		} else {

		}
	}
	
	public void feedback(boolean adding, int processID) {
		if (adding) {
			
		} else {

		}
	}
	
}
