import tkinter as tk
from datetime import datetime, timedelta


class TaskClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Track Task Clock")
        self.start_time = None
        self.running = False

        self.label = tk.Label(
            root, text="Press 'Start' to begin", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(
            root, text="Start", command=self.start_timer, font=("Helvetica", 14))
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(
            root, text="Stop", command=self.stop_timer, font=("Helvetica", 14))
        self.stop_button.pack(pady=10)

        self.elapsed_time_label = tk.Label(
            root, text="Elapsed time: 00:00:00", font=("Helvetica", 16))
        self.elapsed_time_label.pack(pady=20)

    def start_timer(self):
        self.start_time = datetime.now()
        self.label.config(text="Timer is running...")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button(state=tk.NORMAL)
        self.update_timer()

    def stop_timer(self):
        if self.start_time:
            elapsed_time = datetime.now() - self.start_time
            self.elapsed_time_label.config(
                text=f"Elapsed time: {elapsed_time.total_seconds(): .2f} seconds")
            self.label.config(text="Press 'Start' to begin")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.start_time = None

    def update_timer(self):
        if self.running:
            elapsed_time = datetime.now() - self.start_time
            self.elapsed_time_label.config(
                text=f"Elapsed time: {str(elapsed_time).split('.')[0]}")
            self.root.after(1000, self.update_timer)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskClock(root)
    root.mainloop()
