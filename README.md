## 基础操作
  
### 执行命令
```python
# 简单的方式，还有其他方式，网上查询。
os.system('cd .. && hexo clean && hexo g && hexo d')
```
### 读写文件

```python
with open('$path', 'r') as f:
    # 读取全部
    print(f.read())
    # 行读取 
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
```

```python
with open('$path', 'w') as f:
    f.write('Hello, world!')
```

## Pandas

## Numpy
