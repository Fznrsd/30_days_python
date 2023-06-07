import re
import json
import csv
import math
import sys
import string

# level 1
# q no. 1

# def read_file(file_path= "/home/faizan/30_days_python/day_19/obama_speech.txt"):
#   try:
#     with open(file_path, 'r', encoding='utf-8') as f:
#       file_content = f.read()
#       # if file != '':
#       print("File opened successfully.")
#       return file_content
#   except Exception as e:
#      print(e)

# file_content = read_file()
# # print(file_content)
# file_content = file_content.split("\n")
# print(file_content)
# line_count = 0
# for line in file_content:
#   if line.strip():  # Exclude empty lines
#     line_count += 1
# print("Number of lines in the file:", line_count)

# file_content = read_file()
# file_content = file_content.split(" ")
# print(file_content)
# words_count = 0
# for word in file_content:
#   if word.strip():  # Exclude empty lines
#     words_count += 1
# print("Number of words in the file:", words_count)



# q no. 2
# same do in day 10

# level 2
# q no. 4

# with open("/home/faizan/30_days_python/day_19/email_exchange_big.txt") as f:
#     email_addresses = []
#     for line in f:
#         match = re.search(r"(?<=To: )\S+@\S+", line)
#         if match:
#             email_addresses.append(match.group())

# print(email_addresses)

# q no. 5

# def find_most_common_words(file_path= "/home/faizan/30_days_python/day_19/obama_speech.txt", cont= -1):
#     try:       
#         with open(file_path, 'r', encoding='utf-8') as f:
#             file_content = f.read()
#             words = file_content.split()
#             word_counts = {}
#             for i in words:
#                 if i in word_counts:
#                     word_counts[i] = word_counts[i] + 1
#                 else:
#                     word_counts[i] = 1

#         return sorted([(v, k) for k, v in word_counts.items()], reverse=True)[:cont]
#     except Exception as e:
#         print(e)

# print(find_most_common_words(cont=5))

# q no. 6

# in quetion 5 put cont = 10


# q no. 7

# def clean_text(text):
#     text = re.sub('[,.!?;:]', '', text)
#     text = text.lower()
#     stop_words = set(open('/home/faizan/30_days_python/day_19/stop_words.py', 'r').read().split())
#     text = ' '.join([word for word in text.split() if word not in stop_words])
#     return text

# def remove_support_words(text):
#     support_words = ['and', 'the', 'of', 'to', 'was', 'in', 'a', 'that', 'is', 'he']
#     for word in support_words:
#       text = text.replace(word, '')
#     return text

# def check_text_similarity(text1, text2):
#     text1 = clean_text(text1)
#     text2 = clean_text(text2)
#     text1 = remove_support_words(text1)
#     text2 = remove_support_words(text2)
#     text1 = set(text1)
#     text2 = set(text2)
#     jaccard_similarity = len(text1.intersection(text2)) / len(text1.union(text2))
#     return jaccard_similarity   

# if __name__ == '__main__':
#     michelle_speech = open('/home/faizan/30_days_python/day_19/michelle_obama_speech.txt', 'r').read()
#     melina_speech = open('/home/faizan/30_days_python/day_19/melina_trump_speech.txt', 'r').read()
#     similarity = check_text_similarity(michelle_speech, melina_speech)
#     print(f'The similarity between Michelle\'s and Melina\'s speech is {similarity}')

# q no. 8
# same as question 5

# q no. 9

def countRegEx(csv_Obj,regEx):
    csv_reader = csv.reader(csv_Obj, delimiter=',')
    count = 0
    for row in csv_reader:
        for i in row:
            count += len(re.findall(regEx,i))

    csv_Obj.seek(0) #Reset back to start of file
    return count

with open('/home/faizan/30_days_python/day_19/hacker_news.csv','r') as f:
    print(countRegEx(f, r'[Pp]ython'))
    print(countRegEx(f, r'Java'))
    print(countRegEx(f, r'[Jj]ava[Ss]cript'))
