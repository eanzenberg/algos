from collections import namedtuple
from typing import List, Tuple


def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    def check_collision(start: Tuple[int, int], dir: str, amount: int, 
                         obstacles_set: set) -> Tuple[int, int]:
        direction = namedtuple('direction', ['x', 'y'])
       
        move = {'n': direction(0,1),
                's': direction(0,-1),
                'e': direction(1,0),
                'w': direction(-1,0)}
        
        x, y = start

        for _ in range(amount):
            x, y = x + move[dir].x, y + move[dir].y
            if (x,y) in obstacles_set:
                return x - move[dir].x, y - move[dir].y

        return x, y
    

    obstacles_set = set(tuple(item) for item in obstacles)
    dirs = {'n': {'l': 'w',
                  'r': 'e'},
            'e': {'l': 'n',
                  'r': 's'},
            's': {'l': 'e',
                  'r': 'w'},
            'w': {'l': 's',
                  'r': 'n'}}

    dir = 'n'
    x, y = 0, 0
    ans = 0

    for com in commands:
        if com == -2:
            dir = dirs[dir]['l']
        elif com == -1:
            dir = dirs[dir]['r']
        else:
            x, y = check_collision(start=(x, y),
                                    dir=dir,
                                    amount=com,
                                    obstacles_set=obstacles_set)
        ans = max(ans, x**2 + y**2)
    return ans


fn_input = namedtuple('fn_input', ['commands', 'obstacles'])
test = namedtuple('test', ['input', 'output'])

tests = [
        test(fn_input([4,-1,3], []), 25),
        test(fn_input([4,-1,4,-2,4], [[2,4]]), 65),
        test(fn_input([6,-1,-1,6], [[0,0]]), 36),
        test(fn_input([7,-2,-2,7,5], []), 49),
        test(fn_input([-2,-1,8,9,6], [[-1,3],[0,4],[0,1], [-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]]), 0),
        test(fn_input([-2,-1,8,9,6], [[0,4],[0,3]]), 4),
        test(fn_input([-2,-1,8,9,6], [[0,3],[0,4]]), 4),        
        test(fn_input([-2,-2,8,9,6], [[0,-4],[0,-3]]), 4),
        test(fn_input([-2,-2,8,9,6], [[0,-3],[0,-4]]), 4),
        test(fn_input([-1,8,9,6], [[4,0],[3,0]]), 4),
        test(fn_input([-1,8,9,6], [[3,0],[4,0]]), 4),
        test(fn_input([-2,8,9,6], [[-4,0],[-3,0]]), 4),
        test(fn_input([-2,8,9,6], [[-3,0],[-4,0]]), 4),        
        test(fn_input([7,-2,-2,7,5], [[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]]), 4)        
]

for t in tests:
    ans = robotSim(commands=t.input.commands, 
                   obstacles=t.input.obstacles)
    print(ans, t.output)
    assert ans == t.output