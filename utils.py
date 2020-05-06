import numpy as np

def read_csv(file_name):

    X = []
    y = []
    try:
        with open(file_name, 'r') as file:
            # skip first line with labels
            lines = file.readline()

            # read all lines
            lines = file.readlines()

            for line in lines:
                # split lines by ','
                temp = line.split(',')

                # append features
                X.append(temp[0])

                # append target without '\n'
                y.append(temp[1][:-1])
    except Exception:
        print('Cant open file.')

    return np.array(X, dtype=float), np.array(y, dtype=float)

def save_thetas(theta_0, theta_1):
    if (theta_0 != 0.0) and (theta_1 != 0.0):
        try:
            theta_value_file = open('thetas.txt', 'w')
            theta_value_file.write('{}\n{}'.format(theta_0, theta_1))
            theta_value_file.close()
        except Exception:
            print("message: An error happened !")
