from cryptography.fernet import Fernet
from datetime import datetime
import json
import os
import random
import string


def get_key_file_name(key):
    file_name = key[-20:]
    key = key[:-20]
    return (key, file_name)


def get_random_string(length):
    letters = string.ascii_letters
    file_name = ''.join(random.choice(letters) for _ in range(length))
    if not check_file(file_name):
        get_random_string(length)
    return file_name


def check_file(file_name):
    file_name = file_name + '.json'
    return os.path.isfile(os.path.join('storage', 'files', file_name))


class __encryption__:
    def __init__(self, key):
        self.__fernet__ = Fernet(key)

    def encrypt(self, s):
        return self.__fernet__.encrypt(s)

    def decrypt(self, s):
        return self.__fernet__.decrypt(s)


class file_manager:
    def __init__(self, ip):
        self.pseudo_file_name = None
        self.pseudo_file_name_json = None
        self.filename = None
        self.ip = ip

    def create_json(self):
        dictionary = {
            'name': self.filename,
            'file_location': os.path.join('storage', 'files', self.pseudo_file_name),
            'onetime': self.onetime,
            'time': get_date_time(),
            'ip': self.ip
        }
        json_data = json.dumps(dictionary)
        file_name = self.pseudo_file_name_json + '.json'
        file = open(os.path.join('storage', 'json', file_name), 'w')
        file.write(json_data)
        file.close()

    def writefile(self, filename):
        self.filename = filename
        key = Fernet.generate_key()
        enc = __encryption__(key)
        file_data = enc.encrypt(file.read())
        self.pseudo_file_name = get_random_string(20)
        self.pseudo_file_name_json = get_random_string(20)
        self.create_json()
        file = open(os.path.join('storage', 'files', self.pseudo_file_name), 'wb')
        file.write(file_data)
        file.close()
        return str(key)[2:-2] + self.pseudo_file_name_json

    def readfile(key):
        key_file_name = get_key_file_name(key)
        json_data = json.loads(open(os.path.join('storage', 'json', key_file_name[1]), 'r').read())
        
        file_name = json_data['name']
        file_location = json_data['file_location']
        file_data = open(file_location, 'rb').read()
        enc = __encryption__(key)
        file_data =  enc.decrypt(key_file_name[0])
        open(os.path.join('storage', 'temp', file_name), 'rb').write(file_data)
        return True




