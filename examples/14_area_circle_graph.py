import math
import matplotlib.pyplot as plt

# รับค่ารัศมีจากผู้ใช้
radius = float(input("ป้อนความยาวรัศมีของวงกลม: "))

# คำนวณพื้นที่ (pi * r^2)
area = math.pi * (radius ** 2)

# แสดงผลลัพธ์
print(f"พื้นที่วงกลมคือ: {area:.2f}")

# สร้างกราฟวงกลม
fig, ax = plt.subplots(figsize=(6, 6))
circle = plt.Circle((0, 0), radius, color='blue', alpha=0.5)
ax.add_artist(circle)

# ตั้งค่าแกน
ax.set_xlim([-radius * 1.2, radius * 1.2])
ax.set_ylim([-radius * 1.2, radius * 1.2])
ax.set_aspect('equal', adjustable='box')

# ใช้ฟอนต์ที่รองรับภาษาไทยหรือเปลี่ยนเป็นภาษาอังกฤษเพื่อหลีกเลี่ยง warning
plt.rcParams['font.family'] = ['DejaVu Sans', 'sans-serif']
plt.title(f'Circle with radius = {radius} and area = {area:.2f}')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
