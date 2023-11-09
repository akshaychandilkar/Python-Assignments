import os
import psutil

def create_process_log(directory):    
    process_list = psutil.process_iter(attrs=['pid', 'name', 'username'])

    log_file_path = os.path.join(directory, "ProcessInfoLog.txt")

    with open(log_file_path, "w") as log_file:
        log_file.write("Name\tPID\tUsername\n")
        for process in process_list:
            try:
                name = process.info['name']
                pid = process.info['pid']
                username = process.info['username']
                log_file.write(f"{name}\t{pid}\t{username}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    print(f"Process information logged in {log_file_path}")

def main():  
    directory_name = input("Enter the directory name: ")

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    create_process_log(directory_name)

if __name__ == "__main__":
    main()