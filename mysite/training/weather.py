# coding: utf-8


def main():
    from lxml import etree
    from pip._vendor import requests
    req = requests.get('http://informer.gismeteo.ru/xml/29634_1.xml')
    # print requests.get('https://api.github.com/user', auth=('still65@yandex.ru', 'vfuyfnbv772'))
    if req.ok:
        root = etree.fromstring(req.content)
        for df in root.xpath('//FORECAST'):
            print u'''
                    Погода на сегодня {}/{}/{} - {}:00 часов. Облачность: {},
                    Атмосферное давление: {}-{}, Температура воздуха:({}, {}), Скорость ветра: {}-{} мс.,
                    'Влажность воздуха: {}-{}, Ощущается как: {}, {} '''\
                .format(df.get('day'), df.get('month'), df.get('year'), df.get('hour'), df.xpath('PHENOMENA/@cloudiness')[0],
                        df.find('PRESSURE').get('min'), df.find('PRESSURE').get('max'), df.find('TEMPERATURE').get('min'),
                        df.find('TEMPERATURE').get('max'), df.find('WIND').get('min'), df.find('WIND').get('max'),
                        df.find('RELWET').get('min'), df.find('RELWET').get('max'), df.find('HEAT').get('min'),
                        df.find('HEAT').get('max'))

if __name__ == "__main__":
    main()