from datetime import datetime
import os
import string
import random
import shutil
import json


def get_random_string(length):
    letters = string.ascii_letters
    rand = ''.join(random.choice(letters) for _ in range(length))
    return rand


def get_date_time():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")


def push_temp(filename):
    path = os.path.join('storage', 'temp')
    if os.path.exists(os.path.join(path, filename)):
        rand = get_random_string(23)
        json_data = {
            'filename': filename,
            'date_time': get_date_time(),
            'download': False
        }
        file = open(os.path.join(path, rand + '.json'), 'w')
        file.write(json.dumps(json_data))
        file.close()
        os.mkdir(os.path.join(path, rand))
        shutil.move(os.path.join(path, filename), os.path.join(path, rand, filename))
        return rand
    else:
        return None


def get_temp(file_code):
    try:
        path = os.path.join('storage', 'temp')
        file = open(os.path.join(path, file_code + '.json'), 'r')
        json_data = json.loads(file.read())
        path = os.path.join(path, file_code, json_data['filename'])
        if os.path.exists(path):
            return path
        else:
            return None
    except:
        return None
