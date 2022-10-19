import subprocess

interface="wlan0"
newmac="3C:22:FB:A4:63:AC"

print(" Changing mac address for " + interface + " for " + newmac)

subprocess.call("ifconfig " + interface + " down" , shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + newmac , shell=True)
subprocess.call("ifconfig " + interface + " up" , shell=True)
import subprocess

interface = input("Enter your Interface name: ")
mac = input("Enter the new mac address (in format XX:XX:XX:XX:XX:XX) : ")

subprocess.run("ifconfig " +interface+ " down", shell=True)
subprocess.run("ifconfig " +interface+ " hw ether "+mac, shell=True)

subprocess.run("ifconfig " +interface+ " up", shell=True)
