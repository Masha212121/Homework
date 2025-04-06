scores = input().split()
scores = [int(score) for score in scores]

best_score = scores[0]
for score in scores[1:]:
    if score > best_score:
        best_score = score

print(f"{best_score}")