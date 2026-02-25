def shift_list_elements(ls, shift):
    n = len(ls)
    out = [0 for i in range(n)]
    for i in range(n):
       out[(i + shift) % n] = ls[i]
    return out