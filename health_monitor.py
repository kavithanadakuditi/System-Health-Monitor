import psutil

def cpu_usage():
    print("\n--- CPU Usage ---")
    print(f"CPU Usage: {psutil.cpu_percent()}%")

def memory_usage():
    print("\n--- Memory Usage ---")
    memory = psutil.virtual_memory()
    print(f"Total: {memory.total / (1024**3):.2f} GB")
    print(f"Used: {memory.used / (1024**3):.2f} GB")
    print(f"Percentage: {memory.percent}%")

def disk_usage():
    print("\n--- Disk Usage ---")
    disk = psutil.disk_usage('/')
    print(f"Total: {disk.total / (1024**3):.2f} GB")
    print(f"Used: {disk.used / (1024**3):.2f} GB")
    print(f"Percentage: {disk.percent}%")

def menu():
    while True:
        print("\n===== System Health Monitor =====")
        print("1. CPU Usage")
        print("2. Memory Usage")
        print("3. Disk Usage")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            cpu_usage()
        elif choice == "2":
            memory_usage()
        elif choice == "3":
            disk_usage()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

menu()