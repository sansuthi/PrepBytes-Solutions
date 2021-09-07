# Permutation Queries
'''
You are given an array of  queries consisting of n positive integers between 1 and m, you have to process all queries[i] according to the following rules:
In the beginning, you have the permutation  P=1,2,3,...,m.
For the current  i, find the position of  queriesi  in the permutation P(indexing from 0) and then move this at the beginning of the permutation  P. 
For each query, you need to print the position of queriesi  in  P.

Input Format
First line of input contains two integers n and m -denoting the number of queries and size of the permutation P.
Second line of input contains n space separated integers-denoting each query.

Output Format
Print n space separated integers-denoting the position of queriesi  in  P.

Constraints
. 1 ≤ m ≤ 10^3
. 1 ≤ n ≤ m
. 1 ≤ queries[i] ≤ m

Examples
Input
4 5
4 2 5 1

Output
3 2 4 3 

Explanation
The queries are processed as follow: 
For i=0: queriesi=4, P=1,2,3,4,5, position of 4 in P is 3, then we move 4 to the beginning of P resulting in P=4,1,2,3,5. 
For i=1: queriesi=2, P=4,1,2,3,5. , position of 2 in P is 2, then we move 2 to the beginning of P resulting in P=2,4,1,3,5. 
For i=2: queriesi=5, P=2,4,1,3,5, position of 5 in P is 4, then we move 5 to the beginning of P resulting in P=5,2,4,1,3. 
For i=3: queriesi=1,P=5,2,4,1,3, position of 1 in P is 3, then we move 3 to the beginning of P resulting in P=1,5,2,4,3. 
Therefore, the result is 3 2 4 3
'''
# SOLUTION - 7/9/2021 12:36PM
nq, np = map(int, input().split())
queries = list(map(int, input().split()))
P, pos = [a for a in range(1, np+1)], []
for query in queries:
  pos.append(P.index(query))
  P.remove(query)
  P.insert(0, query)
print(*pos)
