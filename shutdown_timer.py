import tkinter as tk
from tkinter import messagebox
import threading
import os


class ShutdownApp:
    def shutdown(self):
        try:
            timer_minutes = int(self.entry.get())
            threading.Timer(0, self.execute_shutdown, args=[timer_minutes]).start()
            messagebox.showinfo("Shutdown Timer", f"Shutdown in {timer_minutes} minutes.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def abort_shutdown(self):
        try:
            # Abort shutdown on macOS
            os.system("sudo killall shutdown")
            messagebox.showinfo("Shutdown Timer", "Shutdown aborted.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def execute_shutdown(self, timer_minutes):
        try:
            # Schedule the shutdown using 'sudo shutdown' command on macOS
            os.system(f"sudo shutdown -h +{timer_minutes}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def __init__(self, master):
        print("App started!!!")

        self.master = master
        master.title("Shutdown Timer")

        self.label = tk.Label(master, text="Enter shutdown timer in minutes")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.shutdown_btn = tk.Button(master, text="Shutdown", command=self.shutdown)
        self.shutdown_btn.pack()

        self.abut_btn = tk.Button(master, text="Abort Shutdown", command=self.abort_shutdown)


if __name__ == "__main__":
    root = tk.Tk()
    app = ShutdownApp(root)
    root.mainloop()
