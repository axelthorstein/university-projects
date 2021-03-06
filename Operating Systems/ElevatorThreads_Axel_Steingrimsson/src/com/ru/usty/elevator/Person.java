package com.ru.usty.elevator;

import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;

public class Person implements Runnable {

	private Elevator elevator = null;
	private int startFloor;
	private int ID;
	private int stopFloor;
	private Thread thread;
	private Semaphore semaphore = new Semaphore(1);
	private boolean running = true;
	
	
	public Person(int ID, int startFloor, int stopFloor){
	        this.ID = ID;
	        this.startFloor = startFloor;
	        this.stopFloor = stopFloor;
	        this.thread = new Thread(this, "" + this.ID);
	}
	
	public void setElevator(Elevator elevator) {
		this.elevator = elevator;
	}
	
	public Elevator getElevator() {
		return this.elevator;
	}
	
	public int getStartFloor() {
		return this.startFloor;
	}
	public int getStopFloor() {
		return this.stopFloor;
	}
	
	public void stopRunning() {
		this.running = false;
	}
	
	@Override
	public void run(){
    }


	public Thread getThread() {
		return this.thread;
	}
}
