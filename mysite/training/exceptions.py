# coding: utf-8


def main():
    d = dict.fromkeys(range(1, 11), True)
    try:
        s[11]
    except KeyError as err:
        print 'Некорректное значение ключа {}'.format(err)
    except Exception as err:
        print 'Получить ключ словаря не удалось - %s' %(err)
        pass

    try:
         12 / 0
    except ZeroDivisionError:
        print "Деление на ноль"
    finally:
        print "executing finally clause"

    try:
        something = d[10]
    except KeyError as err:
        print 'Некорректное значение ключа {}'.format(err)
    else:
        print something

if __name__ == '__main__':
    main()