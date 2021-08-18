import re

pattern = re.compile(r'(.+)\s[-]\s[-].+'
                     r'(\d{2}[/]\w{3}[/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2}\s[+]\d{4})'
                     r'.{3}(\w{3,4})\s'
                     r'([/]\w+[/]\w+)\s'
                     r'.+(\d{3})'
                     r'\s(\d+)\s')

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for raw in f:
        result = pattern.search(raw)
        parsed_row = (result.group(1), result.group(2), result.group(3),
                      result.group(4), result.group(5), result.group(6))
        print(parsed_row)
