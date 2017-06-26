def ask_ok(prompt, retries=4, complaint='yes or no, please!'):  # 默认参数值
    while True:
        ok = input(prompt)
        if ok in ['y', 'ye', 'yes']:
            return True
        if ok in ['n', 'no', 'nop', 'nope']:
            return False
        retries -= 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


result = ask_ok('Do you really want to quit?')
print(result)
result = ask_ok('OK to overwrite the file?', 2)
print(result)
result = ask_ok('OK to overwrite the file?', 2, 'Come on, Only yes or no!')
print(result)

i = 5


def f(arg=i):
    print(arg)


i = 6
f()
