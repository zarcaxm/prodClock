import time


def start_timer():
    input("Press Enter to start the timer...")
    start_time = time.time()
    print("Time started. Press Enter to stop the timer...")
    input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    start_timer()
