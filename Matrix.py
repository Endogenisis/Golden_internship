n=int(input())
p=n+n-1 # Размер матрицы
d=0 # Переменная строки сверху
e=p # Переменная столбца справа
f=p # Переменная строки снизу
h=0 # Переменная столба слева
t=p # Для вывода матрицы
por=n # Число для записи
c = [[0 for j in range(p)] for i in range(p)]
for i in range(1): # Первая строка слева-направо
    for j in range(p):
        c[i][j]+=por
    d+=1
while por!=1:
    for j in range(e-1,e): # Сверху-вниз правый столбец
        for i in range(d,f):
            c[i][j]+=por
    e-=1
    for i in range(f-1,f): # Справа-налево нижняя строка
        for j in range(e-1,h-1,-1):
            c[i][j]+=por
    f-=1
    p-=1
    for j in range(h,h+1): # Снизу вверх левый столбец
        for i in range(f-1,d-1,-1):
            c[i][j]+=por
    h+=1
    por-=1
    for i in range(d, d+1):
        for j in range(h, e):
            c[i][j]+=por
    p-=1
    d+=1
for i in range(t):
    for j in range(t):
        print(c[i][j], end=" ")
    print()