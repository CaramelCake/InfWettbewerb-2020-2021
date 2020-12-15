import itertools

before0 = [{1:3, 0:12}, {0:6, 3:3, 4:1}, {4:7, 6:12, 5:5}, {5:11, 3:9, 2:6}, {2:12, 1:9}]
after0 = [{'f':12, 'e':1}, {'f':6, 'a':1}, {'a':7, 'g':6, 'b':5}, {'b':11, 'c':6}, {'c':12, 'd':11}, {'d':5, 'g':12, 'e':7}]

before1 = [{1:12, 2:2}, {1:6, 8:4, 7:2, 0:12}, {0:6, 5:4}, {5:10, 7:8, 6:6, 4:4}, {4:10, 3:8}, {3:2, 6:12, 8:10, 2:8}]
after1 = [{'a':2, 'f':6}, {'a':8, 'g':6, 'b':4}, {'b':10, 'c':6}, {'c':12, 'h':10, 'd':8}, {'d':2, 'e':10}, {'f':12, 'i':2, 'e':4}, {'g':12, 'h':4, 'i':8}]

before2 = [{1:8, 2:6, 3:3}, {3:9, 4:3}, {4:9, 5:11, 6:4, 8:6}, {6:10, 7:8}, {7:2, 8:12, 11:3, 10:7, 9:5}, {11:3, 12:9}, {12:3, 2:12, 13:5, 14:7}]
after2 = [{'a':10, 'b':6, 'c':3}, {'c':9, 'd':3}, {'d':9, 'e':11, 'h':6, 'f':8}, {'h':12, 'g':10, 'k':9, 'j':7, 'i':5}, {'f':2, 'g':4}, {'k':3, 'l':9}, {'l':3, 'b':12, 'm':7, 'n':5}]

before3 = [{1:11, 2:1, 3:2, 4:4, 5:5, 6:7, 7:8, 8:10}, {1:5, 9:1}, {9:7, 10:5}, {10:11, 2:7}, {3:8, 11:4}, {11:10, 12:8}, {4:10, 12:2}, {5:11, 13:7, 13:1, 14:11}, {14:5, 6:1}, {7:2, 15:10}, {15:4, 16:2}, {16:8, 8:4}]
after3 = [{'a':12, 'b':11, 'c':2, 'd':3, 'e':4, 'f':5, 'h':6, 'j':7, 'e':8, 'm':9, 'n':10, 'o':12}, {'a':6, 'p':12}, {'f':11, 'g':5}, {'h':12, 'i':6}, {'j':1, 'k':7}]

before4 = [{0:3, 1:12}, {1:6, 2:3}, {2:9, 7:6, 3:3}, {3:9, 6:6, 4:3}, {4:9, 9:6}, {9:12, 8:9, 12:6, 13:3}, {8:3, 6:12, 5:9, 10:6}, {5:3, 7:12, 0:9}, {13:9, 14:6}, {14:12, 15:9}, {15:3, 12:12, 11:9}, {11:3, 10:12}]
after4 = [{'a':3, 'b':6}, {'a':9, 'd':6}, {'j':6, 'k':3}, {'k':9, 'l':6}, {'b':12, 'c':3}, {'d':12, 'e':3, 'f':6, 'c':9}, {'j':12, 'i':3, 'k':6, 'e':9}, {'i':9, 'l':12, 'm':3, 'p':6}, {'m':9, 'n':6}, {'f':12, 'g':3}, {'g':9, 'h':12}, {'p':12, 'o':3}, {'o':9, 'n':12}]

before5 = [{1:10, 2:12, 7:4, 8:6}, {7:10, 6:8, 4:4, 3:2}, {8:12, 6:2, 5:6, 0:8}]
after5 = [{'b':12, 'c':2}, {'b':6, 'i':4, 'h':2, 'a':12}, {'a':6, 'f':4}, {'f':10, 'h':8, 'g':6, 'e':4}, {'e':10, 'd':8}, {'d':2, 'g':12, 'i':10, 'c':8}]

def take_lines(figure): #gibt eine Liste der Streichhölzer zurück, bei after0 ist die z.B ['g', 'd', 'a', 'c', 'f', 'e', 'b'].
    lines = list(set([i for point in figure for i in [*point]]))
    return lines

def remove_lines(figure, lines, num_of_removed_lines):#gibt eine Liste der figures zurück, wenn manche Streichhölzer weggezogen worden sind.
    big_list = []
    for j in itertools.combinations(lines, num_of_removed_lines):
        list1 = []
        for i in figure:
            dict1 = {k:i[k] for k in i if k not in j}    
            sorted_dict1 = {k:v for k, v in sorted(dict1.items(), key = lambda item:item[1])}
            list1.append(sorted_dict1)

        #print(list1)

        big_list.append(list1)
    return big_list #len(big_list) kann berechnet werden, indem man den Multinomialkoeffizient verwendet.

def compare_dict(dict1, dict2): #die Methode vergleicht die Values von verschiedenen Dictionaries.
    if list(dict1.values()) == list(dict2.values()):
        return True
    else:
        return False

def compare_list_dict(list1, list2): #diese vergleicht 2 Listen von Dictionaries(also Figure), anhand der oben erwähnten Methode. 
    matched_list = []
    for i in list1:
        matched = [i for j in list2 if compare_dict(i, j)]
        matched_list.append(matched)
    if [] in matched_list:
        return False
    else:
        return True                   # hiermit wird festgestellt, ob 2 Figuren kongruent sind.

def compare_figures(figure_before, figure_after, i):
    x = remove_lines(figure_before, take_lines(figure_before), i)
    y = remove_lines(figure_after, take_lines(figure_after), i)
    matched1 = [a for a in x for b in y if compare_list_dict(a, b)] # hier sind jeweils die kongruente Figuren, einmal in numerierten Schreibweise
    matched2 = [b for a in x for b in y if compare_list_dict(a, b)] # und einmal in buchstabierten Schreibweise

    if matched1: # sobald diese Liste nicht leer ist, wird aus jeder Liste jeweils das erste Element zurückgegeben.
        return matched1[0], matched2[0]
    else:
        print('Impossible')
        return None
    
def move(figures, figure_before, figure_after):
    lines1 = take_lines(figures[0])
    moved_lines1 = [item for item in take_lines(figure_before) if item not in lines1]

    lines2 = take_lines(figures[1])
    moved_lines2 = [item for item in take_lines(figure_after) if item not in lines2]
    return moved_lines1, moved_lines2 # die lines, die zu umlegen sind

num = int(input('Num of removed lines: '))
z = compare_figures(before0, after0, num)
#print(z)

if z:
    w = move(z, before0, after0)
    # print(w)
    print("We have to move {} lines from {} to {}".format(num, w[0], w[1]))
