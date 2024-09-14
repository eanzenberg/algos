dart_score_1 = [1, 2, 4]
dart_score_2 = [1, 2, 4]
dart_score_3 = [1, 2, 4]

scores = []

for score_3 in dart_score_3:
    for score_2 in dart_score_2:
        for score_1 in dart_score_1:
            score = score_1 + score_2 + score_3
            scores.append(score)
            print(score_1, score_2, score_3, "Total score is: ", score)

print(sorted(set(scores)))
print(scores)
