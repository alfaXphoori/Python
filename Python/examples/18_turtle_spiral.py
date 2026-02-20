initializeTurtle()
speed(10)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(250):
    pencolor(colors[i % 6])
    forward(i * 2)
    left(59)