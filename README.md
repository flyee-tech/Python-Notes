# Python-Nodes

> build by: python3.X+

## base opt

### exec command

```python
# has other way, to google search!
os.system('cd .. && hexo clean && hexo g && hexo d')
```

### file read write
```python
with open('$path', 'r') as f:
    # read all
    print(f.read())
    # read by line 
    for line in f.readlines():
        print(line.strip()) # remove end '\n'
```
```python
with open('$path', 'w') as f:
    f.write('Hello, world!')
```

### MySQL

```python
import pymysql
conn = pymysql.connect(host=str(host), port=3306, user=str(user), passwd=str(passwd), db='quantify_data')
cursor = conn.cursor()
cursor.execute('insert sql')
conn.commit()
conn.close()
```

### JSON

```python
json_obj = json.loads(json_str)
json_str = json.dumps([T])
```

### MD5

```python
import hashlib
md5 = hashlib.md5('$sth').hexdigest()
```

### HTTP

```python
import urllib.request
# post submit a bytes data
host = 'http://blog.peiel.com/'
req = urllib.request.Request(host, bytes(str_urls, encoding="utf8"), {'Content-Type': 'text/plain', 'Content-Length': len(str_urls)})
f = urllib.request.urlopen(req)
response = f.read()
f.close()
print(response)
```

## Pandas

### Query data from mysql

```python
df = pd.read_sql(sql='select * from ...', con=conn)
```

### Convert a column data to a list

```python
list(df['column_name'])
df['column_name'].tolist()
```

## Numpy
