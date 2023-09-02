import psutil
import tkinter as tk
from tkinter import messagebox

def get_battery_percentage():
    battery = psutil.sensors_battery()
    percent = battery.percent
    return percent

battery_percentage = get_battery_percentage()

root = tk.Tk()
root.withdraw()  # Hide the main window

message = f"Battery Percentage: {int(battery_percentage)}%"
messagebox.showinfo("Battery Alert", message)
