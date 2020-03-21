import string
import os
import re


def main():
    files = os.listdir('/Users/Peiel/Desktop/algo4-words/')
    print(len(files))
    words = set()
    for f in files:
        if f.find('txt') == -1:
            continue
        f = open("/Users/Peiel/Desktop/algo4-words/%s" % f, "r", encoding='utf-8')
        for line in f.readlines():
            line = line.strip('\n')
            line = line.strip(string.digits)
            line = line.strip(string.punctuation)
            line = line.rstrip(string.punctuation)
            for word in line.split(' '):
                if word.__contains__("'") \
                        or word.__contains__("]") \
                        or word.__contains__("[") \
                        or word.__contains__(";") \
                        or word.__contains__("?") \
                        or word.__contains__("/") \
                        or word.__contains__("<") \
                        or word.__contains__("+") \
                        or word.__contains__("(") \
                        or word.__contains__(")") \
                        or word.__contains__("^") \
                        or word.__contains__(",") \
                        or word.__contains__(".") \
                        or word.__contains__('"') \
                        or word.__contains__("-"):
                    continue
                if bool(re.search(r'\d', word)):
                    continue
                if five_set.__contains__(word):
                    continue
                if len(word) <= 3:
                    continue
                if not word.isalpha():
                    continue
                word = word.lower()
                ins_sentence = ''
                cnt = 0
                for sen in sentence_list:
                    if word in sen.lower():
                        cnt = cnt + 1
                i = 1
                for sen in sentence_list:
                    if word in sen.lower():
                        ins_sentence = ins_sentence + '<br>%s.' % i + sen + '<br>'
                        i = i + 1
                        if ins_sentence.count('\n') > 7:
                            break
                ins_sentence = ins_sentence.replace('\n', '')
                ins_sentence = ins_sentence.replace('|', '')
                words.add('%s|sentence cnt : %s <br> %s' % (word, cnt, ins_sentence))
    print('five %s' % len(five_set))
    print('words %s' % len(words))
    with open('/Users/Peiel/Desktop/words_2.txt', 'w') as f:
        for w in words:
            f.write(w)
            f.write('\n')


def five():
    f = open("/Users/Peiel/Desktop/five.txt", "r", encoding='utf-8')
    for line in f.readlines():
        line = line.strip('\n')
        line = line.strip(string.digits)
        line = line.strip(string.punctuation)
        line = line.rstrip(string.punctuation)
        for word in line.split(' '):
            five_set.add(word)


five_set = set()
sentence_list = list()


def sentence():
    f = open("/Users/Peiel/Desktop/sentence.txt", "r", encoding='utf-8')
    for line in f.readlines():
        sentence_list.append(line)


if __name__ == '__main__':
    five()
    sentence()
    main()
