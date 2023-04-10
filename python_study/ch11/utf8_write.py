lines = ['안녕하세요\n', 'おはようございます\n', 'hello\n']

with open('greeting_utf8.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line)
