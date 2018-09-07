#!/usr/bin/env python3
# -*- coding: utf8 -*-

import math


class LineFormater(object):

    """
    LineFormater() -> new line formater with default values
    LineFormater(**kwargs) -> new line formater initialized with the name=value
    pairs in the keyword argument. For example: LineFormater(length=20)
    
    LF = LineFormater()
    LF.align(<elt>) --> formated string
    <elts> can be a single object with __str__ method or an iterable.
    
    Key word arguments (kwargs)
    ---------------------------
    NAME:    DESCRIPTION....................................(DEFAULT)
    length:  Positive integer...............................(80)
             Length of formated string.
    just:    Single character...............................("l")
             Justification type among:
               "l": left
               "c": center
               "r": right
               "s": spread (similar to justify)
    pad:     Positive integer...............................(0)
             Left and right paddings (ie extra spaces).
             Paddings reduce the content to keep length.
    l_pad:   Positive integer...............................(0)
             Left padding (ie extra spaces on left tip).
    r_pad:   Positive integer...............................(0)
             Right padding (ie extra spaces on right tip).
    shift:   Signed integer.................................(0)
             Shift of the content, rightward is positive.
    sep:     String.........................................(" ")
             Separator between elements if an iterator is
             given as input.
    tip:     String.........................................("")
             Characters at left and right tips.
             These reduce the content to keep length.
    crop:    Boolean........................................(True)
               True:  crop the content that doesn't match
                      the length
               False: non length matching content is
                      displayed on several lines

    Multi and table contexts display iterable's content in columns
    with total width matching length.

    Kwargs for multi and table contexts
    -----------------------------------
    lengths: Lengths of columns.............................(80)
    justs:   Justifications of columns .....................("l")
    pads:    Padding of columns ............................(0)
    l_pads:  Left padding.of columns........................(None)
    r_pads:  Right padding.of columns.......................(None)
    shifts:  Shifts of columns..............................(0)
    seps:    Separator inside columns.......................(" ")
    tips:    Tips of columns................................("")
    crops:   Crop or keep non matching contents.............(True)

    Separate values for each columns can be given using lists.
    None value can be used to keep default of a specific column.
    """

    _align_parser = {"l": "ljust", "r": "rjust", "c": "center", "s": "center"}

    _defaults = {
        "length": 80,
        "just": "l",
        "pad": 0,
        "l_pad": None,
        "r_pad": None,
        "shift": 0,
        "sep": " ",
        "tip": "",
        "crop": True,
        "lengths": None,
        "justs": "l",
        "pads": 0,
        "l_pads": None,
        "r_pads": None,
        "shifts": 0,
        "seps": " ",
        "tips": "",
        "crops": True,
    }

    def __init__(self, **kwargs):
        self.reset()
        self.set(**kwargs)

    def reset(self, *args):
        """
        With no arguments, reset all arguments to defaults, else, reset only
        given arguments (given as strings).
        """
        if len(args) == 0:
            for key, value in self._defaults.items():
                setattr(self, key, value)
        else:
            for arg in args:
                if arg in self._defaults:
                    setattr(self, arg, self._defaults[arg])

    def set(self, **kwargs):
        """Set values of the name=value pairs in the keyword argument."""
        for key, value in kwargs.items():
            if key in self._defaults:
                setattr(self, key, value)

    def align(self, elts, **kwargs):
        """
        Multi purpose formater.
        All other methods are interfaces of this one.
        
        >>> LF = LineFormater(length=20)
        >>> LF.align("content", l_pad=2)
        '  content           '
        >>> LF.align("content", just="r", r_pad=2)
        '           content  '
        >>> LF.align("content", just="c", shift=2)
        '        content     '
        >>> LF.align(["elt1", "elt2", "elt3"], just="s", pad=1)
        ' elt1   elt2   elt3 '
        >>> LF.align(["elt1", "elt2"], just="c", sep="*"*4)
        '    elt1****elt2    '
        >>> LF.align(["elt1", "elt2", "elt3"], just="c", tip="|", sep=":", pad=1)
        ' | elt1:elt2:elt3 | '
        >>> LF = LineFormater(length=12)
        >>> LF.align("very_long_content", just="l")
        'very_long_co'
        >>> LF.align("very_long_content", just="r")
        'long_content'
        >>> LF.align("very_long_content", just="c", shift=-3)
        'long_content'
        >>> LF = LineFormater(length=20, crop=False)
        >>> LF.align(["longcontent", "verylongcontent"], just="c")
        'longcontent verylong\\n      content       '
        >>> LF.align("longcontent verylongcontent", just="r")
        'longcontent verylong\\n             content'
        >>> elts = ["superverylongcontent", "verylongcontent", "longcontent", "short"]
        >>> LF.align(elts, just="s")
        'superverylongcontent\\n verylongcontent lon\\n  gcontent  short   '
        """
        length = kwargs.get("length", self.length)
        just = kwargs.get("just", self.just)
        pad = kwargs.get("pad", self.pad)
        l_pad = kwargs.get("l_pad", self.l_pad)
        r_pad = kwargs.get("r_pad", self.r_pad)
        l_pad = pad if l_pad is None else l_pad
        r_pad = pad if r_pad is None else r_pad
        shift = kwargs.get("shift", self.shift)
        sep = kwargs.get("sep", self.sep)
        tip = kwargs.get("tip", self.tip)
        crop = kwargs.get("crop", self.crop)
        elts = elts if isinstance(elts, (tuple, list)) else [elts]
        elts = [str(elt) for elt in elts]
        length = length - l_pad - r_pad - len(tip) * 2
        space, retained = 1, False
        if just == "s" and len(elts) > 1:
            n_chars = sum([len(elt) for elt in elts])
            space = max(1, (length - n_chars) // (len(elts) - 1))
            retained = (length - n_chars) % (len(elts) - 1)
        txt = (sep * space).join(elts)
        if retained:
            i = txt.rfind(" ")
            txt = txt[:i] + " " + txt[i:]
        txt = getattr(txt, self._align_parser[just])(length)
        if shift > 0:
            txt = " " * shift + txt[:-shift]
        if shift < 0:
            txt = txt[-shift:] + " " * -shift
        if len(txt) > length:
            if crop:
                n = len(txt) - length
                n1, n2 = n // 2, n // 2 + n % 2
                left, right = (just == "l"), (just == "r")
                txt = txt[:length] if left else (txt[n:] if right else txt[n1:-n2])
            else:
                n_parts = len(txt) // length + 1
                indexes = (
                    (i * length, min(len(txt), (i + 1) * length))
                    for i in range(n_parts)
                )
                return "\n".join(
                    [self.align(txt[i1:i2], **kwargs) for i1, i2 in indexes]
                )
        if tip:
            txt = tip + txt + tip
        if l_pad > 0:
            txt = " " * l_pad + txt
        if r_pad > 0:
            txt = txt + " " * r_pad
        return txt

    def center(self, elts, **kwargs):
        """
        Center justification.
        
        >>> LF = LineFormater(length=20)
        >>> LF.center("content")
        '      content       '
        """
        kwargs.setdefault("just", "c")
        return self.align(elts, **kwargs)

    def left(self, elts, **kwargs):
        """
        Left justification.
        
        >>> LF = LineFormater(length=20)
        >>> LF.left("content")
        'content             '
        """
        kwargs.setdefault("just", "l")
        return self.align(elts, **kwargs)

    def right(self, elts, **kwargs):
        """
        Right justification.
        
        >>> LF = LineFormater(length=20)
        >>> LF.right("content")
        '             content'
        """
        kwargs.setdefault("just", "r")
        return self.align(elts, **kwargs)

    def spread(self, elts, **kwargs):
        """
        Spread justification.
        
        >>> LF = LineFormater(length=20)
        >>> LF.spread(["elt1", "elt2", "foo"])
        'elt1    elt2     foo'
        """
        kwargs.setdefault("just", "s")
        return self.align(elts, **kwargs)

    def _setdefault_as_list(self, kwargs, varname, default, N):
        if not isinstance(default, (tuple, list)):
            default = [default] * N
        if len(default) < N:
            message = "default for {} has not same dimensions as given elements"
            raise ValueError(message.format(varname))
        var = kwargs.setdefault(varname, default)
        if not isinstance(var, (tuple, list)):
            var = [var] * N
        n_var = len(var)
        if n_var < N:
            var = var + default[n_var:N]
        elif n_var > N:
            var = var[:N]
        var = [default[i] if v is None else v for i, v in enumerate(var)]
        kwargs[varname] = var
        return var

    def multi_align(self, elts, **kwargs):
        """
        Multi purpose formater on columns.
        All other multi_ or table_ methods are interfaces of this one.
        
        >>> LF = LineFormater(length=30)
        >>> LF.multi_align(["elt1", "elt2", "elt3"])
        'elt1      elt2      elt3      '
        >>> LF.multi_align(["elt1", "elt2", "elt3"], shifts=[2, -1, 1])
        '  elt1    lt2        elt3     '
        >>> LF.multi_align(["elt1", "elt2", "elt3"], justs="c", sep="|")
        '   elt1  |   elt2  |   elt3   '
        >>> LF.multi_align(["right", "center", "left"], justs=["r", "c", None])
        '    right   center  left      '
        >>> LF.multi_align(["long_elt", "very_long_elt", "short"], r_pads=3)
        'long_e    very_l    short     '
        >>> LF.set(pads=1, sep="|")
        >>> LF.multi_align(["elt1", "elt2"], justs=["r", "l"])
        '         elt1 | elt2          '
        >>> LF.multi_align(["elt1", "elt2"], justs="c", tip="|")
        '|     elt1    |     elt2     |'
        >>> LF.reset("pads", "sep")
        >>> LF.multi_align(["elt1", "elt2", "elt3"])
        'elt1      elt2      elt3      '
        >>> elts = ["short", "long_content", "very_very_long_content"]
        >>> LF.multi_align(elts, crops=[False, True, False])
        'short     long_cont very_very_\\n                    long_conte\\n                    nt        '
        >>> LF.multi_align(elts, lengths=[5, 12])
        'short long_content very_very_ '
        """
        N = len(elts)
        sep = kwargs.setdefault("sep", self.sep)
        tip = kwargs.setdefault("tip", self.tip)
        length = kwargs.setdefault("length", self.length)
        actual_length = length - len(sep) * (N - 1) - len(tip) * 2
        default_length = actual_length // N
        default_remain = default_length + actual_length % N
        default_lengths = [default_length] * (N - 1) + [default_remain]
        self._setdefault_as_list(kwargs, "lengths", default_lengths, N)
        self._setdefault_as_list(kwargs, "justs", self.justs, N)
        pads = self._setdefault_as_list(kwargs, "pads", self.pads, N)
        l_pads = self._setdefault_as_list(kwargs, "l_pads", self.l_pads, N)
        r_pads = self._setdefault_as_list(kwargs, "r_pads", self.r_pads, N)
        None_N = [None] * N
        kwargs["l_pads"] = pads if l_pads == None_N else l_pads
        kwargs["r_pads"] = pads if r_pads == None_N else r_pads
        self._setdefault_as_list(kwargs, "shifts", self.shifts, N)
        self._setdefault_as_list(kwargs, "seps", self.seps, N)
        crops = self._setdefault_as_list(kwargs, "crops", self.crops, N)
        _formater = kwargs.setdefault("_formater", self.align)
        formated_elts = []
        for i, elt in enumerate(elts):
            i_kwargs = {
                key[:-1]: value[i] for (key, value) in kwargs.items() if key[-1] == "s"
            }
            formated_elts.append(_formater(elt, **i_kwargs))
        if not all(crops):
            n_chars = len(formated_elts[0])
            n_lines = max([elt.count("\n") + 1 for elt in formated_elts])
            elts = [elt.split("\n") for elt in formated_elts]
            elts = [elt + [" " * n_chars] * (n_lines - len(elt)) for elt in elts]
            return "\n".join(self.center(line, **kwargs) for line in zip(*elts))
        return self.align(formated_elts, **kwargs)

    multi = multi_align

    def multi_center(self, elts, **kwargs):
        """
        Center justified columns.
        
        >>> LF = LineFormater(length=30)
        >>> LF.multi_center(["elt1", "elt2", "elt3"])
        '   elt1      elt2      elt3   '
        """
        kwargs.setdefault("justs", "c")
        return self.multi_align(elts, **kwargs)

    def multi_right(self, elts, **kwargs):
        """
        Right justified columns.
        
        >>> LF = LineFormater(length=30)
        >>> LF.multi_right(["elt1", "elt2", "elt3"])
        '     elt1      elt2       elt3'
        """
        kwargs.setdefault("justs", "r")
        return self.multi_align(elts, **kwargs)

    def multi_left(self, elts, **kwargs):
        """
        Left justified columns.
        
        >>> LF = LineFormater(length=30)
        >>> LF.multi_left(["elt1", "elt2", "elt3"])
        'elt1      elt2      elt3      '
        """
        kwargs.setdefault("justs", "l")
        return self.multi_align(elts, **kwargs)

    def multi_spread(self, elts, **kwargs):
        """
        Spread justified columns.
        
        >>> LF = LineFormater(length=30, pads=1)
        >>> LF.multi_spread([["A1", "A2", "A3"],["B1", "B2"]])
        ' A1   A2   A3   B1         B2 '
        """
        kwargs.setdefault("justs", "s")
        return self.multi_align(elts, **kwargs)

    def _right_left(self, elts, **kwargs):
        """
        >>> LF = LineFormater(length=20)
        >>> LF._right_left(["rjust", "ljust"])
        '    rjust ljust     '
        >>> LF._right_left(["elt1", "elt2"], sep="|", pads=1)
        '    elt1 | elt2     '
        >>> LF._right_left(["my_var", 1], sep=": ", shift=3)
        '      my_var: 1     '
        """
        kwargs.setdefault("justs", ["r", "l"])
        return self.multi_align(elts, **kwargs)

    def table(self, elts, **kwargs):
        """
        Multi purpose table formater.
        All other table _methods are interfaces of this one.
        
        >>> LF = LineFormater(length=34)
        >>> LF.table(["elt1", "elt2", "elt3"], justs=["l", "c", "r"])
        '| elt1     |   elt2   |     elt3 |'
        """
        kwargs.setdefault("sep", "|")
        kwargs.setdefault("tip", "|")
        kwargs.setdefault("justs", "l")
        kwargs.setdefault("pads", 1)
        return self.multi_align(elts, **kwargs)

    def table_center(self, elts, **kwargs):
        """
        Center justified tables.
        
        >>> LF = LineFormater(length=34)
        >>> LF.table_center(["elt1", "elt2", "elt3"])
        '|   elt1   |   elt2   |   elt3   |'
        """
        kwargs.setdefault("justs", "c")
        return self.table(elts, **kwargs)

    def table_left(self, elts, **kwargs):
        """
        Left justified tables.
        
        >>> LF = LineFormater(length=34)
        >>> LF.table_left(["elt1", "elt2", "elt3"])
        '| elt1     | elt2     | elt3     |'
        """
        kwargs.setdefault("justs", "l")
        return self.table(elts, **kwargs)

    def table_right(self, elts, **kwargs):
        """
        Right justified tables.
        
        >>> LF = LineFormater(length=34)
        >>> LF.table_right(["elt1", "elt2", "elt3"])
        '|     elt1 |     elt2 |     elt3 |'
        """
        kwargs.setdefault("justs", "r")
        return self.table(elts, **kwargs)

    def table_spread(self, elts, **kwargs):
        """
        Spread justified tables.
        
        >>> LF = LineFormater(length=30)
        >>> LF.table_spread([["A1", "A2", "A3"],["B1", "B2"]])
        '| A1  A2   A3 | B1        B2 |'
        """
        kwargs.setdefault("justs", "s")
        return self.table(elts, **kwargs)

    def dictionary(self, key, value, **kwargs):
        """
        Double alignment for key/value pairs
        Key is right justified, value is left justified. Separator is ': '
        
        >>> LF = LineFormater(length=20)
        >>> LF.dictionary("key", "value")
        '      key: value    '
        """
        kwargs.setdefault("sep", ": ")
        return self._right_left([key, value], **kwargs)

    def multi_dictionary(self, keys, values, **kwargs):
        """
        Double alignment for colums. 
        
        >>> LF = LineFormater(length=30)
        >>> LF.multi_dictionary(["key1", "key2"], ["value1", "value2"])
        '  key1: value1   key2: value2 '
        >>> LF.sep = "|"
        >>> LF.multi_dictionary(["var1", "var2"], [1, 2], shifts=2)
        '    var1: 1   |    var2: 2    '
        """
        kwargs.setdefault("_formater", self._right_left)
        kwargs.setdefault("seps", ": ")
        return self.multi_align(list(zip(keys, values)), **kwargs)

    def table_dictionary(self, keys, values, **kwargs):
        """
        Double alignment for tables.
        
        >>> LF = LineFormater(length=42)
        >>> LF.table_dictionary(["key1", "key2"], ["value1", "value2"], shifts=-2)
        '|   key1: value1    |    key2: value2    |'
        """
        kwargs.setdefault("_formater", self._right_left)
        kwargs.setdefault("seps", ": ")
        return self.table(list(zip(keys, values)), **kwargs)


if __name__ == "__main__":

    import doctest

    doctest_result = doctest.testmod()
    print("\ndoctest >", doctest_result, "\n")
