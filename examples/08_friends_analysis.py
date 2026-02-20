# หาคะแนนสูงสุด
max_score = max(scores)
max_index = scores.index(max_score)
print(f"คนที่ได้คะแนนมากที่สุดคือ {friends[max_index]} ได้คะแนน {max_score}")

# หาคะแนนต่ำสุด
min_score = min(scores)
min_index = scores.index(min_score)
print(f"คนที่ได้คะแนนน้อยที่สุดคือ {friends[min_index]} ได้คะแนน {min_score}")

# หาคะแนนเฉลี่ย
average_score = sum(scores) / len(scores)
print(f"คะแนนเฉลี่ยของทุกคนคือ {average_score:.2f}")
