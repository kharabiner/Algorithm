import sys
input = sys.stdin.readline

N = int(input().strip())
label = 'WelcomeToSMUPC'
print(label[N%14-1])