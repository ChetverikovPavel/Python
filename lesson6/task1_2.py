content = []
content_ip = []
spam = 0
spam_ip = 0
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for el in f:
        content_tuple = (el.split(' - -')[0], el.split('] "')[1].split(' /')[0], el.split(' HTTP')[0].split(' ')[6])
        content.append(content_tuple)

for el in content:
    content_ip.append(el[0])
    print(el)

ip_set = set(content_ip)
for el in ip_set:
    if content_ip.count(el) > spam:
        spam_ip = el
        spam = content_ip.count(el)
print(f'ip: {spam_ip}, Количество запросов: {spam}')

