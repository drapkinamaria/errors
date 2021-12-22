import os
import time
import sys

DICTIONARY_PATH = input()
if DICTIONARY_PATH == "-h" or DICTIONARY_PATH == "--help":
    print(
        "В папке файла есть файл readme.txt,  в котором можно прочитать подробную информацию. "
    )
    sys.exit()
WORD = input()
MAX_COST = int(input())

NodeCount = 0
WordCount = 0


class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

        global NodeCount
        NodeCount += 1

    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()

            node = node.children[letter]

        node.word = word


trie = TrieNode()

with open(os.path.basename(DICTIONARY_PATH), "r") as file:
    f = file.readlines()
    string = ".,();:!?"
    a = " ".join(map(str, f))

    for char in string:
        a = a.replace(char, "")
        a = a.replace('"', "")
        a = a.replace("\\n", "")
        a = a.replace("\n", "")

    flat_list = a.split(" ")

for word in flat_list:
    WordCount += 1
    trie.insert(word)


def search(word, maxCost):

    currentRow = range(len(word) + 1)

    results = []

    for letter in trie.children:
        searchRecursive(
            trie.children[letter], letter, word, currentRow, results, maxCost
        )

    return results


def searchRecursive(node, letter, word, previousRow, results, maxCost):

    columns = len(word) + 1
    currentRow = [previousRow[0] + 1]

    for column in range(1, columns):

        insertCost = currentRow[column - 1] + 1
        deleteCost = previousRow[column] + 1

        if word[column - 1] != letter:
            replaceCost = previousRow[column - 1] + 1
        else:
            replaceCost = previousRow[column - 1]
        currentRow.append(min(insertCost, deleteCost, replaceCost))

    if currentRow[-1] <= maxCost and node.word != None:
        results.append(node.word)

    if min(currentRow) <= maxCost:
        for letter in node.children:
            searchRecursive(
                node.children[letter], letter, word, currentRow, results, maxCost
            )


results = search(WORD, MAX_COST)
print("Неправильное слово: " + WORD)
for result in results:
    print((results.index(result) + 1), ":", result)
a = input("Введите номер правильного слова: ")
if len(results) < int(a) or int(a) < 1:
    print("Вы ввели неправильное число")
else:
    print(results[int(a) - 1])
