l1, l2 = [], []

with open("input.txt", "r") as f:
    for l in f:
        id = l.rstrip().split()
        l1.append(int(id[0]))
        l2.append(int(id[-1]))

# Part One
a = sorted(l1)
b = sorted(l2)
dist = sum([abs(a[i] - b[i]) for i in range(len(l1))])
print("Total Distance:", dist)

# Part Two
sim_score = sum([n * l2.count(n) for n in l1])
print("Similarity Score:", sim_score)
