#!/usr/bin/env python3
# -*- coding: utf8 -*-


_align_parser = {
    "l": "ljust",
    "r": "rjust",
    "c": "center",
    "s": "center",
    }

def align(elts, length, **kwargs):
    """
    >>> align("content", 20, just="c")
    '      content       '
    >>> align("very_long_content", 12, just="l")
    'very_long_co'
    >>> align("very_long_content", 12, just="r")
    'long_content'
    >>> align("very_long_content", 12, just="c")
    'ry_long_cont'
    >>> align("very_long_content", 12, just="c", crop=False)
    'very_long_content'
    >>> align(["elt1", "elt2", "elt3"], 20, just="c", tip="|", sep=":", pad=1)
    ' | elt1:elt2:elt3 | '
    """
    just =  kwargs.setdefault("just",  "l")
    pad =   kwargs.setdefault("pad",   0)
    l_pad = kwargs.setdefault("l_pad", pad)
    r_pad = kwargs.setdefault("r_pad", pad)
    shift = kwargs.setdefault("shift", 0)
    sep =   kwargs.setdefault("sep",   " ")
    tip =   kwargs.setdefault("tip",   "")
    crop =  kwargs.setdefault("crop",  True)
    elts = elts if isinstance(elts, (tuple, list)) else [elts]
    elts = [str(elt) for elt in elts]
    length = length - l_pad - r_pad - len(tip)*2
    space, retained = 1, False
    if just == "s":
        n_chars = sum([len(elt) for elt in elts])
        space = max(1, (length - n_chars) // (len(elts) - 1))
        retained = (length - n_chars) % (len(elts) - 1)
    txt = (sep * space).join(elts)
    if retained:
        i = txt.rfind(" ")
        txt = txt[:i] + " " + txt[i:]
    txt = getattr(txt, _align_parser[just])(length)
    if shift > 0:
        txt = " "*shift + txt[:-shift]
    if shift < 0:
        txt = txt[-shift:] + " "*-shift
    if crop and len(txt) > length:
        n = len(txt) - length
        if just == "l":
            txt = txt[:length]
        if just == "r":
            txt = txt[n:]
        if just in ("c", "s"):
            n1 = n // 2
            n2 = n // 2 + n % 2
            txt = txt[n1:-n2]
    if tip:
        txt = tip + txt + tip
    if l_pad > 0:
        txt = " " * l_pad + txt
    if r_pad > 0:
        txt = txt + " " * r_pad
    return txt


def center(elts, length, **kwargs):
    """
    >>> center("content", 20)
    '      content       '
    >>> center("content", 20, shift=2)
    '        content     '
    >>> center("content", 20, shift=-2)
    '    content         '
    >>> center(["elt1", "elt2"], 20, sep=" "*4)
    '    elt1    elt2    '
    """
    kwargs.setdefault("just", "c")
    return align(elts, length, **kwargs)


def left(elts, length, **kwargs):
    """
    >>> left("content", 20, l_pad=2)
    '  content           '
    """
    kwargs.setdefault("just", "l")
    return align(elts, length, **kwargs)


def right(elts, length, **kwargs):
    """
    >>> right("content", 20, r_pad=2)
    '           content  '
    """
    kwargs.setdefault("just", "r")
    return align(elts, length, **kwargs)


def spread(elts, length, **kwargs):
    """
    >>> spread(["elt1", "elt2", "foo"], 20)
    'elt1    elt2     foo'
    >>> spread(["elt1", "elt2", "elt3"], 20, pad=1)
    ' elt1   elt2   elt3 '
    >>> spread(["long_content", "very_long_content"], 20)
    'content very_long_co'
    """
    kwargs.setdefault("just", "s")
    return align(elts, length, **kwargs)


def _setdefault_as_list(kwargs, varname, default, N):
    var = kwargs.setdefault(varname, [default]*N)
    if not isinstance(var, (tuple, list)):
        var = [var]*N
    n_var = len(var) 
    if n_var < N:
        var = var + [default] * (N - n_var)
    elif n_var > N:
        var = var[:N]
    return [default if v is None else v for v in var]


def multi_align(elts, length, **kwargs):
    """
    >>> multi_align(["elt1", "elt2", "elt3"], 30)
    'elt1      elt2      elt3      '
    >>> multi_align(["elt1", "elt2", "elt3"], 30, shifts=[2, -1, 1])
    '  elt1    lt2        elt3     '
    >>> multi_align(["elt1", "elt2", "elt3"], 30, justs="c", sep="|")
    '   elt1  |   elt2  |   elt3   '
    >>> multi_align(["right", "center", "left"], 30, justs=["r", "c", None])
    '    right   center  left      '
    >>> multi_align(["long_elt", "very_long_elt", "short"], 30, r_pads=3)
    'long_e    very_l    short     '
    >>> multi_align(["elt1", "elt2"], 20, sep="|", pads=1, justs=["r", "l"])
    '    elt1 | elt2     '
    """
    N = len(elts)
    sep = kwargs.setdefault("sep", " ")
    tip = kwargs.setdefault("tip", "")
    justs =  _setdefault_as_list(kwargs, "justs",  "l",     N)
    pads =   _setdefault_as_list(kwargs, "pads",   0,       N)
    l_pads = _setdefault_as_list(kwargs, "l_pads", pads[0], N)
    r_pads = _setdefault_as_list(kwargs, "r_pads", pads[0], N)
    shifts = _setdefault_as_list(kwargs, "shifts", 0,       N)
    actual_length = length - len(sep) * (N-1) -len(tip)*2
    default_length = actual_length // N
    default_remain = default_length + actual_length % N
    default_lengths = [default_length]*(N-1) + [default_remain]
    lengths = kwargs.setdefault("lengths", default_lengths)
    txt_elts = []
    for i, elt in enumerate(elts):
        i_args = (
            elt,
            lengths[i],
            )
        i_kwargs = {
            "just": justs[i],
            "pad":   pads[i],
            "l_pad": l_pads[i],
            "r_pad": r_pads[i],
            "shift": shifts[i],
            "crop":  True,
            }
        txt_elts.append(align(*i_args, **i_kwargs))
    return center(txt_elts, length, **kwargs)

def multi_center(elts, length, **kwargs):
    """
    >>> multi_center(["elt1", "elt2", "elt3"], 30)
    '   elt1      elt2      elt3   '
    """
    kwargs.setdefault("justs", "c")
    return multi_align(elts, length, **kwargs)

def multi_right(elts, length, **kwargs):
    """
    >>> multi_right(["elt1", "elt2", "elt3"], 30)
    '     elt1      elt2       elt3'
    """
    kwargs.setdefault("justs", "r")
    return multi_align(elts, length, **kwargs)

def multi_left(elts, length, **kwargs):
    """
    >>> multi_left(["elt1", "elt2", "elt3"], 30)
    'elt1      elt2      elt3      '
    """
    kwargs.setdefault("justs", "l")
    return multi_align(elts, length, **kwargs)


def multi_spread(elts, length, **kwargs):
    """
    >>> multi_spread([["A1", "A2", "A3"],["B1", "B2"]], 30)
    'A1    A2    A3 B1           B2'
    """
    kwargs.setdefault("justs", "s")
    return multi_align(elts, length, **kwargs)


def right_left(elt1, elt2, length, **kwargs):
    """
    >>> right_left("rjust", "ljust", 20)
    '    rjust ljust     '
    >>> right_left("elt1", "elt2", 20, sep="|", pads=1)
    '    elt1 | elt2     '
    >>> right_left("my_var", 1, 20, sep=": ", shift=3)
    '      my_var: 1     '
    """
    return multi_align([elt1, elt2], length, justs=["r","l"], **kwargs)

def table(elts, length, **kwargs):
    """
    >>> table(["elt1", "elt2", "elt3"], 34, justs=["l", "c", "r"])
    '| elt1     |   elt2   |     elt3 |'
    >>> table(["elt1", "elt2", "elt3"], 34)
    '| elt1     | elt2     | elt3     |'
    >>> table(["elt1", "elt2", "elt3"], 34, justs="c")
    '|   elt1   |   elt2   |   elt3   |'
    >>> table(["elt1", "elt2", "elt3"], 34, justs="r")
    '|     elt1 |     elt2 |     elt3 |'
    """
    kwargs.setdefault("sep", "|")
    kwargs.setdefault("tip", "|")
    kwargs.setdefault("justs", "l")
    kwargs.setdefault("pads", 1)
    return multi_align(elts, length, **kwargs)

def table_center(elts, length, **kwargs):
    """
    >>> table_center(["elt1", "elt2", "elt3"], 34)
    '|   elt1   |   elt2   |   elt3   |'
    """
    kwargs.setdefault("justs", "c")
    return table(elts, length, **kwargs)

def table_left(elts, length, **kwargs):
    """
    >>> table_left(["elt1", "elt2", "elt3"], 34)
    '| elt1     | elt2     | elt3     |'
    """
    kwargs.setdefault("justs", "l")
    return table(elts, length, **kwargs)

def table_right(elts, length, **kwargs):
    """
    >>> table_right(["elt1", "elt2", "elt3"], 34)
    '|     elt1 |     elt2 |     elt3 |'
    """
    kwargs.setdefault("justs", "r")
    return table(elts, length, **kwargs)

def table_spread(elts, length, **kwargs):
    """
    >>> table_spread([["A1", "A2", "A3"],["B1", "B2"]], 30)
    '| A1  A2   A3 | B1        B2 |'
    """
    kwargs.setdefault("justs", "s")
    return table(elts, length, **kwargs)


def multi_right_left(elts1, elts2, length, **kwargs):
    """
    >>> multi_right_left(["A", "B"], [1, 2], 20, seps=":")
    '   A:1       B:2    '
    >>> multi_right_left(["var1", "var2"], [1, 2], 28, sep="|", seps=": ")
    '  var1: 1    |  var2: 2     '
    >>> multi_right_left(["var1", "var2"], [1, 2], 28, seps=": ", shifts=2)
    '    var1: 1       var2: 2   '
    """
    N = min(len(elts1), len(elts2))
    seps = _setdefault_as_list(kwargs, "seps", " ", N)
    elts = []
    i_kwargs = kwargs.copy()
    i_kwargs.pop("sep", None)
    i_kwargs.pop("shifts", None)
    i_kwargs.pop("shift", None)
    for i, (elt1, elt2) in enumerate(zip(elts1, elts2)):
        tmp = right_left(elt1, elt2, length, sep=seps[i], **i_kwargs)
        elts.append(tmp)
    return multi_center(elts, length, **kwargs)




if __name__ == "__main__":

    import doctest
    doctest_result = doctest.testmod()
    print("\ndoctest >", doctest_result, "\n")


