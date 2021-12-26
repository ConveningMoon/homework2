# 1 Создай пустой словарь dict_emails
dict_emails = {}

# 2 Добавь туда ключ gmail со значением andrei@gmail.com
dict_emails['gmail'] = 'andrei@gmail.com'

# 3 Добавь по ключу gmail также элементы viktoria@gmail.com и ella@gmail.com, чтобы в значении оказались все три почты.
# Для этого используй список.
dict_emails['gmail'] = [dict_emails['gmail']]
dict_emails['gmail'].append('viktoria@gmail.com')
dict_emails['gmail'].append("ella@gmail.com")

# 4 Выведи каждый e-mail из словаря в новой строчке с помощью цикла for.
for i in dict_emails:
    for j in dict_emails[i]:
        print(j)

# 5 Добавь в словарь ключ yandex со значением liza@yandex.ru
dict_emails['yandex'] = 'liza@yandex.ru'

# 6 Из словаря dict_emails по ключу yandex вытащи значение.
print(dict_emails['yandex'])

from pprint import pprint

pprint(dict_emails)