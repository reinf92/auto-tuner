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

    def selectVersion(self):
        sql = 'SELECT PV.PRG_VER ver, PV.PRG_LINK link FROM AN_PRG P LEFT JOIN AN_PRG_VER PV ON P.PRG_ID = PV.PRG_ID ORDER BY VER DESC LIMIT 1'
        self.curs.execute(sql)
        data = self.curs.fetchall()
        print(data)
        print(data[0])
        
        return data[0]

    def selectUser(self, ip, mac):
        sql = 'SELECT USER_IP IP, USER_MAC_ADDR MAC FROM AN_USER WHERE USER_IP = %s AND USER_MAC_ADDR= %s'
        self.curs.execute(sql,(ip, mac))
        data = self.curs.fetchall()
        
        return len(data)

    def insertUseHistory(self, ip, mac):
        sql = 'INSERT INTO AN_TUNE_USAGE (USER_ID, REG_DATE) VALUES ((SELECT USER_ID FROM AN_USER WHERE USER_IP = %s AND USER_MAC_ADDR = %s), CURRENT_TIMESTAMP())'
        self.curs.execute(sql,(ip, mac))
        self.conn.commit()

    def insertNotAuthorized(self, ip, mac):
        sql = 'INSERT INTO AN_TUNE_ACCESS (IP, MAC_ADDR, REG_DATE) VALUES (%s, %s, CURRENT_TIMESTAMP())'
        self.curs.execute(sql,(ip, mac))
        self.conn.commit()

    def close(self):
        self.curs.close()
        self.conn.close()