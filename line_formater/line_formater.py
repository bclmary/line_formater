#!/usr/bin/env python3
# -*- coding: utf8 -*-


class LineFormater(object):

    """
    LineFormater() -> new line formater with default values
    LineFormater(**kwargs) -> new line formater initialized with the name=value
    pairs in the keyword argument.  For example:  LineFormater(length=20)
    
    LF = LineFormater()
    LF.align(<elt>) --> formated string
    <elts> can be a single object with __str__ method or an iterable.
    
    kwargs
    ------
    NAME:   DESCRIPTION..................................(DEFAULT)
    length: length of formated string....................(80)
    just:   justification in ["l", "s", "r", "s"]........("l")
    pad:    left and right padding, ie extra spaces......(0)
    l_pad:  left padding.................................(None)
    r_pad:  right padding................................(None)
    shift:  shift of the content, rightward is positive..(0)
    sep:    separator between elements...................(" ")
    tip:    characters at left and right tips............("")
    crop:   crop the ouput if it doesn't match length....(True)

    kwargs for multi and table contexts
    -----------------------------------
    lengths: lengths of columns...........(80)
    justs:   justifications of columns ...("l")
    pads:    padding of columns ..........(0)
    l_pads:  left padding.of columns......(None)
    r_pads:  right padding.of columns.....(None)
    shifts:  shifts of columns............(0)
    seps:    separator inside columns.....(" ")
    tips:    tips of columns..............("")

    Separate values for each columns can be given using lists.
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
        >>> LF.align(["longcontent", "verylongcontent"], just="s")
        'gcontent verylongcon'
        >>> LF.align(["longcontent", "verylongcontent"], just="s", crop=False)
        'longcontent verylongcontent'
        >>> LF = LineFormater(length=12)
        >>> LF.align("very_long_content", just="l")
        'very_long_co'
        >>> LF.align("very_long_content", just="r")
        'long_content'
        >>> LF.align("very_long_content", just="c", shift=-3)
        'long_content'
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
        if just == "s":
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
        _formater = kwargs.setdefault("_formater", self.align)
        formated_elts = []
        for i, elt in enumerate(elts):
            i_kwargs = {
                key[:-1]: value[i] for (key, value) in kwargs.items() if key[-1] == "s"
            }
            formated_elts.append(_formater(elt, **i_kwargs))
        return self.center(formated_elts, **kwargs)

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
