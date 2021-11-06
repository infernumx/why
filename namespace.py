namespace = type(
    "_namespace",
    (),
    {
        "__rshift__": lambda self, x: exec("globals()[x] = self;") or self
        if isinstance(x, str)
        else [setattr(self, *attr) for attr in x] and self,
    },
)()

(
    namespace
    >> "std"
    >> {
        ("a", 1),
        (
            "print",
            lambda: print(
                "\n".join([f"std.{x} = {getattr(std, x)}" for x in vars(std)])
            )
        ),
    }
)

std.print()
