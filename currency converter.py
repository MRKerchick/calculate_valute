import valute_request



def main():
    a = int(input('\n\nДоступные действие с валютами:\n1. Обновить базу с валютами\n2. Подсчитать валюту\n3. Выход\n').replace(' ',''))
    if a == 1: valute_request.reload_valute()
    elif a == 2: valute_request.valute_convert()
    elif a == 3: exit()
    else: 
        print('\nВведите только цифру!\n')
while True:
    main()








