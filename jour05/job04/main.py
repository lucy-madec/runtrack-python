def tapis(n):
    h_b = "+" + "-" * (n+1) + "+"
    print(h_b)

    for i in range(n + 1):
        hashtag = "#" * (n + 1)
        liste = list(hashtag)
        if i < len(liste):
            liste[-i - 1] = " "
        space = ""
        for tapis in liste:
            space +=tapis
        print("|"+space+"|")

    print(h_b)

tapis(5)