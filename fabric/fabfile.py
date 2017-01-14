from fabric.api import *
import time

env.hosts = ['root@192.168.0.1:22']  # ip 端口
env.password = 'password'  # 密码


# local() 执行本地命令
def mvn_pack():
    print("------------------------------------ 开始打包项目 ------------------------------------")
    with lcd("/Users/elong/IdeaProjects/****/"):  # 进入本地目录
        local("mvn clean")
        local("mvn package")


# run() 执行远程服务器的命令
def put_pack():
    print("------------------------------------ 备份服务器原项目 ------------------------------------")
    run("mv ... ..." + time.strftime("%m%d", time.localtime()))
    print("------------------------------------ 开始上传项目包 ------------------------------------")
    put("本地路径", "远程路径")
    print("------------------------------------ 重启Tomcat并打印日志 ------------------------------------")
    run("set -m ; /etc/init.d/tomcat restart")
    time.sleep(2)
    run("tail -f /home/tomcat/logs/catalina.out")


def start():
    mvn_pack()
    put_pack()
