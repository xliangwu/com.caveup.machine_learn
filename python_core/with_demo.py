class Simple:
    def __enter__(self):
        print("In __enter__ method")
        return "Simple"

    def __exit__(self, type, value, trace):
        print("In __exit__ method")
        print(type)
        print(value)
        print(trace)


def get_simple():
    return Simple()


with get_simple() as simple:
    print(simple)
