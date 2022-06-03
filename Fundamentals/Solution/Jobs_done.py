# Jobs done
'''
Prashanna works in a company, whose boss Mr. Garg follows an outdated process of working. He asked 
Prashanna to prepare a work plan on the yearly basis. This means, on first January job-1 has to be done, 
on second January job-2 has to be done,.......on 29th January job-29 has to be done and so on... 
Now it is very difficult for Prashanna to answer boss. Because boss can ask the number of jobs done 
(How many jobs has been completed ?) till now (date/month/year).

For example: 
1. if he ask on 10/01/2020, answer would be 10.
2. if he ask on 02/03/2020, answer would be 62.

Input format
. The first line of input contains a single integer T denoting the number of test cases. 
. Then T test cases follow. Each test case consist of one line. The first line of each test case 
consists of an integer D, M, and Y where D is the day, M is the month, and Y is the year.

Output format
Print the number of jobs done till input date in new line.

Constraints
. 1 <= T <= 100
. 1 <= D <= 31
. 1 <= M <= 12
. 1990 <= Y <= 2100

Time Limit
1 second

Example
Input
2
10 1 2020
2 3 2020

Output
10
62
'''
# SOLUTION - 3/6/2022 11:27PM
for _ in range(int(input())):
  d, m, y = map(int, input().split());
  n_jobs = d;
  if m != 1:
    for i in range(1, m):
      if i == 2:
        if (y%400 == 0 or (y%4 == 0 and y%100 != 0)):
          n_jobs += 29;
        else:
          n_jobs += 28;
      elif i == 4 or i == 6 or i ==9 or i == 11:
        n_jobs += 30;
      else:
        n_jobs += 31;
  print(n_jobs);
