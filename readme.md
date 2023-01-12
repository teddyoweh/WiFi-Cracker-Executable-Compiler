# WiFi Cracker
This script is designed to test various passwords against a specific wifi SSID, trying to find the correct password. 

## Requirements
* Python 3
* `urllib`
* `datetime`
* `os`
* `platform`
* `subprocess`

## How to use
1. Run the script 
2. Enter the SSID of the wifi network you want to crack.
3. Enter the interface name.
4. Choose whether to use a common wordlist or specify a custom word list.
5. The script will then iterate through each word in the chosen wordlist, attempting to connect to the wifi network with that word as the password.

## Additional Information
* The script will create a log file named `log.txt` which will log each attempt made by the script, along with the date and time of the attempt, the SSID and password used, and the outcome of the attempt (success or failure).
* The script supports MacOS, Windows, and Linux.

This script could be used in a cyber security testing engagement to find weaknesses in an organization's wifi security. It could also be used by an attacker to gain unauthorized access to a wifi network. Use of this script to access wifi networks without proper authorization is illegal.
