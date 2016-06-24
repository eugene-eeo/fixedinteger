fixedinteger
============

Lean and mean Python library implementing fixed-size integers::

    >>> from fixedinteger import u8
    >>> MAX_U8 = 2**8 - 1
    >>> u8(int('1'*9, base=2)) == MAX_U8
    True

Type names are inspired by Rust. Implements ``u{8,32,64}``
(unsigned integers), and ``i{8,32,64}`` signed variants. You
can also create your own fixed-size integer classes::

    >>> from fixedinteger import fixed_int
    >>> word = fixed_int('word', 8, signed=False)
    >>> word(128)
    128
