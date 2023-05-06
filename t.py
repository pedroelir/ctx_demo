from ctx_demo import ctx, ctx_man, Some


def localscope():
    some = Some()
    print(f" Using some object {id(some)}")


print("With @contxtmanager")
with ctx_man() as label:
    some = Some()
    print(f"Middle got object {label=}")

print("\nTraditional Contex Manager")
with ctx() as label:
    some = Some()
    print(f"Middle got object {label=}")

print("\nWith @contxtmanager using localscope fucntion")
with ctx_man() as label:
    localscope()
    print(f"Middle got object {label=}")

print("\nTraditional Contex Manager using local scope fucntion")
with ctx() as label:
    localscope()
    print(f"Middle got object {label=}")
