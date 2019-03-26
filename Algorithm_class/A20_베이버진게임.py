import sys
sys.stdin = open('A20_베이비진게임_input.txt')



def solution(card):
    player1 = {x: [0, 0] for x in range(10)}
    player2 = {x: [0, 0] for x in range(10)}

    for i in range(0, 12, 2):
        player1[card[i]][0] += 1
        if player1[card[i]][0] == 3:
            return 1
        if player1[card[i]][1] == 2:
            return 1

        if card[i]-1 >= 0 and player1[card[i]][0] == 1:
            player1[card[i] - 1][1] += 1
            if  player1[card[i]-1][1] == 2 and player1[card[i]-1][0] > 0:
                return 1

        if card[i]+1 < 10 and player1[card[i]][0] == 1:
            player1[card[i] + 1][1] += 1
            if player1[card[i]+1][1] == 2 and player1[card[i]+1][0] > 0:
                return 1

        player2[card[i+1]][0] += 1
        if player2[card[i+1]][0] == 3:
            return 2
        if player2[card[i+1]][1] == 2:
            return 2

        if card[i+1] - 1 >= 0 and player2[card[i+1]][0] == 1:
            player2[card[i+1] - 1][1] += 1
            if player2[card[i+1]-1][1]== 2 and player2[card[i+1]-1][0] > 0:
                return 2

        if card[i+1] + 1 < 10 and player2[card[i+1]][0] == 1:
            player2[card[i+1] + 1][1] += 1
            if  player2[card[i+1] + 1][1] == 2 and player2[card[i+1]+1][0] > 0:
                return 2
    return 0


T = int(input())
for tc in range(T):
    card = list(map(int, input().split()))
    print('#{} {}'.format(tc+1, solution(card)))
