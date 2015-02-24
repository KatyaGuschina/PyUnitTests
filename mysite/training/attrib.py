# coding - utf-8


class AccessCounter(object):

    def __init__(self, val):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)


def main():
    t = AccessCounter(23)
    print t.__dict__
    setattr(t, 'value', 32)
    print t.__dict__
    delattr(t, 'value')
    print t.__dict__


if __name__ == '__main__':
    main()