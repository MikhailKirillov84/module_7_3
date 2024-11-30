# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут
# file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.


from idlelib.replace import replace
from itertools import count

'''
    Создадим класс "WordsFinder", объект этого класса должен принимать при создании (__init__), неограниченного 
    количество названий файлов и записывать их в атрибут "file_names" в виде списка или кортежа.
    Класс будет содержать метод "get_all_words" - подготовительный метод, который возвращает словарь, для этого 
    создадим переменную "all_words", следующего вида:
    {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}.
    Пройдем циклом "for", чтобы перебрать названия и записать в переменную "file_names".
    Используя оператор "with" откроем(open) для чтения('r') и переберем названия файлов, в переменную "single_line"
    запишем содержимое файла, для тения(read()), в виде строки переведя их в нижний регистр метод (lower()).
    Используя статический метод str.maketrans() который создает и возвращает таблицу преобразования символов, 
    используемую методом строки str.translate()., избавимся от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] 
    в строке. (тире обособлено пробелами, это не дефис в слове).
    Используя метод split() разобьем эту строку на элементы списка, и запишем в переменную "line_elem".
    Добавим в переменную "all_words" результат переменной "line_elem" в месте с названием файла.
    Вернем (return) результат переменной.
    
    Создадим метод "find(self, word)" - метод, где "word" - искомое слово. Возвращает словарь, где ключ - название файла, 
    значение - позиция первого такого слова в списке слов этого файла.
    Создадим переменную "find_words", которая будет содержать пустой словарь.
    Искомое слово будем представлять в нижнем регистре методом (lower()).
    Пройдем циклом "for", чтобы перебрать названия файла и содержимое переменной "all_words", 
    в содержимом метода "get_all_words".Для перебора одновременно ключа(названия) и значения(списка слов) 
    воспользуемся методом словаря - item().
    Создадим условие(if), если искомое слово(word) есть в переменной "all_words", тогда записываем в переменную "find_words" 
    значение переменной "all_words" в виде индекса используя метод "index(word)" в месте с названием файла.
    Вернем (return) результат переменной.
    
    Создадим метод "count(self, word)" - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
    значение - количество слова word в списке слов этого файла.
    Создадим переменную "count_words", которая будет содержать пустой словарь.
    Искомое слово будем представлять в нижнем регистре методом (lower()).
    Пройдем циклом "for", чтобы перебрать названия файла и содержимое переменной "words",
    в содержимом метода "get_all_words".
    Для перебора одновременно ключа(названия) и значения(списка слов) воспользуемся методом словаря - item().
    Записываем в переменную "count_words" значение переменной "words" в виде значения количества вхождений 
    искомого слова(word) в строке.
    Вернем (return) результат переменной.
'''
import string
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_names in self.file_names:
            with (open(file_names, 'r', encoding='utf-8') as file):
                single_line = file.read().lower()
                replacing = str.maketrans(',', ',', string.punctuation + '-')
                single_line = single_line.translate(replacing)
                line_elem = single_line.split()
                all_words[file_names] = line_elem
        return all_words

    def find(self, word):
        find_words = {}
        word = word.lower()
        for file_names, all_words in self.get_all_words().items():
            if word in all_words:
                find_words[file_names] = all_words.index(word)
        return find_words

    def count(self, word):
        count_words = {}
        word = word.lower()
        for file_names, words in self.get_all_words().items():
            count_words[file_names] = words.count(word)
        return count_words

# Подготовим заранее файл с текстом ('test_file.txt'), создадим переменную (finder2) куда передадим класс "WordsFinder",
# с названием файла на который применим действие функций.
if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего
