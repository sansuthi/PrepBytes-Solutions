# Dice Game
'''
Pragya and Tina love to play the Dice game whenever they are free. A dice contains 6 distinct numbers from 1 to 6. 
Rules of the game are simple, they decide the number of games to be played represented by N, each game has two rounds, 
in first round Pragya throws the dice and in the second round Tina throws the dice, player whose value after throwing 
the dice is greater wins that game. If the values are the same than the game is declared a draw.

The player who won more games among the N games that are played in a day is declared as the winner of the day.

Input format
First line contains an integer N, representing the number of games to be played in a day.
Each of the next N lines contains two integers P and Q representing the dice value for Pragya and Tina respectively.

Output format
Print Pragya if Pragya is Winner of the day.
Print Tina if Tina is Winner of the day.
Print Draw if the number of games won by Pragya and Tina is equal.

Constraints
. 2 <= N <= 100
. 1 <= P,Q <= 6

Example
Input
3
1 3
2 2
4 5

Output
Tina

Sample test case explanation
Game 1: Tina won
Game 2: Draw
Game 3: Tina won
So the Winner of the day is Tina.
'''
# SOLUTION - 20/3/2022 11:23PM
N = int(input())
p_score = t_score = 0
while N != 0:
  score1, score2 = map(int, input().split())
  if score1 > score2:
    p_score += 1
  elif score1 < score2:
    t_score += 1
  N -= 1
if t_score > p_score:
  print('Tina')
elif t_score < p_score:
  print('Pragya')
else:
  print('Draw')
