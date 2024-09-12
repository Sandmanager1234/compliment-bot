import sqlite3

class DBmanager:
    def __init__(self):
        self.conn = sqlite3.connect('compliments.db')
        self.curr = self.conn.cursor()
    

    def create_tables(self):
        self.curr.execute("CREATE TABLE users(id INTEGER, tg_id INTEGER, is_vstr BLOB);")
        self.curr.execute("CREATE TABLE compliments(id INTEGER, text TEXT);")
        self.conn.commit()

    def user_exists(self, tg_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.curr.execute("SELECT `id` FROM `users` WHERE `tg_id` = ?", (tg_id,))
        return bool(len(result.fetchall()))
    
    def user_is_active(self, tg_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.curr.execute("SELECT is_vstr FROM `users` WHERE `tg_id` = ?", (tg_id,))
        return bool(result.fetchone()[0])

    def add_user(self, tg_id, is_vstr=True):
        self.curr.execute('INSERT INTO users(tg_id, is_vstr) VALUES(?, ?);', (tg_id, is_vstr))
        self.conn.commit()
    
    def change_user(self, tg_id, is_vstr=False):
        self.curr.execute('UPDATE users SET is_vstr = ? WHERE tg_id = ?', (is_vstr, tg_id))
        self.conn.commit()

    def get_users(self):
        res = self.curr.execute('SELECT tg_id FROM users WHERE is_vstr = ?', (1, ))
        return res.fetchall()

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    db = DBmanager()
    # db.add_user(123456789)
    res = db.user_is_active(123456789)
    print(res)
    res2 = db.user_exists(1234567089)
    print(res2)
    # db.delete_user(123456789)
    # res1 = db.get_users()
    # print(res1)