# Decreasing Order Strings
'''
Sorting numbers is something we are very much comfortable with. Let's get comfortable with sorting strings as well. 
The task is simple, given a string S you have to sort the characters of the string in lexicographically-decreasing order.

Note - Do not use inbuilt sorting function.

Input format
The first line contains an integer T, denoting the number of test cases.
Each test case consists of a string S containing only lowercase characters.

Output format
For each test case on a new line, print the string sorted in lexicographically-decreasing order.

Constraints
. 1 <= T <= 5
. 1 <= |S| <= 10^6, where |S| denotes length of string S.

Time limit
1 second

Example
Input
2
prepbytes
algorithm

Output
ytsrppeeb
tromlihga
'''
# SOLUTION - 22/3/2022 3:10PM
for _ in range(int(input())):
    string = input();
    str_set = ''.join(set(string));
    while len(str_set) > 0:
        greater = str_set[0];
        for i in range(1, len(str_set)):
            if str_set[i] > greater:
                greater = str_set[i];
        print(greater*string.count(greater), end='');
        str_set = str_set.replace(greater, '');
    print();
