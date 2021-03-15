import os
import subprocess


data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
profile = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print("{:<30}| {:<}".format('Profile', 'Password'))




for i in profile:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [a.split(":")[1][1:-1] for a in results if "Key Content" in a]
    try:
        print ("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}| {:<}".format(i, ""))


input('Press any key to quit....')