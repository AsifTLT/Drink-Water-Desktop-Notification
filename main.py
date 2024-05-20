import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "when you don't Drink a water, your health is not good enough for yourself",
            app_icon = "C:/Users/User/Desktop/200 PYTHON PROJECT CHALLENGE/data/Day9/Drink Water Desktop Notification/glassofwater_84019.ico",
            timeout=10
            
        )
        time.sleep(60*60)
        # time.sleep(6)
    