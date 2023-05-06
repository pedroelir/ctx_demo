from contextlib import contextmanager


class Some:
    def __init__(self) -> None:
        print(f"Object some {id(self)} got instantiated")

    def __del__(self):
        print(f"Object some {id(self)} got deleted")


class ctx:
    def __enter__(self):
        print("First inside Traditional Context Manager")
        label = "Object from Traditional Context Manager"
        return label

    def __exit__(self, type, value, tb):
        print("Exit from Traditional Context Manager")


@contextmanager
def ctx_man():
    print("First inside @contextmanager")
    try:
        yield "Object from @contextmanager"
    finally:
        print("Exit from @contextmanager")


# def localscope():
#     some = Some()
#     print(f" Using some object {id(some)}")


# print("With @contxtmanager")
# with ctx_man() as label:
#     some = Some()
#     print(f"Middle got object {label=}")

# print("\nTraditional Contex Manager")
# with ctx() as label:
#     some = Some()
#     print(f"Middle got object {label=}")

# print("\nWith @contxtmanager")
# with ctx_man() as label:
#     some = Some()
#     print(f"Middle got object {label=}")
