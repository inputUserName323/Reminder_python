import time
from win10toast import ToastNotifier

def reminder(message, delay):
    time.sleep(delay)
    toaster = ToastNotifier()
    toaster.show_toast(
        "Reminding",
        message,
        duration=10
    )

message = input("Enter your reminder message: ")
delay = int(input("Enter reminder time (second) : "))

reminder(message, delay)