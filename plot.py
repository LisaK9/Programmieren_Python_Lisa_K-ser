import matplotlib.pyplot as plt

plt.style.use('seaborn')


def train_functions(x, y1, y2, y3, y4):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.subtitle = 'train functions'
    ax1.scatter(x, y1, s=8, color='blue')
    ax1.set_title('train function 1')
    ax2.scatter(x, y2, s=8, color='blue')
    ax2.set_title('train function 2')
    ax3.scatter(x, y3, s=8, color='blue')
    ax3.set_title('train function 3')
    ax4.scatter(x, y4, s=8, color='blue')
    ax4.set_title('train function 4')
    plt.tight_layout()
    plt.show()