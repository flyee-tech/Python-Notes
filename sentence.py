import string
import os
import re


def main():
    files = os.listdir('/Users/Peiel/Desktop/algo4-words/')
    print(len(files))
    sentances = set()
    for f in files:
        if f.find('txt') == -1:
            continue
        f = open("/Users/Peiel/Desktop/algo4-words/%s" % f, "r", encoding='utf-8')
        content = f.read()
        content = content.replace('\n', '')
        for sentance in content.split('.'):
            sentances.add('%s.' % sentance)
    print('sentances %s' % len(sentances))
    with open('/Users/Peiel/Desktop/sentence.txt', 'w') as f:
        for s in sentances:
            f.write(s)
            f.write('\n')


if __name__ == '__main__':
    main()
