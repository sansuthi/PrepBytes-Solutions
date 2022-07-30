# Infection
'''
Prepbudy is having N school friends. One day Prepbudy tested covid positive and before he know about this he 
infected one of his friends. Before the report came for i=1,2,3,...N his i-th friend  meet the Ai friend and 
infect him also if he was not already infected. You have to tell how many Prepbudy's friends are getting infected.

Input format
. The first line contains two space-separated separated integers N and X 
  - the number of Prepbudy's friends and the first friend who gets infected.
. The next line contains N space-separated integers A1,A2...AN 
  - i friend meets the Ai friend.

Output format
Print a single integer - the number of Prepbudy's friends who get infected.

Constraints
. 2 ≤ N ≤ 2∗10^5
. 1 ≤ X ≤ N
. 1 ≤ Ai ≤ N

Time Limit
1 second

Example
Sample Input
4 2
3 1 1 2

Sample Output
3

Explanation
Initially, Prepbudy will infect the 2nd friend. Now, 2nd friend will infect the 1st then 
1st will infect the 3rd hence Prepbud's 3 friends will get infected.
'''
# SOLUTION - 30/7/2022 9:01AM
N, X = map(int, input().split());
A = list(map(int, input().split()));
infected = [X];
while A[X-1] not in infected:
  infected.append(A[X-1]);
  X = A[X-1];
print(len(infected));
