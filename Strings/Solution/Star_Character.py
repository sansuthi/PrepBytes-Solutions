# Star Character
'''
PrepBuddy has a collection of strings stored in an array. He wants to know the count of Star Characters present in the 
collection. A Star character is a character that occurs at least once in each of the string present inside the collection.

Input format
The first line contains an integer T denoting the number of test cases.
For each test case:
The first line contains an integer N denoting the number of strings present inside the collection.
Each of the next N lines contains a string.

Output format
For each test case on a new line, print the count of Star characters.

Constraints:
. 1 <= T <= 10
. 1 <= N <= 100
. 1 <= |S| <= 100

Time Limit
1 second

Example
Input
3
3
abcdde
baccd
eeabg
4
basdfj
asdlkjfdjsa
bnafvfnsd
oafhdlasd
3
vtrjvgbj
mkmjyaeav
sibzdmsk

Output
2
4
0
'''
# SOLUTION - 22/3/2022 9:29PM
for _ in range(int(input())):
    N = int(input()); 
    strings = []; star_count = 0;
    for i in range(N):
        strings.append(input());
    for letter in set(strings[0]):
        count = 0;
        for i in range(1, N):
            if strings[i].count(letter) >= 1:
                count += 1;
            else:
                break;
        if count == N-1:
            star_count += 1;
    print(star_count);
