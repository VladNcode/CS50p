def main():
    name = input("What is your name? ")
    a = input("a? ")
    b = input("b? ")
    print(div(a, b))
    # hello(name)


def hello(name="default"):
    print(f"Hello {name}")


def div(a, b):
    return int(a) / int(b)


main()
