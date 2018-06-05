string = input()
def hasnumbers():
    for i in string:
        if i.isdigit():
            return True
    return False
def haslowercase():
    for i in string:
        if i.islower():
            return True
    return False
def hasuppercase():
    for i in string:
        if i.isupper():
            return True
    return False
def hasspecialchar():
    spl = "!@#$%^&*()-+"
    for i in string:
        if i in spl:
            return True
    return False
def main():
    if len(string) < 6:
        return False
    if not hasnumbers():
        return False
    if not haslowercase():
        return False
    if not hasuppercase():
        return False
    if not hasspecialchar():
        return False
    return True
if main():
    print("Passed")
else:
    print("Failed")
