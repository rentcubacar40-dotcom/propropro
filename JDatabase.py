import os
import json
import time
import io
from datetime import datetime

class JsonDatabase(object):
    def __init__(self,path='newdb'):
        self.path = f'{path}.jdb'
        self.items = {}

    def check_create(self):
        exist = os.path.isfile(self.path)
        if not exist:
            db = open(str(self.path), 'w')
            db.write('')
            db.close()

    def save(self):
        dbfile = open(self.path, 'w')
        i = 0
        for user in self.items:
            separator = ''
            if i < len(self.items) - 1:
                separator = '\n'
            dbfile.write(user + '=' + str(self.items[user]) + separator)
            i += 1
        dbfile.close()

    def create_user(self,name):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.items[name] = {
            'dir': '',
            'cloudtype': 'moodle',
            'moodle_host': '',
            'moodle_repo_id': 4,
            'moodle_user': '',
            'moodle_password': '',
            'isadmin': 0,
            'zips': 100,
            'uploadtype':'draft',
            'proxy':'',
            'tokenize':0,
            # NUEVOS CAMPOS DE ESTADÍSTICAS
            'upload_count': 0,
            'total_mb_used': 0,
            'last_upload': '',
            'first_upload': '',
            'account_created': current_time
        }

    def create_admin(self,name):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.items[name] = {
            'dir': '',
            'cloudtype': 'moodle',
            'moodle_host': 'https://aulacened.uci.cu/',
            'moodle_repo_id': 5,
            'moodle_user': 'eliel21',
            'moodle_password': 'ElielThali2115.',
            'isadmin': 1,
            'zips': 100,
            'uploadtype':'draft',
            'proxy':'',
            'tokenize':0,
            # NUEVOS CAMPOS DE ESTADÍSTICAS
            'upload_count': 0,
            'total_mb_used': 0,
            'last_upload': '',
            'first_upload': '',
            'account_created': current_time
        }

    def remove(self,name):
        try:
            del self.items[name]
        except:pass

    def get_user(self,name):
        try:
            return self.items[name]
        except:
            return None

    def save_data_user(self,user, data):
        # SOLO GUARDA LOS DATOS, NO AGREGA NADA
        self.items[user] = data

    def is_admin(self,user):
        User = self.get_user(user)
        if User:
            return User['isadmin'] == 1
        return False

    def get_all_users(self):
        """Obtiene todos los usuarios registrados"""
        return self.items

    def get_user_count(self):
        """Obtiene el número total de usuarios"""
        return len(self.items)

    def load(self):
        dbfile = open(self.path, 'r')
        lines = dbfile.read().split('\n')
        dbfile.close()
        for lin in lines:
            if lin == '': continue
            tokens = lin.split('=')
            user = tokens[0]
            data = json.loads(str(tokens[1]).replace("'", '"'))
            self.items[user] = data
