import matplotlib.pyplot as plt
import numpy as np

friends = ["Alice", "Bob", "Charlie", "David", "Emma", 
           "Frank", "Grace", "Henry", "Ivy", "Jack",
           "Kate", "Leo", "Mary", "Nick", "Olivia"]
scores = [85, 92, 78, 95, 88, 76, 90, 82, 87, 91, 
          79, 84, 59, 80, 86]

plt.figure(figsize=(10, 6))
colors = ['skyblue'] * len(scores) # เริ่มต้นด้วยสีฟ้าอ่อนทั้งหมด
for i, score in enumerate(scores):
    if score < 60:
        colors[i] = 'orange'
    elif score > 80:
        colors[i] = 'lightgreen' # ใช้ lightgreen เพื่อให้แตกต่างจากสีส้มและฟ้าอ่อน
plt.bar(friends, scores, color=colors)
plt.xlabel("Friend Name")
plt.ylabel("Score")
plt.title("Scores of Each Friend")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
