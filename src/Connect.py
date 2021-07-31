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

    def select(self, ip, mac):
        sql = 'SELECT IP, MAC FROM TB_NETWORK WHERE IP = %s AND MAC = %s'
        self.curs.execute(sql,(ip, mac))
        data = self.curs.fetchall()
        
        return len(data)

    def insert(self, ip, mac, auth):
        sql = 'INSERT INTO TB_ACCESS_HIS (IP, MAC, REG_DATE, AUTH_YN) VALUES (%s, %s, DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL 9 HOUR), %s)'
        self.curs.execute(sql,(ip, mac, auth))
        self.conn.commit()

    def close(self):
        self.curs.close()
        self.conn.close()