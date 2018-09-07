LineFormater
############


Description
===========

A class containing a collection of text line formater methods.
Each method get the same signature (except ``dictionary`` and derived).

**Mandatory inputs**:  any object with ``__str__`` method or list of objects.

**Output**: string of fixed length.


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

Example::

  input = ["elt1", "elt2", "elt3"]
  length = 18
  pad = 2
  sep = "*"
  output = "  elt1*elt2*elt3  "



Multi context
----------------

In multi context, each element of given contents are formated in as many content zones.
The previously described arguments are still available, and affect the main content zone (and not the contents).
See ``length``, ``pad``, ``l_pad``, ``r_pad``, ``shift`` and ``sep``.
All these arguments can be applied separately on each content zones using there plural forms.
See ``lengths``, ``pads``, ``l_pads``, ``r_pads``, ``shifts`` and ``seps``.
If a single value is given to these plural form, it will be applied to all the content zones.
If one wants to set separate values for each plural form, a list must be given.
Also, if one want to keep the default for some content zones, a None value must be filled at corresponding positions.


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
   │elt1 elt2         │  > left (l)
   │                  │
   │    elt1 elt2     │  > center (c)
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

:left:
    left alignment

:center:
    center alignment

:right:
    right alignment

:spread:
    spread alignment


Multi context
----------------

The content MUST be an iterable.

:muti:
   multi-purpose formater in multiples zones

:multi_left: 
    left alignment in multiples zones

:multi_center: 
    center alignment in multiples zones

:multi_right:
    right alignment in multiples zones

:multi_spread: 
    spread alignments in mutliples zones


Table context
-------------

Same as multi-context.

:table:
   multi-purpose formater in table

:table_left: 
    left alignment in table

:table_center: 
    center alignment in table

:table_right:
    right alignment in table

:table_spread: 
    spread alignments in table


Extra formaters
---------------

Two positoinal arguments (key, value) are awaited.

:dictionary:
    double alignment for key/value : key is right justified, value is left justified. Separator is ':'

:multi_dictionary: 
    double alignments for multiple zones. Key and value positional arguments MUST be lists.

:table_dictionary: 
    double alignments for table.



Positional arguments
====================

:content:
    | A single object with __str__ method or an iterable (two elements for special methods ``dictionary`` and derived).
    | The elements to format.


Key word arguments
==================

Single forms
------------

:length:  
    | Positive integer.
    | Length of formated string.
    | Default is 80.

:just:
    | Single character.
    | Justification type among:
    |   "l": left
    |   "c": center
    |   "r": right
    |   "s": spread (similar to justify)
    | Default is "l".

:pad:
    | Positive integer.
    | Left and right paddings (ie extra spaces).
    | Paddings reduce the content to keep length.
    | Default is "l".

:l_pad:
    | Positive integer.
    | Left padding (ie extra spaces on left tip).
    | Default is 0.

:r_pad:
    | Positive integer.
    | Right padding (ie extra spaces on right tip).
    | Default is 0.

:shift:
    | Signed integer.
    | Shift of the content, rightward is positive.
    | Default is 0.

:sep:
    | String.
    | Separator between elements if an iterator is given as input.
    | Default is " ".

:tip:
    | String.
    | Characters at left and right tips.
    | These reduce the content to keep length.
    | Default is "".

:crop:
    | Boolean.
    |   True:  crop the content that doesn't match the length.
    |   False: non length matching content is displayed on several lines.
    | Default is True.



Plural forms
------------

:lengths:
    | Positive integer or list of positive integers.
    | Lengths of each content zones.
    | Default: None (auto-computed).

:justs:
    | Single character or list of single character.
    | Flags for alignment types of each content zones.
    | Default: "l" for ``multi_align`` and ``table`` methods.

:l_pads:
    | Positive integer or list of positive integers.
    | Left and right padding of each content zones.
    | Paddings reduce the contents to keep lengths.
    | Default: 0.

:l_pads:
    | Positive integer or list of positive integers.
    | Left padding of each content zones.
    | Default: 0.

:r_pads:
    | Positive integer or list of positive integers.
    | Right padding of each content zones.
    | Default: 0.

:shifts:
    | Signed integer or list of signed integers.
    | Shift of each content zones.
    | Default: 0.

:seps:
    | String or list of Strings.
    | Separator inserted between content elements of each content zones (if contents are iterables).
    | Default: " ".

:tips:
    | String or list of Strings.
    | Characters inserted at the tips of each content zones.
    | These reduce the content to keep length.
    | Default: "".

:crops:
    | Boolean or list of Booleans.
    |   True:  crop the contents that doesn't match the lengths.
    |   False: non length matching contents are displayed on several lines.
    | Default is True.


If list are used with plural forms, ``None`` value can be used to keep default of a specific column.


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






