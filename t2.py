import pickle
import datetime

with open('data.pickle', 'rb') as file:
    data = pickle.load(file)


def func1(data):
    data_base = dict()
    for item in data:
        splited = item['body'].split(' ')
        for words in splited:
            if len(words) > 5 and words in data_base:
                data_base[words] += 1
            else:
                data_base[words] = 0

    value = list(data_base.values())
    key = list(data_base.keys())
    max_ = 0
    top_of_words = []
    for i in range(10):
        for j in range(len(value)):
            if value[j] > max_:
                max_ = value[j]
        top_of_words.append(key[j])
        value.pop(j)

    return top_of_words


def mes_len(some_message):
    message_len = len(some_message['body'])
    return message_len


def func2(data):
    len_ = list(map(mes_len, data))
    return sum(len_) / len(data)


def func5(data, word):
    word = word.lower()
    was_writed = 0

    for mes in data:
        any_mes = mes['body'].lower()
        if word in any_mes:
            was_writed += 1

    return was_writed / len(data)
