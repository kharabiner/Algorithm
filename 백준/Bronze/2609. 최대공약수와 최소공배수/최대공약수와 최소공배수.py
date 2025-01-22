def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


A, B = map(int, input().split())

print(gcd(A, B))
print(int(gcd(A, B) * (A / gcd(A, B)) * (B / gcd(A, B))))
