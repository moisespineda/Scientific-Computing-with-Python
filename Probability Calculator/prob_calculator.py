import random
import copy

class Hat:
    def __init__(self, **kargs):
        self.contents=[k for k, v in kargs.items() for i in range(v)]
    
    def draw(self, n_balls_to_pop):
        if n_balls_to_pop>len(self.contents):
            draw_out=self.contents
            return draw_out
        balls_drawn = random.sample(self.contents, n_balls_to_pop)

        for i in balls_drawn:
            self.contents.remove(i)
        
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n = 0
    for i in range(num_experiments):
        drawn = []
        #string2 = copy.copy(string)
        hatexp = copy.deepcopy(hat)
        drawn = hatexp.draw(num_balls_drawn)
        check = True
        for key,value in expected_balls.items():
            if (value > drawn.count(key)):
                check = False
                break
        if(check):
            n += 1
    return n/num_experiments