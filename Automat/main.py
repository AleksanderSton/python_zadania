import random


def random_string(length):
    result = ''
    for i in range(length):
        rand = random.choice(['*', '_'])
        result += rand
    return result


def process_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        rule = lines[0].strip().split(": ")[1]
        n = int(lines[1].strip().split(": ")[1])
        k = int(lines[2].strip().split(": ")[1])
    return rule, n, k

file_path = input("enter the path to Your .cfg file ")
rule, n, k = process_input_from_file(file_path)

dictionary = {'***': rule[0],
              '**_': rule[1],
              '*_*': rule[2],
              '*__': rule[3],
              '_**': rule[4],
              '_*_': rule[5],
              '__*': rule[6],
              '___': rule[7]}

rand_str = random_string(n)
result = ''
print(dictionary)
for i in range(k):
    temp = rand_str[i % n] + rand_str[(i + 1) % n] + rand_str[(i + 2) % n]
    value = int(dictionary.get(temp))
    if value == 1:
        result += '*'
    elif value == 0:
        result += '_'
if k < n:
    for i in range(n - k):
        result += '_'
print(rand_str)
print(result)
