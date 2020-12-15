import itertools
from random import *

list1 = open(" hier den absoluten file path eingeben ", "r+").readlines()
players_starke = [int(line.strip()) for line in list1][1:]          #eine Liste von Spielstärken.

print('There are {} players\n'.format(len(players_starke)))
print(players_starke)

plays_dict = {k:v for k, v in enumerate(players_starke)}            #numerierter Spieler mit seiner Stärke.
print(plays_dict)

starkster = max(plays_dict, key = plays_dict.get)                   #die größte Stärke.

players = list(plays_dict.keys())
shuffle(players)                                                    #eine zufällig gemischte Liste von Spielern. Diese wird für die Turniervarianten KO und KO_5 verwendet.

def showdown(dic):                                                  
    r = random()                                                    
    if r < list(dic.values())[0]/sum(dic.values()):
        return list(dic.keys())[0]
    else:
        return list(dic.keys())[1]

    #diese Funktion nimmt eine Dictionary von 2 Spielern und gibt den Sieger nach Tobis Regeln wieder.

def liga(dict_of_plays):
    winners = []

    liga_matches = [{j: dict_of_plays[j] for j in i} for i in itertools.combinations(dict_of_plays, 2)] #jeder Spieler spielt einmal gegen anderen Spieler. Hier gibt es N x (N-1)/2 Matche.
    #print(liga_matches)
    for i in liga_matches:
        winner_round = showdown(i)
        winners.append(winner_round)

    win_times = {i:winners.count(i) for i in winners}#es wird gezählt, wie oft ein Spieler gewonnen hat.
    #print(win_times)

    liga_winner = min([k for k, v in win_times.items() if v == max(win_times.values())])#gibt den Spieler, der am Öftersten gewinnt, wieder. Der mit der kleinsten Spielernummer wird gewählt beim Gleichstand.
    #print(liga_winner)
    return liga_winner

def ko(players):
    ko_matches = []
    winners = []

    if len(players) < 2:
        return players[0]

    else:
        for i in range(0, len(players), 2):
            ko_matches.append({key:plays_dict[key] for key in players[i:i+2]})#die gemischte Liste von Spielern (Zeile 16) wird in 2er Gruppen geteilt. Hier gibt es nur N/2 Matche.
        #print(ko_matches)

        for i in ko_matches:
            winner_round = showdown(i)
            winners.append(winner_round)#gibt die Gewinner bei jeder Runde wieder.
        #print(winners)
        return ko(winners)#die Funktion wird rekursive wiederholt, bis nur ein Gewinner übrig bleibt.

def ko_5(players):
    ko_5_matches = []
    winners = []
    one_round = []

    if len(players) < 2:
        return players[0]

    else:
        for i in range(0, len(players), 2):
            ko_5_matches.append({key:plays_dict[key] for key in players[i:i+2]})#es gibt hier auch N/2 Matche.
        #print(ko_5_matches)

        for i in ko_5_matches:
            one_time_wins = [showdown(i) for j in range(5)]
            #print(one_time_wins)
            winner_round = max(set(one_time_wins), key = one_time_wins.count)#bei jedem Match wird es 5 Mal gespielt. Der mit den meisten Siegen gewinnt.
            winners.append(winner_round)
        
        #print(winners)
        return ko_5(winners)#die Funktion wird rekursive wiederholt, bis nur ein Gewinner übrig bleibt.

def count_wins_of_starkster(func, num_of_plays):
    count = 0
    for i in range(num_of_plays):
        if func == liga:
            x = func(plays_dict)
            if x == starkster:
                count += 1
        else:
            x = func(players)
            if x == starkster:
                count += 1
    return count

x = count_wins_of_starkster(ko, 100)#diese Funktion gibt wieder, wie oft der Stärkster in einer Spielvariante über 100 Spiele gewinnt.
print(x)
  

