import re

# Пример HTML документа
html_document = """
<html>
<body>
  <p>Мой e-mail: example1@example.com</p>
  <p>Еще один e-mail: another@example.com</p>
  <p>Контактный e-mail: contact@domain.com</p>
  <a href="mailto:info@company.com">Контакты</a>
  
</body>
</html>
"""

# Используем регулярные выражения для извлечения электронных адресов
email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html_document)

# Выводим найденные адреса
for email in email_addresses:
    print(email)
