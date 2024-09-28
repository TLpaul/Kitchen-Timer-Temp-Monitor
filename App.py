import tkinter as tk
from threading import Thread
import random
import time
from plyer import notification

# Function to send notification
def send_notification(message):
    notification.notify(
        title="Kitchen Alert",
        message=message,
        timeout=10
    )

# Timer function
def kitchen_timer(minutes):
    status_label.config(text=f"Timer set for {minutes} minutes.")
    time.sleep(minutes * 60)
    send_notification("Timer is up! Your food is ready.")
    status_label.config(text="Timer is up! Your food is ready.")

# Simulate temperature monitoring
def simulate_temperature_monitoring():
    while True:
        temp = random.uniform(50.0, 100.0)
        temp_label.config(text=f"Current temperature: {temp:.2f}°F")
        if temp > 90.0:
            send_notification("Warning: Temperature too high!")
        time.sleep(5)

# Function to start both the timer and temperature monitoring in separate threads
def start_kitchen_process():
    minutes = int(timer_entry.get())
    Thread(target=kitchen_timer, args=(minutes,)).start()
    Thread(target=simulate_temperature_monitoring).start()

# Tkinter UI
app = tk.Tk()
app.title("Kitchen Timer and Temperature Monitor")

# Timer input
timer_label = tk.Label(app, text="Set Timer (minutes):")
timer_label.pack(pady=10)
timer_entry = tk.Entry(app)
timer_entry.pack(pady=10)

# Start button
start_button = tk.Button(app, text="Start", command=start_kitchen_process)
start_button.pack(pady=10)

# Status label
status_label = tk.Label(app, text="Waiting to start timer...", fg="blue")
status_label.pack(pady=10)

# Temperature label
temp_label = tk.Label(app, text="Current temperature: -- °F", fg="red")
temp_label.pack(pady=10)

# Run the tkinter app
app.mainloop()
