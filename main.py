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

#Задание 5

