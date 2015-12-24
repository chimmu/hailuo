import pymysql
import json
class DbConn:
    def __init__(self, conf):
        with open(conf, 'r') as fp:
            hdl = json.load(fp)
            self.table = hdl['table']
            self.db = hdl['db']
            self.user = hdl['user']
            self.passwd = hdl['passwd']
            self.host = hdl['host']
            self.port = hdl['port']
            self.conn = pymysql.connect(host=self.host,
                                    port=self.port, user=self.user,
                                     password=self.passwd, charset='utf8',
                                     db=self.db)
        
    def checkPasswd(self, user, passwd):
        cmd = 'select passwd from ' + self.table + ' where username="' + user + '"'
        cursor = self.conn.cursor()
        cursor.execute(cmd)
        for item in cursor:
            print('item is {0}'.format(item))
            return passwd == item[0]
    def getUserInfo(self, user):
        cmd = 'select id,username,passwd from ' + self.table + ' where username="' + user + '"'
        cursor = self.conn.cursor()
        cursor.execute(cmd)
        for item in cursor:
            return item
    
g_dbConn = DbConn('db.conf')