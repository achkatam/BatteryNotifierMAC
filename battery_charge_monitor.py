import psutil
import time
import subprocess


def get_battery_status():
    battery = psutil.sensors_battery()
    return battery.percent, battery.power_plugged


def notify():
    title = "Battery Alert",
    message = "Battery level is 80%",
    apple_script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", apple_script])


def main():
    while True:
        battery_percent, battery_power_plugged = get_battery_status()
        if battery_power_plugged and battery_percent >= 73:
            notify()

            while battery_power_plugged:
                time.sleep(2)
                _, battery_power_plugged = get_battery_status()
        time.sleep(2)


if __name__ == "__main__":
    main()
