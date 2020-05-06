import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--eval', type=str, help='sum the integers (default: find the max)')

args = parser.parse_args()

def normalize(self, X):
    # Min max scaling
    x_max = X.max()
    x_min = X.min()
    return (X - x_min) / (x_max - x_min)

def evaluate(X, theta_0, theta_1):
    return theta_0 + theta_1 * X

if __name__ == '__main__':

    mileage = input("Enter mileage: ")

    try:
        with open('thetas.txt') as file:    
            lines = file.readlines()
            theta_0 = float(lines[0])
            theta_1 = float(lines[1])
        print('Estimated value: {}'.format(evaluate(int(mileage), theta_0, theta_1)))
    except:
        theta_0 = 0
        theta_1 = 0
        print('Estimated value: {}'.format(evaluate(int(mileage), theta_0, theta_1)))
