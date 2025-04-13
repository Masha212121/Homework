def is_palindrome(s):
    return s == s[::-1]

for N in range(100000, 1000000):
    s = str(N)
    if not is_palindrome(s[-5:]):
        continue
    if not is_palindrome(str(N + 1)[-5:]):
        continue
    s2 = str(N + 2).zfill(6)
    if not is_palindrome(s2[1:5]):
        continue
    if not is_palindrome(str(N + 3)):
        continue
    print(N)
    break