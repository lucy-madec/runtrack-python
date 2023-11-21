n = int(input())
x = 0
while x<n:
    x+=1
    print("Table de multiplication", x)
    
    for i in range(1,10):
        print(i, "x", n, "=", i*n)
