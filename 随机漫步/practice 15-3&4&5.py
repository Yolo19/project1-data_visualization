import matplotlib.pyplot as plt

from 随机漫步.random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    point_number = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=5)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break