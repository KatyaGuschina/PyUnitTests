#!/usr/bin/python
# coding: UTF-8

import argparse
import logging
import sys
import texttable as tt

MAX_RESULT = 10
FRAMES = 10
my_logger = logging.getLogger('my')
my_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr = logging.FileHandler('my_logger.txt')
hdlr.setFormatter(formatter)
my_logger.addHandler(hdlr)


class Game:

    def __init__(self, string):
        self.string = string
        self.frames = list(self.parse())

    def get_frame_result(self):
        fn = 0
        for index, frame in enumerate(self.frames[:-1]):
            frame.next_frame = self.frames[index+1]
        for frame in self.frames[:FRAMES]:
            fn = fn + frame.get_total_score()
            my_logger.debug(u'Общее количество набранных очков - {}'.format(fn))
            yield fn

    def parse(q):
        res = filter(lambda x: x.strip(' '), q)
        line = iter(res)
        i = 0
        while line:
            i = i +1
            first = line.next()
            if first == 'X':
                if i > 9:
                    f = line.next()
                    try:
                        last = line.next()
                        if not f == 'X':
                            raise Exception('Ошибка ввода, так как 11 бросок не является strike, 12й бросок невозможен')
                        yield 'X{}{}'.format(f, last)
                    except StopIteration:
                        yield 'X{}'.format(f)
                else:
                    yield 'X', ''
                    continue
            if line:
                second = line.next()
            else:
                second = ''
            if first:
                first = str(first)
            if second:
                second = str(second)
            if first == '/':
                raise Exception('Ошибка ввода, первый удар не может быть spare!')
            if second == 'X':
                raise Exception('Ошибка ввода, второй удар не может быть strike!')
            yield first, second

    def get_final_result(self):
        game = Game(ex)
        gen = list(game.parse())
        list_frames = [x.string for x in gen]
        try:
            ten = list_frames.pop(10)
        except IndexError:
            ten = ''
        try:
            eleven = list_frames.pop(10)
        except IndexError:
            eleven = ''
        try:
            list_frames.pop(10)
            return u'Слишком длинное значени строки'
        except IndexError:
            pass
        try:
            list_frames[9] = str(list_frames[9]) + str(ten) + str(eleven)
        except IndexError:
            return u'Слишком короткое значение строки'
        t = tt.Texttable()
        header = ['1', '2', '3', '4',  '5', '6', '7', '8', '9', '10']
        t.header(header)
        row = list_frames
        t.add_row(row)
        row = list(game.get_frame_result())
        t.add_row(row)
        t.set_chars(['-', '|', '+', '='])
        s = t.draw()

        return s


class Throw:

    def __init__(self, frame, knocked_off):
        self.frame = frame
        self.knocked_off = knocked_off

    @property
    def next_throw(self):
        if self == self.frame.first_throw and not self.frame.strike:
            return self.frame.second_throw
        else:
            return self.frame.next_frame.first_throw


class Frame:

    def __init__(self, string, first_throw, second_throw=0):
        self.string = string
        self.first_throw = Throw(self, first_throw)
        self.second_throw = Throw(self, second_throw)
        self.next_frame = None

    @property
    def strike(self):
        return self.first_throw.knocked_off == MAX_RESULT

    @property
    def spare(self):
        return not self.strike and self.first_throw.knocked_off + self.second_throw.knocked_off == MAX_RESULT

    def get_total_score(self):
        score = self.first_throw.knocked_off
        score += self.second_throw.knocked_off
        if self.strike:
            score += self.next_frame.first_throw.knocked_off
            score += self.next_frame.first_throw.next_throw.knocked_off

        if self.spare:
            score += self.next_frame.first_throw.knocked_off
        my_logger.debug(u'Общий счет броска {}'.format(score))
        return score

# TODO: добавить отдельный класс для парсинга строк и кинуть туда эту функцию

    def get_frames(self):
        res = filter(lambda x: x.strip(' '), self.string)
        line = iter(res)
        i = 0
        while line:
            i = i +1
            first = line.next()
            if first == 'X':
                if i > 9:
                    f = line.next()
                    if not f == 'X':
                        raise Exception(u'Ошибка ввода')
                    try:
                        last = line.next()
                        if not last == 'X':
                            raise Exception(u'Ошибка ввода')
                        yield ('X{}{}').format(f, last)
                    except StopIteration:
                        yield ('X{}'.format(f))
                else:
                    yield ('X')
                    continue
            if line:
                second = line.next()
            else:
                second = first
            if first:
                first = str(first)
            if second:
                second = str(second)
            if first == '/':
                raise Exception(u'Ошибка ввода')
            if second == 'X':
                raise Exception(u'Ошибка ввода')
            yield first, second


ex = "8/9-X X 6/4/X 8-X XXX"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', default=ex)
    namespace = parser.parse_args(sys.argv[1:])

    game = Game(namespace.r)
    result = game.get_final_result()

    print result

if __name__ == '__main__':
        main()
