from random import choice
class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_value = [0]
        self.y_value = [0]


    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)

import matplotlib.pyplot as plt

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))

    plt.plot(rw.x_value, rw.y_value, linewidth=1)
    # plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=100)


    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()

    # keep_running = input('Make another walk? (y/n): ')
    # if keep_running == 'n':
    #     break
# x_input_values = list(range(1, 5001))
# y_squares = [x ** 3 for x in x_input_values]
# # plt.plot(input_values, squares, linewidth=5)
# plt.title("Cube Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Cube of Value", fontsize=14)
# #
# # plt.tick_params(axis="both", labelsize=14)
# # plt.show()
#
# plt.scatter(x_input_values, y_squares, c=y_squares, cmap=plt.cm.Blues, edgecolors='none', s=40)
# plt.axis([0, 1100, 0, 1100000])
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
#
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()