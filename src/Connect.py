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
        self.curs.close()
        self.conn.close()
        
        return len(data)

    def insert(self, ip, mac):
        sql = 'INSERT INTO TB_ACCESS_HIS (IP, MAC, REG_DATE) VALUES (%s, %s, DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL 9 HOUR))'
        self.curs.execute(sql,(ip, mac))
        self.conn.commit()

    def close(self):
        self.curs.close()
        self.conn.close()