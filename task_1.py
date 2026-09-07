t = '1h 45m,360s,25m,30m 120s,2h 60s'
result = 0
t = t.replace(' ', ',')
t = t.split(',')
for i in t:
    if 's' in i:
        i = int(i.replace('s', '')) // 60
    elif 'm' in i:
        i = int(i.replace('m', ''))
    elif 'h' in i:
        i = int(i.replace('h', '')) * 60
    result += i

print(f'{result} минут')