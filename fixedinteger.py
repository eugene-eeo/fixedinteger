from integer import Integer


def rectify(val, width, signed):
    if signed:
        mask1 = (1 << (width - 1)) - 1
        mask2 = (1 << (width - 1))
        return (val & mask1) - (val & mask2)

    mask = (1 << width) - 1
    return val & mask


def fixed_int(name, width, signed, rectify=rectify):
    class _Int(Integer):
        __slots__ = ()
        def __new__(cls, v):
            return Integer.__new__(cls, rectify(v, width, signed))
    return type(
        name,
        (_Int,),
        {},
        )


u8  = fixed_int('u8',  8, False)
u32 = fixed_int('u32', 32, False)
u64 = fixed_int('u64', 64, False)

i8  = fixed_int('i8',  8, True)
i32 = fixed_int('i32', 32, True)
i64 = fixed_int('i64', 64, True)
