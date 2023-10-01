#  A MODULE is basically a file containing a set of functions to include in your applicstionn. 
#  There are core python modules ,modules you cam install using the pip package manager (including Django) as well as custom modules


#   CORE MODELS
import datetime
from datetime import date
import time
from time import time




#  PIP MODELS
#pip3 install 

#  IMPORT CUSTOM MODULES
import email_validator
from email_validator import validate_email

email = 'ade@gmail.com'
if validate_email(email):
    print("Email valid")
else:
    print('Email not valid')
#   DATE 
#today = datetime.date.today()
today = date.today()
#print(today)

#   TIME
timestamp = time()
#print(timestamp)
