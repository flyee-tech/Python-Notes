import _thread
import time
from configparser import ConfigParser

import pandas as pd
import pymysql

is_break = False


def main(sql):
    """
    简单的查询一秒内执行sql语句成功的次数
    """
    cfg = ConfigParser()
    cfg.read('mysql_conf.ini')
    host = cfg.get('MYSQL', 'host')
    user = cfg.get('MYSQL', 'user')
    passwd = cfg.get('MYSQL', 'passwd')
    db = cfg.get('MYSQL', 'db')
    conn = pymysql.connect(host=str(host), port=3306, user=str(user), passwd=str(passwd), db=str(db))

    def loop():
        cnt = 0
        while True:
            df = pd.read_sql(sql, con=conn)
            cnt = cnt + 1
            if is_break:
                print(cnt)
                break

    def sleepAndBreak(delay):
        global is_break
        time.sleep(delay)
        is_break = True
        print("set is break is : %s " % is_break)

    _thread.start_new_thread(sleepAndBreak, (1,))
    _thread.start_new_thread(loop, ())

    time.sleep(2)


if __name__ == '__main__':
    # sql = '''
    # select user.id from user left join user_car as c on c.user_id = user.id where user.id = 1
    # '''
    sql = '''
    select * from user where id = 1;
    '''

    main(sql)
