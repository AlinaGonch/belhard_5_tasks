"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""
from collections import Counter


def common_and_longest(text: str) -> tuple:
    common = Counter(text.split(' ')).most_common(1)[0][0]
    len_words = [len(word) for word in text.split(' ')]
    longest = text.split(' ')[len_words.index(max(len_words))]
    return common, longest


if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
