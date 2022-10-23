# -*- coding: utf-8 -*-
n = int(input())
game = ['tesoura','pedra','spock','papel','lagarto']

while(n > 0):
    n -= 1
    s, r = input().split()
    while(game[2] != s):
            game = [game[-1]] + game[:-1]
    s = 2-game.index(r)
    if(s > 0):
        print('rajesh')
    elif(s < 0):
        print('sheldon')
    else:
        print('empate')