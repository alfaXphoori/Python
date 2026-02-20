# Python KPS Module 1 - Interactive Examples

## Table of Contents

- [Basic Mathematics](#01-basic-mathematics)
- [Print Statements](#02-print-statements)
- [Variables](#04-variables)
- [Conditionals](#05-conditionals)
- [Lists](#06-lists)
- [Friends Scores Analysis](#07-09-friends-analysis)
- [Area Calculations](#11-14-area-calculations)
- [Linear Relationship](#15-linear-relationship)
- [Turtle Graphics](#16-19-turtle-graphics)

## 01 - Basic Mathematics

[Run full example](examples/01_basic_math.py)

```python
print(100+50)   # 150
print(100*50)   # 5000
print(100/50)   # 2.0
print(50**2)    # 2500
print(53**5)    # 418195493
```

## 02 - Print Statements

[Run full example](examples/02_print_basic.py)

```python
print("Hello World")
print("Student")
print(100)
print(50)
```

## 03 - Print with Calculation

[Run full example](examples/03_print_calc.py)

```python
print("ตัวเลข 100 บวกกับ 50 จะได้")
print("ผลลัพธ์คือ", 100+50)
```

## 04 - Variables

[Run full example](examples/04_variables.py)

```python
my_name = "Thanakorn yarnguy"
number1 = 30
number2 = 25
print("ฉันชื่อ", my_name)
print("เลขตัวที่ 1 คือ", number1)
print("เลขตัวที่ 2 คือ", number2)
```

## 05 - Conditionals

[Run full example](examples/05_conditionals.py)

```python
if number1 > number2:
    print("คนที่ 1 น้ำหนักมากกว่าคนที่ 2")
else:
    print("คนที่ 2 น้ำหนักมากกว่าคนที่ 1")
```

## 06 - Lists

[Run full example](examples/06_lists.py)

```python
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(mylist[0])
print(mylist[1])
```

## 07-09 - Friends Scores Analysis

[Show friends list](examples/07_friends_scores.py) | [Analysis](examples/08_friends_analysis.py) | [Enhanced Bar Chart](examples/10_enhanced_bar_chart.py)

**Friends and Scores:**
```python
friends = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack", "Kate", "Leo", "Mary", "Nick", "Olivia"]
scores = [85, 92, 78, 95, 88, 76, 90, 82, 87, 91, 79, 84, 93, 80, 86]
```

**Max/Min/Average:**
```python
max_score = max(scores)  # Highest: 95 (David)
min_score = min(scores)  # Lowest: 76 (Frank)
average = sum(scores) / len(scores)  # ~85.07
```

![Enhanced Bar Chart](images/10_enhanced_bar_chart.png)

## 11-14 - Area Calculations

[Rectangle](examples/11_area_rectangle.py) | [Triangle](examples/12_area_triangle.py) | [Circle](examples/13_area_circle.py) | [Circle Graph](examples/14_area_circle_graph.py)

**Examples:**
```python
# Rectangle
area = width * length

# Triangle  
area = 0.5 * base * height

# Circle
area = math.pi * (radius ** 2)
```

![Circle Graph](images/14_area_circle_graph.png)

## 15 - Linear Relationship

[Run full example](examples/15_linear_graph.py)

**y = 10x** (Notebook price example)

![Linear Graph](images/15_linear_graph.png)

## 16-19 - Turtle Graphics

**Note:** Requires ColabTurtle (`!pip3 install ColabTurtle`)

[Square](examples/16_turtle_square.py) | [Star](examples/17_turtle_star.py) | [Spiral](examples/18_turtle_spiral.py) | [Shapes](examples/19_turtle_shapes.py)

**Angle Reference:**
| Angle | Shape |
|-------|-------|
| 121° | Twisted Triangle |
| 91° | Twisted Square |
| 73° | Twisted Pentagon |
| 61° | Twisted Hexagon |
| 144° | Star |

![Turtle Examples](images/turtle_examples.png)

---

**📁 All examples:** [examples/ folder](examples/)

**Run examples:** `cd examples && python3 XX_filename.py`

**Images folder empty** - Add screenshots to `images/` for better visuals.

```bash
!pip3 install ColabTurtle
```

### วาดสี่เหลี่ยม

```python
from ColabTurtle.Turtle import *

initializeTurtle()
color("red")
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
```

### วาดรูปดาวห้าแฉก

```python
initializeTurtle()
color("blue")      # กำหนดสีเต่าเป็นสีน้ำเงิน
pensize(10)        # กำหนดความหนาของเส้น
speed(5)           # กำหนดความเร็วในการวาด

for _ in range(5):
    forward(150)
    right(144)
```

### วาดรูปสวยงามด้วยสีหลากสี

```python
initializeTurtle()
speed(10)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(250):
    pencolor(colors[i % 6])
    forward(i * 2)
    left(59)
```

### วาดรูปทรงต่างๆ ด้วยการปรับมุม

```python
initializeTurtle()
speed(10)
pensize(8)
colors = ["red", "orange", "yellow", "green"]

for i in range(250):
    pencolor(colors[i % 4])  # สลับสีไปเรื่อยๆ ทีละสี 4 สี
    forward(i * 2)
    left(121)
```

### ตารางมุมและรูปทรงที่ได้

| มุม (องศา) | รูปทรงที่ได้ |
|-------------|---------------|
| 121 | สามเหลี่ยมบิดเกลียว (Triangle) |
| 91 | สี่เหลี่ยมบิดเกลียว (Square) |
| 73 | ห้าเหลี่ยมบิดเกลียว (Pentagon) |
| 61 | หกเหลี่ยมบิดเกลียว (Hexagon) |
| 144 | รูปดาว (Star) |

**การกำหนดการแสดงผลสี:** ปรับที่ `colors` และ `i % 6`  
**การกำหนดรูปทรง:** ปรับที่ `left(121)`
