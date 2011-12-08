import re

def lcase(text):
    return text.lower()

def prefixes(text):
    return [text[:3], text[:4], text[:5]]

def suffixed(text):
    return [text[-3:], text[-4:], text[-5:]]

def stem(text):
# To be implemented
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

def digites_and_colons(text):
    if re.match("^[0-9,]+$", text):
        return True
    return False

def digites_and_dots(text):
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

