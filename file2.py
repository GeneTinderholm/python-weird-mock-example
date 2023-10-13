import file1

x = file1.do_thing()


def do_other_thing():
    print(x)  # prints 4 if not mocked, "hello world" if mocked
