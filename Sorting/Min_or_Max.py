# Min Or Max
'''
N cards are arranged from left to right. The ith card has a number Ai written on it. Alice and Bob both are playing 
a game with these cards.Both of them are playing the game optimally and alternatively, in their respective turn, they 
pick a card and remove it. The game continues until one card left.Alice wants the last card to be minimum while Bob 
wants the last card to be maximum. Find the last card that will be left at the end of the game if Alice starts the game.

Input Format
The first line of each test case a single integer N - the number of cards.
The next line contain N space-separated integers A1,A2,.....AN - the values written on the cards. 

Output Format
Print a single line - the value written on the last card.

Constraints
1 ≤ N ≤ 2∗10^3
1 ≤ Ai ≤ 2∗10^9

Example
Sample Input
3 
2 1 3

Sample Output
2

Explanation
Alice removes the third card then Bob removes 2nd card and the first card will left.
'''
# SOLUTION - 31/7/2021 5:52PM
n = input()
array = list(map(int, input().split()))
for i in range(int(len(array)/2)):
    array.remove(max(array))
    if len(array) > 1:
        array.remove(min(array))
print(array[0])
