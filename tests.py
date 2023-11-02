import find_errors_in_sentences
import unittest


def test_app():
    input_values = [
        "their",
        r"C:\Users\Пользователь\PycharmProjects\pythonProject\spellchecker.txt",
        1,
    ]
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    find_errors_in_sentences.input = mock_input
    find_errors_in_sentences.print = lambda s: output.append(s)

    # find_errors_in_sentences.print_something()

    assert output == [
        "Sentence: ",
        "Path: " "Неправильное слово: their",
        "Введите номер правильного слова: 1",
        "they",
    ]
