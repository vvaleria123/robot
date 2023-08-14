import enum
X, Y, C = map(int, input().split())
robot1 = [int(i) for i in input().split()] #col,raw, direction of init pos of robot
commands1 = input().split() #послідовність команд для робота 1
robot2 = [int(i) for i in input().split()] #the same specification
commands2 = input().split() #послідовність команд для робота 2
print(X, Y, C)
print(robot1)
print(commands1)
print(robot2)
print(commands2)

count=0

class Robot:
    def __init__(self, init_pos_x, init_pos_y, init_dir):
        self.pos_x = init_pos_x
        self.pos_y = init_pos_y
        self.dir = init_dir  # you are not shadowing python's dir() globally, so it's ok

# robot = Robot(2, 3, 0)
# robot.pos_x  # instead of robot[0]




class RobotDirection(enum.IntEnum):
    EAST = 0
    NORTH = 1
    WEST = 2
    SOUTH = 3

# robot = Robot(2, 3, RobotDirection.EAST)
# robot.dir == RobotDirection.EAST  # instead of robot.dir == 0


def move_robot(robot,step, X, Y):    #відповідає за рухи робота у різних напрямках
    for _ in range(step):
        if robot.dir == RobotDirection.EAST and robot.pos_x < X:
            robot.pos_x += 1
        elif robot.dir == RobotDirection.NORTH and robot.pos_y < Y:
            robot.pos_y += 1
        elif robot.dir == RobotDirection.WEST and robot.pos_x > 1:
            robot.pos_x -= 1
        elif robot.dir == RobotDirection.SOUTH and robot.pos_y > 1:
            robot.pos_y -= 1
        if robot.pos_x > X or robot.pos_y > Y or robot.pos_x < 1 or robot.pos_y < 1: # changed
            break
    return robot
    


    

def direction_of_robot(robot, dire):   # відповідає за напрямок робота
    if dire=="L":
        if robot.dir == RobotDirection.SOUTH:
            robot.dir == RobotDirection.EAST
            return robot
        else:
            robot.dir = RobotDirection(robot.dir + 1)
            return robot
    if dire == "R":
        if robot.dir == RobotDirection.EAST:
            robot.dir == RobotDirection.SOUTH
        else:
            robot.dir = RobotDirection(robot.dir - 1)
        return robot



    

    
C1 = 0  #проходження циклів , які мають пройти роботи
while C1 < C:
    for i in commands1:
        if i == "L":
            robot1 = direction_of_robot(robot1, i)
        elif i == "R":
            robot1 = direction_of_robot(robot1, i)
        else:
            robot1 = move_robot(robot1, int(i), X, Y)
            count += 1

    for i in commands2:
        if i == "L":
            robot2 = direction_of_robot(robot2, i)
        elif i == "R":
            robot2 = direction_of_robot(robot2, i)
        else:
            print(robot1)
            robot2 = move_robot(robot2, int(i), X, Y)
            count += 1 
            
    C1 += 1

print(count)
