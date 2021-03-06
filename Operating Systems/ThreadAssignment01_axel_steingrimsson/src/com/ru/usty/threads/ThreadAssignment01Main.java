package com.ru.usty.threads;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ThreadAssignment01Main {

    private static final int NUMBER_OF_PROBLEMS = 100;
    private static final int POOL_SIZE = 3;
    
    static Problem getProblem() {
    	return Problematic.nextProblem();
    }
    
    static void runProblem(Runnable runnable) {
    	new Thread(runnable).start();
    }
	
    static Runnable makeRunnable(Problem problem) {
    	
    	Runnable runnable = (new Runnable() {
    		@Override
    		public void run() {
    			Solver.findAndPrintSolution(problem); 
    		}});
    	
		return runnable;
    }
    
    
    public static void main(String[] args) {
        System.out.println("Processors: " + Runtime.getRuntime().availableProcessors());
        System.out.println("Solutions:");

        long startTime = System.currentTimeMillis();
        
        ExecutorService threadPool = Executors.newFixedThreadPool(POOL_SIZE);
        
        final Problem problem = getProblem();
        
        for (int i = 0; i < NUMBER_OF_PROBLEMS; i++) {
        	Runnable runnable = makeRunnable(problem);
        	threadPool.execute(runnable);
        }
        
        try {
        	threadPool.shutdown();
        	threadPool.awaitTermination(5, TimeUnit.MINUTES);
        } catch (InterruptedException e) {
        	e.printStackTrace(); 
        }

        System.out.println("All done");

        System.out.println("Total time: " + (System.currentTimeMillis() - startTime) + " ms");
    }
}
