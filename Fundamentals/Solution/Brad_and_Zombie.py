# Brad and Zombie
'''
The whole world is fighting against zombies right now. Brad Pitt is leading the whole world's army against the zombies. 
He is on a mission to kill all the zombies so that the whole world can again start living life peacefully. He is killing 
zombies one by one strategically. Now, Brad and the zombie, both are on the coordinate axis Ox in points with integer coordinates. 
Brad is currently at the point x1 = A and the zombie is at the point x2 = B. Both of them want to kill each other and for this, 
they have to come at a single point. Both can move by one along the line in any direction an unlimited number of times. When any 
one of them moves, their energy decreases according to the following rules:-

. The first move decreases the energy by 1
. The second move decreases the energy by 2
. The third move decreases the energy by 3 and so on

So, for example if either of them moves 4 steps, his energy will be decreased by 10 because 1 + 2 + 3 + 4 = 10.

Both of them want to lose as little as possible energy and want to come at the same integer point for the fight.
Your task is to determine the minimum energy they should lose if they met at the same point.

Note:- Both, Brad and the zombie have an unlimited amount of energy.

Input Format
. The first line contains a single integer A, denoting the initial position of the Brad Pitt.
. The second line contains a single integer B, denoting the initial position of the zombie.
It is guaranteed that A ≠ B.

Output Format
print the minimum possible loss in energy if both meet at the same point.

Constraints
. 1 ≤ A ≤ 1000
. 1 ≤ B ≤ 1000

Example
Sample Input
5
10

Sample Output
9
'''
# SOLUTION - 27/3/2022 9:46AM
diff = abs(int(input())- int(input()));
energy = 0;
for i in range(diff//2+1):
    energy += 2 * i;
if diff % 2 == 0: 
    print(energy);
else: 
    print(energy+diff//2+1);
