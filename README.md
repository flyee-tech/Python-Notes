## 基础操作

<details>
<summary>执行命令</summary>
<pre>
<code>
# 简单的方式，还有其他方式，网上查询。
os.system('cd .. && hexo clean && hexo g && hexo d')
</code>
</pre>
</details>

<details>
<summary>读写文件</summary>
<pre>
<code>
with open('$path', 'r') as f:
    # 读取全部
    print(f.read())
    # 行读取 
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
</code>
<code>
with open('$path', 'w') as f:
    f.write('Hello, world!')
</code>
</pre>
</details>


## Pandas

## Numpy
