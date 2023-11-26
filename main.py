import re

# Чтение содержимого HTML-файла
with open('index.html', 'r', encoding='utf-8') as file:
    html_document = file.read()
    
# Используем регулярные выражения для извлечения электронных адресов
email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html_document)

# Выводим найденные адреса
for email in email_addresses:
    print(email)
