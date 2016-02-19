"""
Converts a number of words to a predicate. Used by precise module.
"""
import re

_rexes = [
    ("range", 'range'),
    ("located in", 'in|are there|does have'),
    ("closest to", 'closest|nearest'),
    #("distance", 'from|between'),
    ("near", 'near'),
]

_compiled_rexes = [(a,re.compile( '.*(' + b + ')' )) for (a,b) in _rexes]

def convert(predicate):
    """
    Converts natural expression into a defined string
    >>> print(convert("are there in"))
    located in
    """
    for key, rex in _compiled_rexes :
        if rex.match(predicate) : return key
    return ""
