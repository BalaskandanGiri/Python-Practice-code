def func(noofa,tries):
    if tries < 0:
        return 0
    if tries == 0:
        return noofa
    return max(func(noofa+1,tries-1),noofa(noofa+clipboard,))
