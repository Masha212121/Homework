best_score = 0

while True:
    score = int(input())
    if score == -1:
        break
    if score > best_score:
        best_score = score

print(best_score)