import os
import sys
import unicodedata

import nested_dict as nd
from pathspec.compat import unicode


class Levenshtein():
    def not_ready_to_levenshtein(path_name):
        word = ""
        string = ".,();:!?"
        with open(os.path.basename(path_name), "r") as file:
	        f = file.readlines()

        a = " ".join(map(str,f))

        for char in string:
            a = a.replace(char, "")
            a = a.replace('"', '')
            a = a.replace('\\n', "")
            a = a.replace('\n', "")
        flat_list = a.split(" ")

        for element in flat_list:
            if element == "":
                flat_list.remove(element)
            else:
                if type(element) != unicode:
                    flat_list.remove(element)
                    new_element = element.decode("utf-8")
                    flat_list.append(new_element)
                else:
                    new_element = element

        return flat_list


    def ready_to_levenstein(flat_list, sentence, new_dictionary):
        d = {}
        count = 0
        check_words = []
        for s1 in sentence:
            count = 0
            check_words = []
            for s2 in flat_list:
                lenstr1 = len(s1)
                lenstr2 = len(s2)
                for i in range( - 1, lenstr1 + 1):
                    d[(i, - 1)] = i + 1
                for j in range( - 1, lenstr2 + 1):
                    d[( - 1, j)] = j + 1
                for i in range(lenstr1):
                    for j in range(lenstr2):
                        if s1[i] == s2[j]:
                            cost = 0
                        else:
                            cost = 1
                        d[(i,j)] = min(
                                        d[(i - 1,j)] + 1, # deletion
                                        d[(i,j - 1)] + 1, # insertion
                                        d[(i - 1,j - 1)] + cost, # substitution
                                     )
                        if i and j and s1[i] == s2[j - 1] \
                             and s1[i - 1] == s2[j]:
                            d[(i,j)] = min (d[(i,j)],
                                            d[i - 2,j - 2] + 1)
                if (d[lenstr1 - 1,lenstr2 - 1] == 1 or
                d[lenstr1 - 1,lenstr2 - 1] == 2
                or d[lenstr1 - 1, lenstr2 - 1] == 0 ):
                    word = s1
                    s2 = s2.lower()
                    if s2 not in check_words:
                        check_words.append(s2)
                        count += 1
                        new_dictionary[word][str(count)] = s2
        return new_dictionary


    def print_something(the_dictionary):
        for k, v in the_dictionary.items():
            print("Неправильное слово: " + k)
            for k1, v1 in v.items():
                print(k1 + ": " + v[k1])
            a = input("Введите номер правильного слова: ")
            if (len(v) < int(a) or int(a) < 1):
                print("Вы ввели неправильное число")
            else:
                print(v[a])


    new_dictionary = nd.nested_dict()
    sentence = input().split(" ")
    if (sentence == " - h " or sentence == " - help"):
        print("В папке файла есть файл readme.txt, "
              "в котором можно прочитать подробную информацию. ")
        sys.exit()
    path_name = input()
    the_dictionary = not_ready_to_levenshtein(path_name)
    haha = ready_to_levenstein(the_dictionary, sentence,new_dictionary)
    print_something(haha)