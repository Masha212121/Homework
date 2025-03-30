N = int(input())
volumes = []
k = 1
while True:
    volume = k ** 3
    if volume > N:
        break
    volumes.append(volume)
    k += 1
print(' '.join(map(str, volumes)))