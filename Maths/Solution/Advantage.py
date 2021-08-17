# Advantage
'''
Everyone knows that PK came from a different planet because of problems in the spaceship and finds everything new on the earth. 
Although he lost his remote, his powers help in understanding and speaking the native language and he started finding the remote 
everywhere. Most of the people took advantage of him and also try to grab money from him. By seeing all this one kid also took 
advantage of him by assigning him a task in which he provided three integers X, Y, K and told him that he has to find the count of 
the numbers between X and Y (both inclusive) which are divisible by K and promised him if he can solve it he helps in finding the remote.
As PK doesn't know anything about such a task, so he wants your help so that he can get his remote back. 

Input Format
The first line of the input contains three space-separated integers X, Y and K.

Output Format
Print the count of the numbers.

Constraints
. 1 ≤ X,Y ≤ 1000
. 1 ≤ K ≤ 1000

Example
Sample Input
1 10 1

Sample Output
10
'''
# SOLUTION - 17/8/2021 5:21PM
x, y, k = map(int, input().split())
print(len([num for num in range(x, y+1) if num % k == 0]))
