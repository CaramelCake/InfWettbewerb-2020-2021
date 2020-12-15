list1 = open(" hier den absoluten file path eingeben ", "r+").readlines()
print("Numbers of figures:", list1[0])
print("Numbers of pieces:", list1[1])

list1 = [line[:-1].split() for line in list1][2:]
list2 = []

for line in list1:
    list2.append(list(map(int, line)))

print(list2)                                                        #List2 hat also 9 Listen
print("\n")

def permutate(piece):                                               #die Permutationen eines Teilchens erzeugen, ein Dreieck hat also 3 Drehungen.
    shape = []
    for i in range(len(piece)):
        shape.append(piece)
        piece = piece + [piece[0]]
        piece.pop(0)
    shape = tuple(shape)                                            #Tuple wird bevorzugt aufgrund der Ausführungzeit.
    return shape

def combine(list1, list_list2, pos1, pos2):
    some_list = []
    for j in list_list2:
        if list1[pos1] + j[pos2] == 0:
            some_list.append(j)
    return some_list

puzzles = list(permutate(i) for i in list2)                         #hiermit wird eine Liste von 9 Tuples erstellt, die jeweils 3 Permutationen erhalten.
#for puzzle in puzzles: print(puzzle)
#print("\n")

print(puzzles)
#print("\n")

'''
die Seiten eines Dreiecks können so positioniert werden:
                            [1]
          /\               ______
      [0]/  \[1]           \    /
        /____\          [0] \  /[2]
          [2]                \/

'''

def dreieck_puzzle(puzzles):
    count = 0
    for first_pieces in puzzles:                                #erste Tuple mit 3 Rotation.
        sub_list1 = [i for i in puzzles if i != first_pieces]   #eine Liste von den übrigen Teilchen.
        for first_piece in first_pieces:                        #jede Rotation wird mit jeder anderen Rotationen (von übrigen Teilchen) in sub_list angeordnet.
            for b in sub_list1:                                 
                second_pieces = combine(first_piece, b, 2, 1)   #diese Methode stellt eine Liste dar, die die passende Teilchen enthalten.
                sub_list2 = [i for i in sub_list1 if i != b]    #wenn ein Rotation/Teilchen passend ist, soll es von dem sub_list herausgenommen werden.
                for second_piece in second_pieces:
                    for c in sub_list2:
                        third_pieces = combine(second_piece, c, 0, 1)
                        sub_list3 = [i for i in sub_list2 if i != c]
                        for third_piece in third_pieces:
                            for d in sub_list3:
                                fourth_pieces = combine(second_piece, d, 2, 0)
                                sub_list4 = [i for i in sub_list3 if i != d]
                                for fourth_piece in fourth_pieces:
                                    for e in sub_list4:
                                        fifth_pieces = combine(third_piece, e, 2, 1)
                                        sub_list5 = [i for i in sub_list4 if i != e]
                                        for fifth_piece in fifth_pieces:
                                            for f in sub_list5:
                                                sixth_pieces = combine(fourth_piece, f, 2, 1)
                                                sub_list6 = [i for i in sub_list5 if i != f]
                                                for sixth_piece in sixth_pieces:
                                                    for g in sub_list6:
                                                        seventh_pieces = combine(fifth_piece, g, 0, 1)
                                                        sub_list7 = [i for i in sub_list6 if i != g]
                                                        for seventh_piece in seventh_pieces:
                                                            for h in sub_list7:
                                                                eigth_pieces = combine(sixth_piece, h, 2, 0)
                                                                sub_list8 = [i for i in sub_list7 if i != h]
                                                                for eighth_piece in eigth_pieces:
                                                                    for j in sub_list8:
                                                                        for last_piece in j:
                                                                            if last_piece[0] + fifth_piece[2] == 0 and last_piece[1] + sixth_piece[0] == 0:
                                                                                some_list = []
                                                                                some_list.append(first_piece)
                                                                                some_list.append(second_piece)
                                                                                some_list.append(third_piece)
                                                                                some_list.append(fourth_piece)
                                                                                some_list.append(fifth_piece)
                                                                                some_list.append(sixth_piece)
                                                                                some_list.append(seventh_piece)
                                                                                some_list.append(eighth_piece)
                                                                                some_list.append(last_piece)
                                                                                print(some_list)
                                                                                count+=1

    print("there are {} solution(s)".format(count))

'''
Die Teilchen(1st_piece - last_piece) sind in folgender Reihenfolge angeordnet:

            /\
           / 1\             
          /____\ 
         /\    /\
        /3 \ 2/ 4\
       /____\/____\
      /\    /\    /\
     /7 \ 5/ 9\ 6/ 8\
    /____\/____\/____\

'''

dreieck_puzzle(puzzles)

