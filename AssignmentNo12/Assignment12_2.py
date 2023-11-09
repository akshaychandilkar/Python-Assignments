import psutil
import sys

def get_process_info(process_name):
    for process in psutil.process_iter(['pid', 'name', 'status']):
        if process.info['name'] == process_name:
            return process.info

    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: Procinfo.py <process_name>")
    else:
        process_name = sys.argv[1]
        process_info = get_process_info(process_name)

        if process_info:
            print("Process Name:", process_info['name'])
            print("Process ID:", process_info['pid'])
            print("Process Status:", process_info['status'])
        else:
            print(f"Process '{process_name}' is not running.")

if __name__ == "__main__":
    main()