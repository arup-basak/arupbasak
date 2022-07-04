from datetime import datetime

def get_date_time():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")