initializeTurtle()
speed(10)
pensize(8)
colors = ["red", "orange", "yellow", "green"]

for i in range(250):
    pencolor(colors[i % 4])  # สลับสีไปเรื่อยๆ ทีละสี 4 สี
    forward(i * 2)
    left(121)
