

class C:
    def __new__(cls, *args, **kwargs):
        1

    def __init__(self):
        1


def new(*args, **kw):
    print("yo", args, kw)


C.__new__ = new
1