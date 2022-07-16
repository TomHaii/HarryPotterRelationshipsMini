import io
import re


class Book:
    def __init__(self, file):
        self.book = io.open(file, 'rt', encoding='utf-8', newline='\n').readlines()
        self.words = []
        for line in self.book:
            stripped_line = line.split(' ')
            for word in stripped_line:
                only_chars_word = re.sub(r'[^A-Za-z]', '', word)
                self.words.append(only_chars_word.lower())
