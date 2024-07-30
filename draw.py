import matplotlib.pyplot as plt

def draw(path):
    for i in range(100):
        for j in range(100):
            if (i, j) in path:
                plt.plot(i, j, 'ro')
            else:
                plt.plot(i, j, 'bo')

    plt.show()