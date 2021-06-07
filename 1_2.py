#Задание 1
import re
import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

response = requests.get(url)
if response.status_code == 200:
    print(f'Соединение установлено с {url}')
else:
    print(f'Ошибка соединения: {response.status_code}')

with open('parse.txt', 'w', encoding='UTF-8') as f:
    f.write(response.text)

with open('parse.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    while line:
        work_line = []
        line = f.readline().strip()
        remote_addr = re.compile(r'^[\d+\.+]+')
        remote_addr_2 = re.compile(r'^([\:+\d+\w+]+)')
        request_datetime = re.compile(r'\[(.+)\]')
        request_type = re.compile(r'\"(\w+)\s[/]')
        requested_resource = re.compile(r'\s(\/.+)\sHTTP')
        response_code = re.compile(r'\"\s(\d+)\s\d+')
        response_size = re.compile(r'\"\s\d+\s(\d+)')
        try:
            if remote_addr.match(line):
                work_line.append(re.findall(remote_addr, line)[0])
            else:
                work_line.append(re.findall(remote_addr_2, line)[0])
            work_line.append(re.findall(request_datetime, line)[0])
            work_line.append(re.findall(request_type, line)[0])
            work_line.append(re.findall(requested_resource, line)[0])
            work_line.append(re.findall(response_code, line)[0])
            work_line.append(re.findall(response_size, line)[0])
            parsed_raw = tuple(work_line)
        except Exception as e:
            print(e)
        print(parsed_raw)
