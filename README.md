# sdwan-uptime

## Description
This is a very basic application to query the vManage application within a Cisco SD-WAN (Viptela) Infrastructure. It will return a very basic report to show the uptime of all sdwan devices within the infrastructure.



## Requirements and Prerequisites
### package_config.ini
The code uses a file called the package_config.ini to house the information about the vManage and the credentials that the application uses.     In the repository, there is a ```package_config.ini.sample``` that you should rename to ```package_config.ini```.   Then modify the package_config.ini to reflect the following information:
* **serveraddress** - Represents the ip address of the vManage server
* **username** -  username of the login credentials on the vManage server
* **password** - password of the login credentials on the vManage server
* **format** - format of the output.   If the value is *seconds* then it will display the uptime date in seconds format.   If it is anything else, it will display in text notation.

### python
This demo example is based on Python 3.7 and was tested successfully under that version.

There are two main requirements for external libraries:
* requests
* configparser

You can install these prerequisites by the following commands:
```
pip install requests
pip install configparser
```


## Example Output
```
Viptela vManage Engine Starting...

Viptela Configuration:
vManage Server Address: 172.18.52.16:8443
vManage Username: admin
Retrieving the inventory data from Cisco vManage at 172.18.52.16:8443

vmanage              2.1.1.1          - 1.0 days, 14.0 hours, 46.0 minutes, 16.70 seconds, 
vSmart1              2.1.1.3          - 53.0 days, 19.0 hours, 42.0 minutes, 16.70 seconds, 
vSmart2              2.1.1.4          - 53.0 days, 19.0 hours, 42.0 minutes, 16.70 seconds, 
vSmart3              2.1.1.5          - 53.0 days, 19.0 hours, 42.0 minutes, 16.70 seconds, 
vbond                2.1.1.2          - 53.0 days, 19.0 hours, 42.0 minutes, 16.70 seconds, 
C1111-8P             1.1.255.1        - 10.0 days, 3.0 hours, 11.0 minutes, 16.70 seconds, 
DC-ASR1001HX-RTR1    1.1.200.1        - 54.0 days, 1.0 hours, 13.0 minutes, 16.70 seconds, 
DC-ASR1002X-RTR2     1.1.250.1        - 54.0 days, 1.0 hours, 10.0 minutes, 16.70 seconds, 
ISR1k-1              1.1.135.1        - 11.0 days, 2.0 hours, 2.0 minutes, 16.70 seconds, 
cEdge-br1            1.1.100.1        - 54.0 days, 1.0 hours, 15.0 minutes, 16.70 seconds, 
cEdge-br2            1.1.110.1        - 54.0 days, 1.0 hours, 16.0 minutes, 16.70 seconds, 
site250-vEdge-1000-1 1.1.250.2        - 12.0 days, 20.0 hours, 52.0 minutes, 16.70 seconds, 
vEdge-cloud-1        1.1.150.1        - 24.0 minutes, 16.70 seconds, 
vEdge2000            1.1.201.1        - 35.0 days, 4.0 hours, 3.0 minutes, 16.70 seconds```


