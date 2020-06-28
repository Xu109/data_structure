def jisuan(a):
    number = 0
    alpha = 0
    space = 0
    other = 0
    for i in a:
        if i.isdigit():
            number += 1
        elif i.isalpha():
            alpha += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    dict1 = {'number': number, 'alpha': alpha, 'space': space, 'other': other}
    return dict1


print(jisuan('as123 13 sada'))
