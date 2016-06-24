import unittest
from fixedinteger import rectify, u8, u32, u64, i8, i32, i64, fixed_int


btoi = lambda x: int(x, base=2)


class TestRectify(unittest.TestCase):
    def test_overflow_full(self):
        MAX = btoi('1' * 8)
        assert rectify(btoi('1' * 10), 8, False) == MAX
        assert rectify(btoi('1' * 8),  8, False) == MAX

    def test_underflow_unsigned(self):
        for n in range(0, 2**8 - 1):
            assert rectify(n, 8, False) == n

    def test_underflow_signed(self):
        for n in range(0, 2**7 - 1):
            assert rectify(n, 8, True)  == n
            assert rectify(-n, 8, True) == -n


class TestU8(unittest.TestCase):
    integer_class = u8
    signed = False
    width = 8

    @property
    def maximum(self):
        return btoi('1' * (self.width - self.signed))

    @property
    def base(self):
        return 2 ** self.width

    def correct(self, N):
        return rectify(N, self.width, self.signed)

    def test_bounded(self):
        for N in range(0, 100):
            assert self.integer_class(N) == self.correct(N)
            assert self.integer_class(self.maximum + N) == \
                    self.correct(self.maximum + N)

    def test_mutable(self):
        u = self.integer_class(10)
        g = self.correct(10)

        u += 1
        g = self.correct(g + 1)
        assert u == g

        u >>= 1
        g = self.correct(g >> 1)
        assert u == g

        u <<= 2
        g = self.correct(g << 2)
        assert u == g

        u -= 1
        g = self.correct(g - 1)
        assert u == g


class TestU32(TestU8):
    integer_class = u32
    width = 32


class TestU64(TestU8):
    integer_class = u64
    width = 64


class TestI8(TestU8):
    integer_class = i8
    signed = True


class TestI32(TestI8):
    integer_class = i32
    width = 32


class TestI64(TestI8):
    integer_class = i64
    width = 64


class TestCustomSignedFixedInt(TestI8):
    integer_class = fixed_int('', 2, True)
    signed = True
    width = 2


class TestCustomUnsignedFixedInt(TestI8):
    integer_class = fixed_int('', 2, False)
    signed = False
    width = 2


if __name__ == '__main__':
    unittest.main()
