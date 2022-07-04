import random
import string
from datetime import datetime


def get_date_time():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")



#from 48 to 90, remove 58- 64
print(get_date_time())
