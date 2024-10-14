import string
from collections import defaultdict

def analyze_text(text):
    # Удаляем знаки препинания и приводим текст к нижнему регистру
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Разбиваем текст на слова
    words = text.split()
    
    # Создаем словарь для хранения частоты слов
    word_count = defaultdict(int)
    
    # Подсчитываем частоту появления каждого слова
    for word in words:
        word_count[word] += 1
    
    # Сортируем слова по частоте (по убыванию) и алфавиту
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
    
    # Выводим результат
    for word, count in sorted_words:
        print(f"{word}: {count}")

# Запрашиваем текст у пользователя
user_input = input("Введите текст: ")
analyze_text(user_input)