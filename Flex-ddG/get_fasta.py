import numpy as np

best_seqs = []
best_scores = []
for i in range(40):
    scores = []
    seqs = []
    with open("./output/flex_" + str(i) + ".out", "r") as f:
        for line in f:
            if line[0] == "[":
                scores.append(float(line.split("<")[1][:-2].split(",")[0]))
                seqs.append(line.split("<")[1][:-2].split(",")[1])
        best_seqs.append(seqs[scores.index(min(scores))])
        best_scores.append(min(scores))
fasta = ""
ord = np.argsort(best_scores)
for i in range(40):
    fasta += (
        ">orient"
        + str(ord[i] // 5 + 1)
        + "run"
        + str(ord[i] % 5 + 1)
        + ":"
        + str(best_scores[ord[i]])
        + "\n"
        + best_seqs[ord[i]]
        + "\n"
    )
print(fasta)
