#!/usr/bin/env python3

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
        if battery_power_plugged and battery_percent >= 80:
            notify()
            time.sleep(60)


if __name__ == "__main__":
    main()
