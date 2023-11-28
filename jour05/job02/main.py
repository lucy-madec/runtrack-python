def draw_rectangle(width, height):
    width = width - 2
    height = height - 2
    trait= "|" + "-" * width +"|"
    print(trait)
    for i in range(height):
        print("|" + " " * (width) + "|")
    print(trait)
draw_rectangle(10, 3)