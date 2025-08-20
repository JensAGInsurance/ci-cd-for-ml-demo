from datetime import datetime

def main():
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time)

if __name__ == "__main__":
    main()
