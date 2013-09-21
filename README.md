Stock Checker
=============================

There are two python scripts that checks Adafruit and Sparkfun products for stock status. 
It can handle multiple products and will email if there is a change and how many within the set time.
The first run it sends an email with all items in the list and their current status. 
Handles unknown stock and out of stock status as well.
This could be a good starting point to be modifed for any online shop. 


This is great to track your favorite items that you would like to buy soon or if you have your items in the Adafruit or Sparkfun shop. 
Also great if you are curious about how popular an item is. Could be extended with data over time and graphs of how fast an item moves.

This was developed and tested using a Raspberry Pi Model B 256MB.

----

The header of the file has a few settings you can set:


Make sure the pro_stock array has the same number of elements as the products array.


##Product IDs to check
products = [1456, 1105, 1292, 1488, 1491, 1484, 1480]

pro_stock = [0, 0, 0, 0, 0, 0, 0]


##Time in between checks in seconds
_checkTimer = 900_


##Gmail Settings


_GMAIL_USER = 'username'_

_GMAIL_PASS = 'password'_

_SMTP_SERVER = 'smtp.gmail.com'_

_SMTP_PORT = 587_

____

Also you need the BeautifulSoup4 libraray for the Adafruit stock checker.

More info: [http://www.crummy.com/software/BeautifulSoup/](http://www.crummy.com/software/BeautifulSoup/)


This can be added to a cron job to run on startup.

echo '@reboot ~/ada_stock.py' | crontab


License: All source code and designs are released under 

Creative Commons - By - ShareAlike 

CC BY-SA

![CC BY-SA](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)