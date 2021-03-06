package com.ru.usty.elevator;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;

public class Elevator implements Runnable {

	private ArrayList<Person> passengers = new ArrayList<Person>();
	private int numPassengers;
	private int currentFloor;
	private int capacity;
	private int ID;
	private int numFloors;
	private Thread thread;
	private ElevatorScene scene;
	private Semaphore semaphore = new Semaphore(1);
	Map<Integer, Integer> wantedFloors = new HashMap<Integer, Integer>();
	private String direction = "up";
	
	public Elevator(int id, int numFloors, int capacity, ElevatorScene scene) {
		this.currentFloor = 0;
		this.capacity = capacity;
		this.ID = id;
		this.numFloors = numFloors - 1;
		this.thread = new Thread(this, "" + this.ID);
		this.scene = scene;
	}
	
	@Override
	public void run() {
		boolean first = true;
		
		while(true) {
			// Open door
			boolean permit = false;
		    try {
		    	if (first) {
		    		Thread.sleep(1000);
		    		first = false;
		    	}
		        permit = semaphore.tryAcquire(1, TimeUnit.SECONDS);
		        if (permit) {
		            letOnPassengers();
		            if (scene.getPeople().size() != 0) {
			            System.out.println(this.ID + " let on " + numPassengers + " : " + passengers + " passengers at the " + currentFloor + " floor. " + scene.getPeople().size() + " are left waiting.");
		            }
		            moveFloors();
		            Thread.sleep(scene.VISUALIZATION_WAIT_TIME);
		        } else {
		            System.out.println("Could not acquire semaphore");
		        }
		    } catch (InterruptedException e) {
		        throw new IllegalStateException(e);
		    } finally {
		        if (permit) {
		        	letOutPassengers();
		            semaphore.release();
		        }
		    }
		}
	}
	
	private void letOnPassengers() {
		ArrayList<Person> people = scene.getPeopleAtFloor(currentFloor);
        for (Person person : people) {
        	if (numPassengers < capacity) {
	            	numPassengers++;
	            	passengers.add(person);
	            	person.setElevator(this);
	        		scene.removePerson(person);
	            	int floor = person.getStopFloor();
	            	if (wantedFloors.containsKey(floor)) {
	            		wantedFloors.put(floor, wantedFloors.get(floor) + 1);
	            	} else {
	            		wantedFloors.put(floor, 1);
	            	}
        		}
        	}
        
	}
	
	private void letOutPassengers() {
		for (int i = numPassengers - 1; i >= 0; i--){
    		if (passengers.get(i).getStopFloor() == currentFloor) {
        		scene.personExitsAtFloor(currentFloor);
	        	wantedFloors.put(currentFloor, wantedFloors.get(currentFloor) - 1);
        		passengers.get(i).stopRunning();
    			numPassengers--;
    			passengers.remove(i);
    		}
    	}
		
	}
	
	private void moveFloors() {
		int newFloor = currentFloor;
		
		if (currentFloor == numFloors) {
			direction = "down";
		} else if (currentFloor == 0){
			direction = "up";
		}
		
		if (direction == "up") {
			newFloor = currentFloor + 1;
		} else {
			newFloor = currentFloor - 1;
		}
		
		while (scene.getNumberOfPeopleWaitingAtFloor(newFloor) == 0 && wantedFloors.get(newFloor) == 0 && scene.getPeople().size() != 0) {
			if (newFloor == numFloors) {
				direction = "down";
			}
			if (direction == "up") {
				newFloor += 1;
			} else {
				newFloor -= 1;
			}
		}
		currentFloor = newFloor;
	}
	
	public void letPersonOn(Person person) {
		passengers.add(person);
	}
	
	public boolean isFull() {
		return passengers.size() == this.capacity;
	}
	
	public int getNumPassengers() {
		return this.passengers.size();
	}
	
	public int getCurrentFloor() {
		return this.currentFloor;
	}

	public int getElevatorId() {
		return this.ID;
	}
	
    public Thread getThread(){
        return this.thread;
    }

    public synchronized boolean enter(int riderId){
        this.numPassengers++;
        return true;
    }
	
	

}
