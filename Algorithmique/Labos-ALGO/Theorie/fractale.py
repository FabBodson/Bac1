import matplotlib.pyplot as plt


def dragon(n, x, y, z, t):
    if n == 1:
        plt.plot([x, z], [y, t], color='r');
        # print(n, x, y, z, t)
    else:
        u = (x + z + t - y) / 2
        v = (y + t - z + x) / 2
        dragon(n - 1, x, y, u, v)
        dragon(n - 1, z, t, u, v)


dragon(4, 100.0, 100.0, 200.0, 200.0)
plt.show()
