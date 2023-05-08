def foo(a: int, b=None):
    if b is None:
        b = []
    b.append(a)
    print(b) # noqa: T201, E261


foo(1)
foo(2)
foo(3, list())
