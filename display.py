import tkinter as tk
import time

def display_notification(message):
    time.sleep(1)
    notification_window = tk.Tk()
    notification_window.overrideredirect(1)  # Remove window decorations
    notification_window.attributes("-topmost", True)  # Ensure it's always on top
    notification_window.geometry("200x30+{}+0".format(notification_window.winfo_screenwidth() - 200))
    notification_window.title("Notification")

    notification_label = tk.Label(notification_window, text=message)
    notification_label.pack(fill="both")

    # Close the notification after 5 seconds
    notification_window.after(3000, notification_window.destroy)
    notification_window.mainloop()
