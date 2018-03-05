import redis

host = '192.168.1.73'
index = '5'
password = '******'
# 要匹配的正则
pattern = 'abc*'


def getRedisClient(host, database, passwd):
    r = redis.StrictRedis(host='%s' % host, port=6379, db=database, password='%s' % passwd)
    return r


client = getRedisClient(host, index, password)
for key in client.keys(pattern):
    print(key)
    client.delete(key)

    # redis的del命令不支持正则匹配，所以用python写个小脚本
    # 修改全局变量执行批量删除
