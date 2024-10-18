import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water",
            message=(
                "The U.S. National Academies of Sciences, Engineering, and Medicine "
                "recommend about 15.5 cups (3.7 liters) of fluids a day for men and "
                "about 11.5 cups (2.7 liters) for women."
            ),
            app_icon="/home/minahil/python/drinkingwater/glass-of-water.png",  # Ensure the icon path and format is correct
            timeout=10  # Notification duration in seconds
        )
        time.sleep(60*60)  # Sleep for 1 hour (3600 seconds)
