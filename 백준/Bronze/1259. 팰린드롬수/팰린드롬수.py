def palindrome(N):
    for i in range(0,int(len(N)/2)):
        if N[i] != N[len(N)-1-i]:
            print('no')
            return
    print('yes')
    return

while(True):
    N = input()
    if N == '0': break
    palindrome(N)