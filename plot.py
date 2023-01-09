import matplotlib.pyplot as plt

plt.style.use('seaborn')

"""plot function for the training data"""


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


"""plot function for the ideal function of the training data and the matching test data"""


def plot_fit_test(x, y, y_ideal, label, x_test, y_test):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(x, y_ideal, color='red', linewidth=2, label='ideal function')
    ax1.scatter(x, y, marker='o', color='blue', s=12, label=label)
    ax1.set_title('train data and ideal function')
    ax1.legend()
    ax2.plot(x, y_ideal, color='red', linewidth=2, label='ideal_function')
    ax2.scatter(x_test, y_test, color='black', marker="o", s=12, label='test data')
    ax2.set_title('ideal function and matching test data')
    ax2.legend()
    plt.tight_layout()
    plt.show()
