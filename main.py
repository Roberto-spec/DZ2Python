# Задание 1
upgrateConstant = 0.1
dni = 0
probegal = 0
try:
    skorost = int(input("Введите расстояние которое пробежал спортсмен в первый день: "))
    dolgen = int(input("Введите расстояние которое должен пробежать спортсмен: "))
except ValueError:
    print("Вы ввели не число")
if skorost >= dolgen:
    print("Ему один день нужно")
else:
    while True:
        dni += 1
        skorost *= upgrateConstant
        probegal += skorost
        if probegal >= dolgen:
            print("Расстояние в ", dolgen, " км сортсмен пробежит за ", dni, " дней")
            break;
        else:
            continue;

# Задание 2
try:
    naturalNumber = int(input("Введите целое число:"))
except ValueError:
    print("Вы ввели не число")
if naturalNumber <= 0:
    print("Вы ввели неверное число")
else:
    schetchik = 0
    current = 0
    stroka = ""
    while True:
        schetchik += 1
        current = schetchik * schetchik
        stroka += current + " "
        if (schetchik + 1) * (schetchik + 1) >= naturalNumber:
            print(stroka)
            break;
        else:
            continue;

    # Задание 3
    sum = 0
    sumKvadr = 0
    zeroConstant = 0
    try:
        while True:
            naturalNumber = int(input(">>>"))
            sum += naturalNumber
            sumKvadr += naturalNumber * naturalNumber
            if sum == zeroConstant:
                print(sumKvadr)
                break;
            else:
                continue;
    except ValueError:
        print("Вы ввели не число")

# Задание 4
try:
    skolkoChisel = int(input(">>>"))
    vihod = ""
    shitaem = 0
    currentNumber = 1
    currentNumberPovtor = 0
    while True:
        vihod += currentNumber + " "
        currentNumberPovtor += 1
        shitaem += 1
        if shitaem == skolkoChisel:
            print(vihod)
            break;
        if currentNumber == currentNumberPovtor:
            currentNumber += 1
            currentNumberPovtor = 0
        continue;
except ValueError:
    print("Вы ввели не число")

# Задание 5
# Метод 1
numbersStr = input("Введите числа через пробел:>_")
numberX = int(input("Введите число X:>_"))
repeats = ""
current = 0
index = 0
while current < len(numbersStr):
    if numbersStr[current] != ' ':
        if int(numbersStr[current]) == numberX:
            repeats += index + " "
            index += 1
    current += 1
if repeats == "":
    print("Нет совпадений")
else:
    print(repeats)
# Метод 2
numbersStr = input("Введите числа через пробел:>_")
numberX = int(input("Введите число X:>_"))
numbersStrList = numbersStr.split()
repeats = ""
index = 0
while True:
    try:
        index = numbersStrList.index(str(numberX), index)
        repeats += index + " "
    except ValueError:
        break
if repeats == "":
    print(repeats)
else:
    print("Нет совпадений")
# Задание 6
# Метод 1
strokaNumbers = ""
_ = ""
while True:
    _ = input("Введите число(или done если все):>_") + " "
    if _ == "done":
        break
    else:
        strokaNumbers += _ + " "
maxElement = int(strokaNumbers[0])
minElement = int(strokaNumbers[0])
current = 1
while current < len(strokaNumbers):
    if strokaNumbers[current] != " ":
        if int(strokaNumbers[current]) > maxElement:
            maxElement = int(strokaNumbers[current])
        elif int(strokaNumbers[current]) < minElement:
            minElement = int(strokaNumbers[current])
print("Максимальный: " + maxElement)
print("Минимальный: " + minElement)
# Метод 2
strokaNumbers = []
_ = ""
while True:
    _ = input("Введите число(или done если все):>_") + " "
    if _ == "done":
        break
    else:
        strokaNumbers.append(int(_))
print("Максимальный: " + max(strokaNumbers))
print("Минимальный: " + min(strokaNumbers))
# Задание 7
Stroka = "But soft what light through yonder window breaks "
Stroka += "It is the east and Juliet is the sun "
Stroka += "Arise fair sun and kill the envious moon "
Stroka += "Who is already sick and pale with grief"
Stroka = Stroka.split()
result = []
for _ in Stroka:
    try:
        result.index(_)
    except ValueError:
        result.append(_)
result.sort()
print(result)
# Задание 8
string = input('Введите слово: ')
stringRevers = reversed(string)
if "yes" == "".join(set(["yes" if i == j else "no" for i, j in zip(string, stringRevers)])):
    print("yes")
else:
    print("no")
# Задание 9
N = int(input("Введите размер таблицы:>_"))
STOP = N * N
stolb = 0
stroka = 0
strokaNow = True
i = 0
j = 0
mini = []
while i < N:
    mini.append(0)
matrica = []
while j < N:
    matrica.append(mini)

current = 1
maxIndex = 4
minIndex = 0
izmena=0
while True:
    if current == STOP:
        break
    elif strokaNow and stroka == minIndex:
        izmena+=1
        while stroka <= maxIndex:
            if current == STOP:
                break
            else:
                matrica[stolb][stroka] = current
                stroka += 1
                current += 1
        strokaNow = False
    elif strokaNow and stroka == maxIndex:
        izmena += 1
        while stroka >= minIndex:
            if current == STOP:
                break
            else:
                matrica[stolb][stroka] = current
                current += 1
                stroka -= 1
        strokaNow = False
    elif not strokaNow and stolb == minIndex:
        izmena += 1
        while stolb <= maxIndex:
            if current == STOP:
                break
            else:
                matrica[stolb][stroka] = current
                stolb += 1
                current += 1
            strokaNow = True
    elif not strokaNow and stolb == maxIndex:
        izmena += 1
        while stolb >= minIndex:
            if current == STOP:
                break
            else:
                matrica[stolb][stroka] = current
                stolb -= 1
                current += 1
            strokaNow = True
    if izmena== 4 :
        maxIndex -= 1
        minIndex += 1
        izmena=0
print(matrica)
