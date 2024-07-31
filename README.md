# Battery Charge Monitor

This Python script monitors the battery level of your Mac and sends a notification when the battery level getes up to 80% while charging so you do not overcharge it.
It is designed to run in the background as a LaunchAgent.

## Requirements

- Python 3
- The required Python packages are listed in the `requirements.txt` file.

## Setup

1. **Clone the Repository** (or download the script):

   ```sh
   git clone <repository_url>
   cd <repository_directory>

2. Install the Required Packages:
   pip install -r requirements.txt

3. Make the script executable:
   chmod +x battery_charge_monitor.py

4. Create a LaunchAgent to Run the Script in    the Background:

   1. Create the LaunchAgents Directory (if it     doesn't exist):
      mkdir -p ~/Library/LaunchAgents
   2. Create '.plist' File:
      Use a text editor to create a .plist file in    he LaunchAgents folder. For example, you can   se nano:
      nano ~/Library/LaunchAgents/com.user.batteryalert.plist
  3. Edit the .plist File:

   Add the following content to the file,    eplacing /path/to/your/battery_charge_monitor. y with the full path to your script:

      """
       ?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
      <plist version="1.0">
      <dict>
         <key>Label</key>
         <string>com.user.batteryalert</string>
         <key>ProgramArguments</key>
         <array>
            <string>/path/to/your/script/batterynotifer.py</string>
         </array>
         # In case you do not want the app to start everytime you turn the system ON
         # delete the following 2 lines:
         <key>RunAtLoad</key>
         <true/>
         <key>KeepAlive</key>
         <true/>
      </dict>
      </plist>
      "":
5. Load the LaunchAgent:

   Load the LaunchAgent to start the script in the background:

   launchctl load ~/Library/LaunchAgents/com.user.batteryalert.plist

6. Stopping the Script:
   To stop the script, unload the LaunchAgent:

   launchctl unload ~/Library/LaunchAgents/com.user.batteryalert.plist
