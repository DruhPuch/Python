o = 1
while True:

    print('Podaj pierwszą liczbę')
    try:
            x = int(input())
    except:
            x = ValueError
            print('To nie jest liczba')
            x = int(input())
    try:
            print('Podaj drugą liczbę')
            y = int(input())
    except:
            y = ValueError
            print('To nie jest liczba')
            y = int(input())

    print('1. Dodawanie')
    print('2. Odejmowanie')
    print('3. Mnożenie')
    print('4. Dzielenie')
    print('Wybierz rodzaj działania po przez wybór liczby')

    try:
        z = int(input())
    except:
        z = ValueError
        print('To nie jest poprawnie wybrana opcja')
        z = int(input())

    if z == 1:
            print(x+y)
    elif z == 2:
            print(x-y)
    elif z == 3:
            print(x*y)
    elif z == 4:
            if y == 0:
                print('zmień liczbę z 0 przy dzieleniu')
                while True:
                    try:
                        print('Podaj drugą liczbę')
                        y = int(input())
                    except:
                        y = ValueError
                        print('To nie jest liczba')
                        y = int(input())
                    if y != 0:
                        break
                print(x/y)
            elif y != 0:
                print(x/y)

    print('Jeżeli chcesz kontynuować napisz "1", jeżeli nie, wpisz dowolną liczbę')
    try:
            o = int(input())
    except:
            o = ValueError
            print('To nie jest liczba')
            o = int(input())

    if o != 1:
        break