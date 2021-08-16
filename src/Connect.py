import pymysql

class Connect:

    def __init__(self):
        self.conn = pymysql.connect(
            host = '*',
            user = '*',
            password = '*',
            db = '*',
            charset = 'utf8'
        )
        self.curs = self.conn.cursor()

    def selectUser(self, ip, mac):
        sql = 'SELECT ip, mac FROM tb_user WHERE ip = %s AND mac = %s'
        self.curs.execute(sql,(ip, mac))
        data = self.curs.fetchall()
        
        return len(data)

    def insertUseHistory(self, ip, mac):
        sql = 'INSERT INTO tb_use_history (ip, mac, reg_date) VALUES (%s, %s, CURRENT_TIMESTAMP())'
        self.curs.execute(sql,(ip, mac))
        self.conn.commit()

    def insertNotAuthorized(self, ip, mac):
        sql = 'INSERT INTO tb_not_authorized (ip, mac, reg_date) VALUES (%s, %s, CURRENT_TIMESTAMP())'
        self.curs.execute(sql,(ip, mac))
        self.conn.commit()

    def close(self):
        self.curs.close()
        self.conn.close()