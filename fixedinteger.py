from integer import Integer


def rectify(width, signed):
    if signed:
        mask1 = (1 << (width - 1)) - 1
        mask2 = (1 << (width - 1))
        return lambda v: (v & mask1) - (v & mask2)

    mask = (1 << width) - 1
    return lambda v: v & mask


def fixed_int(name, width, signed):
    fix = rectify(width, signed)

    class _Int(Integer):
        __slots__ = ()
        def __new__(cls, v):
            return Integer.__new__(cls, fix(v))
    return type(name, (_Int,), {})


u8  = fixed_int('u8',  8, False)
u32 = fixed_int('u32', 32, False)
u64 = fixed_int('u64', 64, False)

i8  = fixed_int('i8',  8, True)
i32 = fixed_int('i32', 32, True)
i64 = fixed_int('i64', 64, True)
