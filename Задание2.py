#Поиск подстроки
s = input().strip()  
t = input().strip()  

# Поиск вхождений
result = []
for i in range(len(s) - len(t) + 1):
    # Проверяю кусок строки s длиной t
    if s[i:i+len(t)] == t:
        result.append(i)

# Вывод результата
print(' '.join(map(str, result)))  


#Циклический сдвиг
s = input().strip()
t = input().strip()

if len(s) != len(t):
    print(-1)
else:
    doubled_s = s + s
    if t in doubled_s:
        pos = doubled_s.index(t)
        shift = (len(s) - pos) % len(s)
        print(shift)
    else:
        print(-1)
