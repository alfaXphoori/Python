# สร้าง List ของรายชื่อเพื่อน 15 คน (ภาษาอังกฤษ)
friends = ["Alice", "Bob", "Charlie", "David", "Emma", 
           "Frank", "Grace", "Henry", "Ivy", "Jack",
           "Kate", "Leo", "Mary", "Nick", "Olivia"]

# สร้าง List สำหรับเก็บค่าคะแนน 15 ค่า
scores = [85, 92, 78, 95, 88, 76, 90, 82, 87, 91, 
          79, 84, 93, 80, 86]

# แสดงข้อความชื่อเพื่อนและคะแนนที่ได้ เรียงตามลำดับใน list
for i in range(len(friends)):
    print(f"เพื่อนคนที่ {i+1} ชื่อ {friends[i]} ได้คะแนน {scores[i]}")