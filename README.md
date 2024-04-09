# Steal Sophos Logins

## Installation

1. Install Python
2. Clone this repository and cd into it
3. Make a python virtual environment

```bash
python -m venv venv
```

4. Install dependencies

```bash
venv/bin/pip install selenium SpoofMac
```

5. Find your wifi interface name with:

```bash
venv/bin/spoof-mac.py list
```

For example, my output for the above command is:

```bash
- "Ethernet Adapter (en3)" on device "en3" with MAC address <mac address here>
- "Ethernet Adapter (en5)" on device "en5" with MAC address <mac address here>
- "Thunderbolt Bridge" on device "bridge0" with MAC address <mac address here>
- "Wi-Fi" on device "en0" with MAC address <mac address here>
- "Thunderbolt 1" on device "en1" with MAC address <mac address here>
- "Thunderbolt 2" on device "en2" with MAC address <mac address here>
```

The right interface name for me is 'Wi-Fi'

7. You have to change a line in the code depending on your operating system.
   If you're on linux or windows, you have to change the following line:

```python
# change this line for reconnecting command
os.system('networksetup -setairportnetwork en0 PESU-EC-Campus "PESU-EC-Campus"')
```

This line of code, runs the command to reconnect to the PESU EC Campus WiFi network. If you're in RR, you'll have to change the SSID accordingly.

You'll have to look up what the exact command for your distribution is but the most common configuration for network in linux systems is using NetworkManager. If you are using NetworkManager, the command would be:

```bash
nmcli d wifi connect "PESU-EC-Campus" password "PESU-EC-Campus"
# the password is same as the SSID at EC Campus
```

6. Run the script with:

```bash
# venv/bin/python steal.py <interface name> <srn lower limit> <srn upper limit> <department> <campus> <year>
# campus:
# 1 -> RR
# 2 -> EC
venv/bin/python steal.py Wi-Fi 0 200 CS 2 21
```

7. Once the script is done, you'll find the output in `output.txt`
