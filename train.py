import argparse
import numpy as np
import matplotlib.pyplot as plt
from utils import read_csv, save_thetas

parser = argparse.ArgumentParser()
parser.add_argument('--visu', type=str, help='sum the integers (default: find the max)')
parser.add_argument('--metric', type=str, help='sum the integers (default: find the max)')
args = parser.parse_args()

if args.visu == 'on' or args.visu == 'last' \
    or args.visu == 'mse' or args.visu == 'data':
    plt.ion()
    figure = plt.figure()
    ax = figure.add_subplot(1, 1, 1)

class LinearRegression():
    def __init__(self, X, y):

        # Set thetas to zeros in start
        self.theta_0 = 0
        self.theta_1 = 0

        # Set min max of X to use in normalize and unnormalize functions
        self.x_max = X.max()
        self.x_min = X.min()
        self.y_min = y.min()
        self.y_max = y.max()

    def estimate(self, X):
        # Estimate our hipotesis
        return self.theta_0 + self.theta_1 * X

    def normalize(self, X):
        # Min max scaling
        return (X - self.x_min) / (self.x_max - self.x_min)

    def normalize_y(self, y):
        # Min max scaling
        return (y - self.y_min) / (self.y_max - self.y_min)

    def unnormalize_y(self, y):
        # Back to Min max scaling
        return y * (self.y_max - self.y_min) + self.y_min

    def unnormalize(self, X):
        # Back to Min max scaling
        return X * (self.x_max - self.x_min) + self.x_min

    def plot_regression(self, X, y):

        # Estimate values for regression line
        x_line = [0, self.normalize(260000)]
        y_line = [self.estimate(0), self.estimate(self.normalize(260000))]

        # Delete previous plot
        ax.clear()

        # Plot out features and target values
        ax.plot(X, y, 'o', color='#008080')

        # Plot line
        ax.plot(x_line, y_line)

        # Real-time plot
        plt.pause(0.001)

    def plot_data(self, X, y):
        ax.plot(X, y, 'o', color='#008080')

    def plot_mse(self, mse):

        # Plot mse curve
        ax.plot(range(len(mse)), mse, color='#008080')
        plt.show()

    def unnormalize_thetas(self):

        # Unnormalize thetas
        lin_reg.theta_1 = (lin_reg.y_max - lin_reg.y_min) * lin_reg.theta_1 / \
            (lin_reg.x_max - lin_reg.x_min)
        lin_reg.theta_0 = lin_reg.y_min + ((lin_reg.y_max - lin_reg.y_min) * \
            lin_reg.theta_0) + lin_reg.theta_1 * (1 - lin_reg.x_min)

    def train(self, X, y, lr):

        cicle = 0
        mse_history = []
        # Length of training set
        m = len(X)

        print('Computing... ', end='')
        while True:
            # Plot regression line
            if cicle % 2000 == 0 and args.visu == 'on':
                self.plot_regression(X, y)

            # Save mse values
            if cicle % 10000 == 0 and args.visu == 'mse':
                mse = (1 / (2 * m)) * np.sum(np.square(self.estimate(X) - y))
                mse_history.append(mse)

            # Print mse every (n % 10000 == 0)
            if cicle % 10000 == 0 and args.metric == 'mse':
                mse = (1 / (2 * m)) * np.sum(np.square(self.estimate(X) - y))
                print('MSE on {} cicle: {}'.format(cicle, mse))


            # Calculate our derivatives of our MSE to our thetas
            theta_0 = (1 / m) * np.sum(self.estimate(X) - y)
            theta_1 = (1 / m) * np.sum((self.estimate(X) - y) * X)

            # Stop if converge
            if abs(theta_0) < 0.0001 and abs(theta_1) < 0.0001:
                print('Done.')
                return mse_history
            #print(self.estimate(X))

            # Substract our derivatives times learning_rate (lr)
            self.theta_0 -= lr * theta_0
            self.theta_1 -= lr * theta_1

            # Count cicle
            cicle += 1



if __name__ == '__main__':

    # Read data from file and split to X / y
    X, y = read_csv('data/data.csv')

    # Create lin_reg
    lin_reg = LinearRegression(X, y)

    # Min max normalize
    X_norm = lin_reg.normalize(X)
    y_norm = lin_reg.normalize_y(y)

    if args.visu == 'data':
        # Plot data and exit
        lin_reg.plot_data(X, y)
    else:
        # Gradient descent
        mse_history = lin_reg.train(X_norm, y_norm, 0.001)

        if args.visu == 'last':
            lin_reg.plot_regression(X_norm, y_norm)

        # Unnormalize thetas
        lin_reg.unnormalize_thetas()
        print('Estimated thetas: ', lin_reg.theta_0, lin_reg.theta_1)

    # Ptint plot after train or print MSE
    if args.visu == 'mse':
        lin_reg.plot_mse(mse_history)
l
    # Save computed thetas
    save_thetas(lin_reg.theta_0, lin_reg.theta_1)


if args.visu == 'on' or args.visu == 'last' \
    or args.visu == 'mse' or args.visu == 'data':
    plt.ioff()
    plt.show()
