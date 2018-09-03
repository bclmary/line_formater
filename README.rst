LineFormater
############


Description
===========

A class containing a collection of text line formater methods.
Each methods get the same signature (except ``dictionary`` and derived).

**Mandatory inputs**:  string or list of strings

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
 ┃    tip                                                                         tip    ┃
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



Table context
-------------

Table-context is very similar to multi-context. Main differences are only some arguments with differents default values : ``pads`` is set to 1 and ``tip`` and ``sep`` are set to '|' (pipe).

Scheme explaining effect of default arguments in *table context*::

 tip               sep                tip
  ┃ ┆             ┆ ┃ ┆              ┆ ┃
  ┃1┆ content[0]  ┆1┃1┆ content[-1]  ┆1┃
  ┃ ┆             ┆ ┃ ┆              ┆ ┃



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


Methods
=======

Simple context
--------------

The content (single positional argment) can be of any type.

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

The content MUST be an iterable.

:muti:
   multi-purpose formater in multiples zones

:multi_center: 
    center alignment in multiples zones

:multi_left: 
    left alignment in multiples zones

:multi_right:
    right alignment in multiples zones

:multi_spread: 
    spread alignments in mutliples zones


Table context
-------------

Same as multi-context.

:table:
   multi-purpose formater in table

:table_center: 
    center alignment in table

:table_left: 
    left alignment in table

:table_right:
    right alignment in table

:table_spread: 
    spread alignments in table


Extra formaters
---------------

Two positoinal arguments -- the contents -- are awaited.

:dictionary:
    double alignment for key/value : key is right justified, value is left justified. Separator is ':'

:multi_dictionary: 
    double alignments for multiple zones

:table_dictionary: 
    double alignments for table



Positional arguments
====================

:content:
    | element or list of elements (two elements for special methods ``dictionary`` and derived).
    | int, float, string, list, ...
    | the elements to format

Key word arguments
==================

single forms
------------

:length:
    | positive integer
    | total length of the returned string

:just:
    | single character
    | flag for alignment types (see alignments section)
    | default: "l" for ``align`` method

:pad:
    | positive integer
    | left and right paddings
    | default: 0

:l_pad:
    | positive integer
    | left padding (gets priority over ``pad``)
    | default: 0

:r_pad:
    | positive integer 
    | right padding (gets priority over ``pad``)
    | default: 0

:shift:
    | signed integer
    | shift of the content-zone (positive direction is rightward)
    | default: 0

:sep:
    | string
    | separator inserted between content elements
    | default: " "

:tip:
    | string
    | element inserted at the tips of the formated contents
    | default: ""


plural forms
------------

:lengths:
    | positive integer or list of positive integers
    | lengths of each content zones
    | default: None (auto-computed)

:justs:
    | single character or list of single character
    | flags for alignment types of each content zones
    | default: "l" for ``multi_align`` and ``table`` methods

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

:tips:
    | string
    | element inserted at the tips of each content zones
    | default: ""



Examples
========

    >>> LF = LineFormater(length=20)
    >>> center("content")
    '      content       '

    >>> LF.center("content", shift=+5)
    '           content  '

    >>> LF.left("content", l_pad=2)
    '  content           '

    >>> LF.right("content", r_pad=2)
    '           content  '

    >>> LF.spread(["foo", "bar", "foobar"], pad=1)
    ' foo   bar   foobar '

    >>> LF.multi_center(["elt1", "elt2", "elt3"], length=30)
    '   elt1      elt2      elt3   '

    >>> LF.dictionary("my_var", 1)
    '   my_var: 1        '

    >>> LF.table_dictionary(["var1", "var2"], [1, 2], length=28)
    '| var1: 1    |  var2: 2    |'






