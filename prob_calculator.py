import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, number):
        if (number > len(self.contents)):
            return self.contents
        removed = []
        for i in range(number):
            r = self.contents.pop(int(random.random() * len(self.contents)))
            removed.append(r)
        return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        out_balls = hat_copy.draw(num_balls_drawn)
      
        for color in out_balls:
            if (color in expected_copy):
                expected_copy[color] = expected_copy[color] - 1
        
        for x in expected_copy.values():    
            if (x <= 0):
                k = 1
            else:
                k = 0
                break
      
        if k ==1:
            count += 1
    return count / num_experiments
