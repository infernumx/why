#!/usr/bin/env python3
import random

function = type(
    "function",
    (),
    {
        "__init__": lambda self, fn: {
            setattr(self, "fn", fn),
            setattr(self, "args", []),
            setattr(self, "kwargs", {}),
        }
        and None,
        "__invert__": lambda self: print(
            f"{self.fn.__name__}({', '.join(list(map(str, self.args)) + [f'{key}={value!r}' for key, value in self.kwargs.items()])})"
        ),
        "__mod__": lambda self, arg: self.args.append(arg) or self,
        "__floordiv__": lambda self, kwarg: self.kwargs.update(kwarg) or self,
        "__pos__": lambda self: self.fn(*self.args, **self.kwargs),
    },
)

stringstream = type(
    "stringstream",
    (),
    {
        "__init__": lambda self: setattr(self, "string", ""),
        "__lshift__": lambda self, s: {
            setattr(self, "string", getattr(self, "string") + s)
        }
        and self,
        "__repr__": lambda self: self.string,
    },
)

std = type(
    "_std",
    (),
    {
        "__getitem__": lambda self, key: self,
        "__matmul__": lambda self, fn: self.__class__.__dict__[fn],
        "print": function(print),
        "rand": function(lambda: random.randint(1, 100)),
    },
)()


+(std[::] @ "print" % +(std[::] @ "rand") % +(std[::] @ "rand") % +(std[::] @ "rand") % (stringstream() << "Hello" << ", " << "world!") // {"sep": "\n"})
