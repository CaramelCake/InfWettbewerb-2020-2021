list1 = open(" hier den absoluten file path eingeben ", "r+").readlines()

list1 = [line[:-1].split() for line in list1][1:]
kids_wishes = []

for line in list1:
    kids_wishes.append(list(map(int, line)))

kids_wishes = [i for i in enumerate(kids_wishes, 1)]
kids_wishes = [tuple([i[0]] + i[1]) for i in kids_wishes]

gifts = [i[0] for i in kids_wishes]
# print(kids_wishes)

def nth_wishes(wishes, pos):
    return list(wishes[i][pos] for i in range(len(wishes)))

one_wanted = [x for x in nth_wishes(kids_wishes, 1) if nth_wishes(kids_wishes, 1).count(x) == 1]
more_wanted = list(set(x for x in nth_wishes(kids_wishes, 1) if nth_wishes(kids_wishes, 1).count(x) != 1))
# print(one_wanted+more_wanted)

def update(wish, wanted1, wanted2):
    update_wish = []
    update_wish.append(wish[0])
    update_wish.append(wish[1])
    for i in wish[2:]:
        if i in wanted1:
            i = 0
        update_wish.append(i)

    if update_wish[3] in wanted2:
        update_wish[3] = 0

    return tuple(update_wish)

def give_gifts(wishes, func, pos, kids_with_gift):
    update = []
    given = []

    for i in wishes:
        if func(i) and i[pos] not in given:
            kids_with_gift.append(tuple([i[0]]+[i[pos]]))
            given.append(i[pos])
        else:
            update.append(i)
    
    return update, kids_with_gift


kids_with_gifts = []

def wichteln(kids_with_gifts):
    x = give_gifts(kids_wishes, lambda i: i[1] in one_wanted, 1, kids_with_gifts) #die Wünsche in one_wanted werden vergeben

    y = []

    for i in x[0]:
        y.append(update(i, nth_wishes(kids_wishes, 1), nth_wishes(x[0], 2)))        #die Wünsche werden realisiert, so dass kein erster Wunsch am 2. oder 3. Postition vorliegt

    z = give_gifts(y, lambda i: i[1] == sum(i[1:]), 1, kids_with_gifts)             
    w = give_gifts(z[0], lambda i: i[2] == sum(i[2:]) and i[2] != 0, 2, kids_with_gifts)
    v = give_gifts(w[0], lambda i: i[3] != 0, 3, kids_with_gifts)

    left_kids = [i for i in gifts if i not in [j[0] for j in v[1]]]
    left_gifts = [i for i in gifts if i not in [j[1] for j in v[1]]]

    for i in range(len(left_gifts)):
        kids_with_gifts.append((left_kids[i], left_gifts[i]))

    return kids_with_gifts

x = wichteln(kids_with_gifts)
for i in x:
    print(i)