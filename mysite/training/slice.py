#coding - utf-8


class MySlice(object):

    def __getitem__(self, key):
        return list(range(key.start, key.stop, key.step))

def main():

    my = MySlice()

    print my[2:10:1]

if __name__ == "__main__":
    main()