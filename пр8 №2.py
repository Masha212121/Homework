best_score = 0
friend_count = 0

while True:
    score = int(input())
    if score == -1:
        break
    friend_count += 1
    if score > best_score:
        best_score = score

print(best_score)
print(friend_count)