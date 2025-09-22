from multiprocessing import Process, Value
import time
import random
## Parent process
def sensor(shared_temp): 
    for _ in range(5):
        new_temp = random.randint(20, 40) # Generate random integer between 20 and 40
        shared_temp = new_temp
        print(f"[sensor] Updated temperature to {new_temp}°C")
        time.sleep(3) #Simulate time delay 
## Child process
def monitor(shared_temp):
    while True:
        temp = shared_temp.value # Access the shared value
        print(f"[monitor] Current temperature is {temp}°C")
        time.sleep(1) 

#Interprocess communication setup
if __name__ == "__main__":
    shared_temp = Value('i', 25)  # 'i' for integer, initial value 0

    monitor_process = Process(target=monitor, args=(shared_temp,)) # Create monitor process
    monitor_process.start() # Start monitor process
    sensor(shared_temp)
    monitor_process.terminate() # Terminate monitor process after sensor is done