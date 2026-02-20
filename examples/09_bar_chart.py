import matplotlib.pyplot as plt

friends = ["Alice", "Bob", "Charlie", "David", "Emma", 
           "Frank", "Grace", "Henry", "Ivy", "Jack",
           "Kate", "Leo", "Mary", "Nick", "Olivia"]
scores = [85, 92, 78, 95, 88, 76, 90, 82, 87, 91, 
          79, 84, 93, 80, 86]

plt.figure(figsize=(12, 6))
plt.bar(friends, scores, color='skyblue')
plt.xlabel('Friends')
plt.ylabel('Scores')
plt.title('Friend Scores Bar Chart')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
