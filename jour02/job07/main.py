lettres = "abcdefghijklmnopqrstuvwxyz" * 10
for i in range(len(lettres)):
    if i % 2 != 0:
        print(lettres[:i])