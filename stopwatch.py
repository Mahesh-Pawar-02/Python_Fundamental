import time

def stopwatch(duration):
    print("Stopwatch started...")
    start_time = time.time()
    
    while True:
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds", end="\r")
        time.sleep(0.1)  # Update the output every 0.1 seconds

        if elapsed_time >= duration:
            break
    
    print(f"\nStopwatch stopped. Total time: {duration} seconds.")

# Specify the duration for the stopwatch in seconds
duration = 10  # Example: 10 seconds
stopwatch(duration)
