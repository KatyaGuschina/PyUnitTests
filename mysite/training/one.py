#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse

import sys

import logging

logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG,
                    filename=u'file.txt')

# Сообщение отладочное
logging.debug(u'This is a debug message')
# Сообщение информационное
logging.info(u'This is an info message')
# Сообщение предупреждение
logging.warning(u'This is a warning')
# Сообщение ошибки
logging.error(u'This is an error message')
# Сообщение критическое
logging.critical(u'FATAL!!!')


def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default='мир')
    parser.add_argument('-s', type=int)

    return parser


def main():
    parser = createparser()
    namespace = parser.parse_args(sys.argv[1:])
    square = namespace.s ** 2
    print ("Привет, {}! Ответ - {}".format (namespace.name,square))


if __name__ == "__main__":
    main()
