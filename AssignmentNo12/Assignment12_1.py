import os
import sys
import psutil
import logging

logging.basicConfig(filename='proc_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def get_process_info():
    try:
        # Get a list of all running processes
        processes = psutil.process_iter()
        
        # Display header
        print("Process Name | PID | Username")
        
        for process in processes:
            try:
                process_info = process.as_dict(attrs=['name', 'pid', 'username'])
                print(f"{process_info['name']} | {process_info['pid']} | {process_info['username']}")
                
                # Log the process information
                logging.info(f"Process Name: {process_info['name']} | PID: {process_info['pid']} | Username: {process_info['username']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    except Exception as e:
        # Handle unexpected exceptions
        logging.error(f"Error: {str(e)}")

def main():
    get_process_info()

if __name__ == "__main__":
    main()