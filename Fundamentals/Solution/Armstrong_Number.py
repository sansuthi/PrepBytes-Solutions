# Armstrong Number
'''
Alex is a maths freak and he loves reading new concepts and solving problems on them. Recently he read about Armstrong numbers 
that a number N having X digits is an Armstrong number:- If the sum of all the digits of number N to power X is equal to the number.
For example, If N = 1634, X = 4, as 1^4 + 6^4 + 3^4 + 4^4 = 1634, So the number 1634 is a Armstrong Number. Similarly, 371 is also an 
Armstrong number as 3^3 + 7^3 + 1^3 = 371.

Note: X is the number of digits in number N.

Alex received some homework on Armstrong number but somehow he forgot the equation to check whether a number is Armstrong or not. 
You are a good friend of Alex help him to complete his homework.

Input format
. The First line of the input contains an integer T, denoting the number of test cases.
. Next T lines contain test cases, each test case contains one integer N.

Output format
For each test case print "YES" (without quotes) if the number is Armstrong otherwise "NO" (without quotes).

Constraints
. 1 ≤ T ≤ 100
. 1 ≤ N ≤ 10^9

Example
Input
2
66
371

Output
NO
YES

Sample test case explanation
N = 66, so X = 2. Equation is 6^2 + 6^2 = 36 + 36 = 72, which is not equal to 66. Hence N=66 is not an Armstrong number.
N = 371, so X = 3. Equation is 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371, which is equal to 371. Hence N=371 is an Armstrong number.
'''
# SOLUTION - 8/8/2021 12:57PM
for _ in range(int(input())):
  num = int(input())
  asum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    asum += digit ** len(str(num))
    temp //= 10
  print('YES') if num == asum else print('NO')
