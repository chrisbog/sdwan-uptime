import requests
import urllib3
import configparser
import time


def initalize_connection(ipaddress,username,password):

    """
    This function will initialize a connection to the Cisco SD-WAN vManage platform.

    :param ipaddress: This is the IP Address and Port number of vManage (i.e., "192.168.0.1:8443")
    :param username:  This is the username for vManage
    :param password:  This is a password for vManage
    :return: A session object which can be used to make subsequent calls for other queries
    """

    # Disable warnings like unsigned certificates, etc.
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url="https://"+ipaddress+"/j_security_check"

    payload = "j_username="+username+"&j_password="+password
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        }

    sess=requests.session()

    # Handle exceptions if we cannot connect to the vManage
    try:
        response = sess.request("POST", url, data=payload, headers=headers,verify=False,timeout=10)
    except requests.exceptions.ConnectionError:
        print ("Unable to Connect to "+ipaddress)
        return False

    return sess

def get_inventory(serveraddress,session,type):

    """
    This function retrieves the complete hostname data for everything in vManage
    :param serveraddress: This is the IP Address and Port number of vManage (i.e., "192.168.0.1:8443")
    :param session: session object that was returned from the prior initialize_connection function
    :return: inventory data in a dictionary format
    """
    print("Retrieving the inventory data from Cisco vManage at "+serveraddress+"\n")

    url = "https://" + serveraddress + "/dataservice/device"
    response = session.request("GET", url, verify=False,timeout=10)
    json_string = response.json()


    # Initialize the inventory data dictionary
    inv={}
    # Store each item in the dictionary with the key of the "system-ip"
    for item in json_string['data']:
    #   print (item['local-system-ip']+"   "+item['host-name'])
        inv[item['system-ip']]=item['host-name']

        uptimedate = item['uptime-date']

        version = item['version']

        up=time.gmtime(item['uptime-date']/1000)
        currenttime = time.gmtime(time.time())
        difference = time.time() - (uptimedate/1000)

        if type == "seconds":
            result = str(int(difference))
        else:

            secs=difference
            days = secs//86400
            hours = (secs - days*86400)//3600
            minutes = (secs - days*86400 - hours*3600)//60
            seconds = round(secs - days*86400 - hours*3600 - minutes*60)
            result = ("{} days, ".format(days) if days else "") + \
            ("{} hours, ".format(hours) if hours else "") + \
            ("{} minutes, ".format(minutes) if minutes else "") + \
            ("{0:.0f} seconds".format(seconds) if seconds else "")



        print ("{0:20} {1:15} {2:10} {3}".format(item['host-name'],item['system-ip'],version,result))


    return(inv)




print ("Viptela vManage Engine Starting...\n")

# Open up the configuration file and get all application defaults
try:
    config = configparser.ConfigParser()
    config.read('package_config.ini')

    serveraddress = config.get("application","serveraddress")
    username = config.get("application","username")
    password = config.get("application","password")
    type = config.get("application","format")
except configparser.Error:
    print ("Cannot Parse package_config.ini")
    exit(-1)

print ("Viptela Configuration:")
print ("vManage Server Address: "+serveraddress)
print ("vManage Username: "+username)

session=initalize_connection(serveraddress,username,password)
if session != False:
    inventory=get_inventory(serveraddress,session, type)

