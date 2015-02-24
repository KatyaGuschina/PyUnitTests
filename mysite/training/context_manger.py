# coding: utf-8
import logging

my_logger = logging.getLogger('dima')


class ErrorLog:
        def __init__(self, obj):
            self.obj = obj

        def __enter__(self):
            my_logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            hdlr = logging.FileHandler('my_logger.txt')
            hdlr.setFormatter(formatter)
            my_logger.addHandler(hdlr)
            return self.obj

        def __exit__(self, exc_type, exc_val, exc_tb):
            my_logger.setLevel(logging.CRITICAL)


def main():

    my_logger.debug(u'DEBUG!!!')
    with ErrorLog(open('file.txt', 'w')) as afile:
        my_logger.debug(u'This is a debug message')
    with open('file.txt') as a:
        my_logger.debug(u'DEBUG!!!')

if __name__ == '__main__':
    main()