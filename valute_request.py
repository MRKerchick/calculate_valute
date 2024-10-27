import requests
import xml.etree.ElementTree as ET
slovar = {}
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
def reload_valute():
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for valute in root.findall('Valute'):
            char_code = valute.find('CharCode').text
            value = valute.find('Value').text
            slovar[char_code] = float(value.replace(',','.'))
        slovar['RUB'] = 1
        print('Валюты обновлены!')
    else:
        print(f'Сайт чёт плохо себя чувствует, код ошибки: {response.status_code}')
def valute_convert():
    val_in = str(input('Введите валюту которую хотите перевести: ')).upper()
    val_kol_vo = int(input('Введите кол-во валюты которую хотите перевести: '))
    val_out = str(input('Введите валюту в которую хотите перевести: ')).upper()
    if val_in in slovar and val_out in slovar:
        print(f'1 {val_in} = {(slovar[val_in] / slovar[val_out])*val_kol_vo} {val_out}')
    else: print('У тя валюта не правильно введена, \nиди английский поучи, умник тут, \nвалюты он тут считать')





