line_formaters
##############


Description
===========

A collection of text line formaters.

**Mandatory inputs**:  string or list of strings, length

**Output**: string of given length


Simpe context
-------------

The string is formated in a conceptual zone of given ``length``.
On both sides, there is paddings (see ``pad`` argument), which are extra spacing, reducing the content zone.
Left and right paddings can be individually specified using ``l_pad`` and ``r_pad`` arguments respectively.
The content can be shifted of a signed value (see ``shift`` aguement) inside the content-zone.
If the content is a list of elements, one can specify the separator using ``sep`` arguement.


Scheme explaining common key word arguments in *simple context*::

 │<┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄length┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄>│
 │         ┆                          ┆         │
 │<┄l_pad┄>┆       content-zone       ┆<┄r_pad┄>│
 │         ┆                          ┆         │
 │<┄┄pad┄┄>┆    <┄┄ - shift + ┄┄>     ┆<┄┄pad┄┄>│


Multiple context
----------------

In multi context, each element of given contents are formated in as many content zones.
The previously described arguments are still available, and affect the contents zones (and not the contents).
See ``length``, ``pad``, ``l_pad``, ``r_pad``, ``shift`` and ``sep``.
All these arguments can be applied separately on each content zones using the plural form of these arguements.
See ``lengths``, ``pads``, ``l_pads``, ``r_pads``, ``shifts`` and ``seps``.
If a single value is given to these plural form, it will be applied to all the content zones.
If one wants to set separate values for each plural form, a list must be given.
Also, if one want to keep the default for some content zones, a None value must be filled at corresponding position. 


Scheme explaining common key word arguments in *multiple context*::

 ┃<┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄length┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄>┃
 ┃     │                                                                           │     ┃
 ┃     │                             main content zone                             │     ┃
 ┃     │                                                                           │     ┃
 ┃     │<┄┄┄┄┄┄┄┄┄┄┄┄lengths[0]┄┄┄┄┄┄┄┄┄┄┄>│   │<┄┄┄┄┄┄┄┄┄┄┄lengths[-1]┄┄┄┄┄┄┄┄┄┄┄>│     ┃
 ┃     │         ┆               ┆         │   │         ┆               ┆         │     ┃
 ┃ pad │ pads[0] ┆  contents[0]  ┆ pads[0] │sep│pads[-1] ┆ contents[-1]  ┆pads[-1] │ pad ┃
 ┃     │         ┆               ┆         │   │         ┆               ┆         │     ┃
 ┃     │         ┆ <┄shifts[0]┄> ┆         │   │         ┆ <┄shifts[0]┄> ┆         │     ┃
 ┃     │         ┆               ┆         │   │         ┆               ┆         │     ┃
 ┃     │                                                                           │     ┃
 ┃     │      <┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ - shift + ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄>      │     ┃


Alignments
----------

Types of alignment::

   │<┄┄content-zone┄┄>│
   │                  │
   │    elt1 elt2     │  > center (c)
   │                  │
   │elt1 elt2         │  > left (l)
   │                  │
   │         elt1 elt2│  > right (r)
   │                  │
   │elt1   elt3   elt2│  > spread (s)


Formaters
=========

Simple context
--------------

:align:
    multi-purpose simple formater

:center:
    center alignment

:left:
    left alignment

:right:
    right alignment

:spread:
    spread alignment


Multiple context
----------------

:muti_align:
   multi-purpose formater in multiples zones

:multi_center: 
    center alignment in multiples zones

:multi_left: 
    left alignment in multiples zones

:multi_right:
    right alignment in multiples zones

:right_left: 
    fixed alingments - right and left - on two zones

:multi_right_left:
    multiple context of right_left alignment


Positional arguments
====================

:content:
    | element or list of elements (int, float, string, ...)
    | the elements to format

:length:
    | positive integer
    | total length of the returned string

Key word arguments
==================

single forms
------------

:pad:
    | positive integer
    | left and right paddings
    | paddings of the main-content-zone for multis
    | default: 0

:l_pad:
    | positive integer
    | left padding (gets priority over ``pad``)
    | left padding of the main-content-zone for multis
    | default: 0

:r_pad:
    | positive integer 
    | right padding (gets priority over ``pad``)
    | right padding of the main-content-zone for multis
    | default: 0

:shift:
    | signed integer
    | shift of the content-zone (positive direction is rightward)
    | shift of the main-content-zone for multis
    | default: 0

:sep:
    | string
    | separator inserted between content elements
    | separator inserted between content zones for multis
    | default: " "


plural forms
------------

:lengths:
    | positive integer or list of positive integers
    | lengths of each content zones
    | default: None (auto-computed)

:l_pads:
    | positive integer or list of positive integers
    | left and right padding of each content zones
    | default: 0

:l_pads:
    | positive integer or list of positive integers
    | left padding of each content zones
    | default: 0

:r_pads:
    | positive integer or list of positive integers
    | right padding of each content zones
    | default: 0

:shifts:
    | signed integer or list of signed integers
    | shift of each content zones
    | default: 0

:seps:
    | string
    | separator inserted between content elements of each content zones
    | default: " "


Examples
========

    >>> center("content", 20)
    '      content       '

    >>> center("content", 20, shift=+5)
    '           content  '

    >>> left("content", 20, l_pad=2)
    '  content           '

    >>> right("content", 20, r_pad=2)
    '           content  '

    >>> spread(["foo", "bar", "foobar"], 20, pad=1)
    ' foo   bar   foobar '

    >>> multi_center(["elt1", "elt2", "elt3"], 30)
    '   elt1      elt2      elt3   '

    >>> right_left("my_var", 1, 20, sep=": ")
    '   my_var: 1        '

    >>> multi_right_left(["var1", "var2"], [1, 2], 28, sep="|", seps=": ")
    '  var1: 1    |  var2: 2     '






