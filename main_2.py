from crm_module import crm_in_list as crm

# Задание 1
(crm[0][1]), type(crm[0][1])

# Задание 2
only_mail = list()
for data in crm:
    only_mail.append(data[1])

# Задание 3
domains = list()
for dom in only_mail:
    domains.append(dom[dom.find('@'):])

# Задание 4
copy_domains_number4 = domains.copy()
for dom in copy_domains_number4:
    if dom[dom.find('@'):] == '@skyeng.ru':
        copy_domains_number4.remove(dom)

# Задание 5
copy_domains_number5 = domains.copy()
for dom in copy_domains_number5:
    if dom[dom.find('@'):] in ('@skyeng.ru', '@skyeng.com'):
        copy_domains_number5.remove(dom)

# Задание 6
# Обычные домены
norm_domains = ['@hotmail.com', '@hotmail.ru', '@yandex.com', '@yandex.ru', '@gmail.com', '@gmail.ru', '@outlook.com',
                '@outlook.ru', '@skyeng.com', '@skyeng.ru', '@mail.com', '@mail.ru']
unic_domain = list()
for dom in domains:
    if dom not in norm_domains:
        unic_domain.append(dom)

##Задание 7
dict_domains = {}
keys = list()
temp = list()

for dom in domains:
    keys.append(dom[dom.find('@'):dom.find('.')])
keys = list(dict.fromkeys(keys))

for k in keys:
    for dom in domains:
        if dom[dom.find('@'):dom.find('.')] == k:
            temp.append(dom)
    temp = list(dict.fromkeys(temp))
    dict_domains[k] = len(temp)
    temp.clear()



