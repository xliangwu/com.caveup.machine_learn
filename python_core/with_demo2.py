class Simple:
    def __enter__(self):
        print("In __enter__ method")
        return self

    def __exit__(self, type, value, trace):
        print(type)
        print(value)
        print(trace)
        # execute this line even it has exception
        print("In __exit__ method")

    def do_sth(self):
        bar = 1 / 0
        return bar + 10


def get_simple():
    return Simple()


with get_simple() as simple:
    simple.do_sth()
