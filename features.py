import re
from porter import PorterStemmer
p = PorterStemmer()

def lcase(text):
    return text.lower()

def prefixes(text):
    return [text[:3], text[:4], text[:5]]

def suffixes(text):
    return [text[-3:], text[-4:], text[-5:]]

def stem(text):
    if text.isalpha():
        return p.stem(text.lower(), 0, len(text)-1)
    return text

def is_pair_of_digits(text):
    if re.match("^[0-9]{2}$", text):
        return True
    return False

def is_four_digits(text):
    if re.match("^[0-9]{4}$", text):
        return True
    return False

def letters_and_digits(text):
    if re.match("^[0-9a-zA-Z]+$", text):
        return True
    return False

def digits_and_hyphens(text):
    if re.match("^[0-9\-]+$", text):
        return True
    return False

def digits_and_slashes(text):
    if re.match("^[0-9/]+$", text):
        return True
    return False

def digits_and_colons(text):
    if re.match("^[0-9,]+$", text):
        return True
    return False

def digits_and_dots(text):
    if re.match("^[0-9.]+$", text):
        return True
    return False

def ucase_and_dots(text):
    if re.match("^[A-Z.]+$", text):
        return True
    return False

def initial_ucase(text):
    if re.match("^[A-Z][a-z]*$", text):
        return True
    return False

def only_ucase(text):
    if re.match("^[A-Z]+$", text):
        return True
    return False

def only_lcase(text):
    if re.match("^[a-z]+$", text):
        return True
    return False

def only_digits(text):
    if re.match("^[0-9]+$", text):
        return True
    return False

def only_non_alnum(text):
    if re.match("^[^a-zA-Z0-9]+$", text):
        return True
    return False

def contains_ucase(text):
    if re.match("[A-Z]", text):
        return True
    return False

def contains_lcase(text):
    if re.match("[a-z]", text):
        return True
    return False

def contains_digits(text):
    if re.match("[0-9]", text):
        return True
    return False

def contains_non_alnum(text):
    if re.match("[^a-zA-Z0-9]", text):
        return True
    return False

def date_regex(text):
    if re.match("^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$", text):
        return True
    return False

def pattern(text):
    text = re.sub("[A-Z]", "A", text)
    text = re.sub("[a-z]", "a", text)
    text = re.sub("[0-9]", "0", text)
    return text

def collapsed_pattern(text):
    text = re.sub("[A-Z]+", "A", text)
    text = re.sub("[a-z]+", "a", text)
    text = re.sub("[0-9]+", "0", text)
    return text

def features(text):
    return [text, lcase(text), prefixes(text), suffixes(text), stem(text), is_pair_of_digits(text), is_four_digits(text), letters_and_digits(text), digits_and_hyphens(text), digits_and_slashes(text), digits_and_colons(text), digits_and_dots(text), ucase_and_dots(text), initial_ucase(text), only_ucase(text), only_lcase(text), only_digits(text), only_non_alnum(text), contains_ucase(text), contains_lcase(text), contains_digits(text), contains_non_alnum(text), date_regex(text), pattern(text), collapsed_pattern(text)]

def print_features(text):
    feats = features(text)
    i = 2
    ret = "f[01]=" + text
    for f in feats[1:]:
        if type(f) == str:
            ret += ("\tf[%02d]=%s" % (i, f))
        elif type(f) == bool and f == True:
            ret += ("\tf[%02d]" % i)
        i += 1
    return ret
