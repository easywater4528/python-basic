import matplotlib.pyplot as plt

# 간단한 데이터
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 그래프 그리기
plt.plot(x, y, marker='o')
plt.title("Sample Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.savefig("my_plot.png") 
plt.show() 
