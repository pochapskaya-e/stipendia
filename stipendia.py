A=[]
B=["ФИО","Англиский язык","Философия","Математический анализ","Информатика и информационно-коммуникационные технологии"]
A.append(B)
i = 1
ob1 = 0
n = int(input("Введите количество студентов - "))
ball = 0 #Минимальный балл по дисциплине
pov = [] #Cписок студентов с повышенной стипендией
ob = [] #Список студентов с обычной стипендией
net  = [] #Список неуспевающих студентов

def srball(C=[]): #Функция для вычисления среднего балла
    sred=0  
    name = C[0] 
    for j in range(1,len(B)):
        sred=sred+C[j]
    global ball 
    ball = ball + sred/4
    print(str(name)+" имеет средний балл: "+str(sred/4))

def transpouse(mat): #Транспонирование массива
    matrix = []
    for i in range(len(mat[0])):
        matrix.append(list())
        for j in range(len(mat)):
            matrix[i].append(str(mat[j][i])) 
    return matrix

def step(C=[]): #Проверка стипендии
    name = C[0]
    strp = ""
    D=[]
    for o in range(1,len(C)):
        D.append(C[o])
    if min(D) == 2:
        strp = " - неуспевающий"                 
    elif min(D) == 4:
        strp = " - обычная стипендия"          
    else: strp = " - повышенная стипендия"           
    if strp == " - повышенная стипендия":
        pov.append(name+" "+strp)
    elif strp == " - обычная стипендия":
        ob.append(name+" "+strp)
    elif strp == " - неуспевающий":
        net.append(name+" "+strp)

while i <= n: #Ввод имен и оценок
    C=[]
    C.append(str(input(str(B[0])+" - ")))
    for j in range(1,len(B)): 
        C.append(int(input("Oценкa по дисциплине "+str(B[j])+" - ")))
    A.append(C)
    i = i+1

a = transpouse(A)
mlen = (max(map(len, col)) for col in zip(*a))  
s = f"{{:<{next(mlen)}}} {' '.join(f'{{:>{ml}}}' for ml in mlen)}" 
for d  in a:
    print(s.format(*d));

for i in range(1,len(A)): #Вывод средней оценки
    srball(A[i])
    step(A[i])
print("Средний балл группы: "+str(ball/n))

for i in range(len(pov)): #Выводим кто и какую стипендию получает
    print(pov[i],sep='\t')   
for i in range(len(net)):
    print(net[i],sep='\t')
for i in range(len(ob)):
    ob1 = ob1 + 1
print('Колличество студентов назначенных на обычную стипендию - ', ob1 )