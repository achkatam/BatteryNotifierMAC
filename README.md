# Battery Charge Monitor

This Python script monitors your Mac's battery charge level and sends a notification when it reaches 80% while charging.

## Features

- Monitors battery percentage
- Sends a macOS notification when the battery reaches 80% while charging
- Runs in the background using `nohup`

## Requirements

- Python 3.9 or higher
- `psutil` library
- macOS

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/achkatam/chargingNotification.git
   cd chargingNotification

2. Create and activate a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate

3. Install required packages:
   pip install psutil

4. Usage
   Run the script in the background:

   bash
   Copy code
   nohup .venv/bin/python /path/to/chargingNotification/battery_charge_monitor.py &
   Replace /path/to/chargingNotification/ with the actual path to the directory where the script is located.

License
This project is licensed under the MIT License.