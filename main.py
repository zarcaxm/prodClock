import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta


class TaskClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Track Task Clock")
        self.start_time = None
        self.running = False
        self.task_name = None

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 14))
        self.style.configure("TLabel", font=("Helvetica", 16))

        # Main Frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Task name label and entry
        self.label = ttk.Label(
            self.main_frame, text="Enter task name and press 'Start' to begin")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.task_entry = ttk.Entry(self.main_frame, font=("Helvetica", 14))
        self.task_entry.grid(row=1, column=0, columnspan=2,
                             pady=10, sticky=(tk.W, tk.E))

        # Start and stop buttons
        self.start_button = ttk.Button(
            self.main_frame, text="Start", command=self.start_timer)
        self.start_button.grid(row=2, column=0, pady=10)

        self.stop_button = ttk.Button(
            self.main_frame, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.grid(row=2, column=1, pady=10)

        # Elapsed time label
        self.elapsed_time_label = ttk.Label(self.main_frame, text="00:00:00")
        self.elapsed_time_label.grid(row=3, column=0, columnspan=2, pady=20)

        # Task label
        self.task_label = ttk.Label(self.main_frame, text="")
        self.task_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

    def start_timer(self):
        self.task_name = self.task_entry.get()
        if self.task_name:
            self.start_time = datetime.now()
            self.running = True
            self.label.pack_forget()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.task_label.config(state=tk.DISABLED)
            self.task_entry.pack_forget()
            self.task_label.config(text=f"Task: {self.task_name}")
            self.update_timer()
        else:
            self.label.config(text="Task Name")

    def stop_timer(self):
        self.running = False
        if self.start_time:
            elapsed_time = datetime.now() - self.start_time
            hours, remainder = divmod(elapsed_time.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            self.elapsed_time_label.config(
                text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
            )
            self.label.config(
                text="Enter task name and press 'Start' to begin")
            self.label.grid()  # Show the label again
            self.start_button.state(["!disabled"])  # Enable the start button
            self.stop_button.state(["disabled"])  # Disable the stop button
            self.task_entry.grid()  # Show the task entry again
            self.task_entry.config(state=tk.NORMAL)
            self.task_entry.delete(0, tk.END)  # Clear the entry field
            self.start_time = None
            self.task_label.config(text=f"Task: {self.task_name} completed")

    def update_timer(self):
        if self.running:
            elapsed_time = datetime.now() - self.start_time
            hours, remainder = divmod(elapsed_time.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            self.elapsed_time_label.config(
                text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
            self.root.after(1000, self.update_timer)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskClock(root)
    root.mainloop()
