X, Y, C = map(int, input().split())
robot1 = list(map(int, input().split())) #col,raw, direction of init pos of robot
commands1 = input().split() #послідовність команд для робота 1
robot2 = list(map(int, input().split())) #the same specification
commands2 = input().split() #послідовність команд для робота 2
print(X, Y, C)
print(robot1)
print(commands1)
print(robot2)
print(commands2)

count=0


def move(robot,step, X, Y):    #відповідає за рухи робота у різних напрямках
    for s in range(step):
        if int(robot[2])==0 and robot[0] < X:
            robot[0]= int(robot[0])+int(step)
        elif int(robot[2])==1 and robot[1] < Y:
            robot[1]=int(robot[1])+int(step)
        elif int(robot[2])==2 and robot[0] > 1:
            robot[0]=int(robot[0])-int(step)
        elif int(robot[2])==3 and robot[1] > 1:
            robot[1]=int(robot[1])-int(step)
        if robot[0] > X or robot[1] > Y or robot[0] < 1 or robot[1] < 1: # ось тут
            break
    return robot
    


    

def dir(robot, dire):   # відповідає за напрямок робота
    if dire=="L":
        if robot[2]==3:
            robot[2]=0
            return robot
        else:
            robot[2]=int(robot[2])+1
            return robot
    if dire == "R":
        if robot[2] == 0:
            robot[2] = 3
        else:
            robot[2] = robot[2] - 1
        return robot

    
# def stuk(robot, X, Y):
#     if robot[0] >= X or robot[1] >= Y or robot[0] <= 0 or robot[1] <= 0:
#         return False
#     return True

    

    
C1 = 0  #проходження циклів , які мають пройти роботи
while C1 < C:
    for i in commands1:
        if i == "L":
            robot1 = dir(robot1, i)
        elif i == "R":
            robot1 = dir(robot1, i)
        else:
            robot1 = move(robot1, int(i), X, Y)
            count += 1

    for i in commands2:
        if i == "L":
            robot2 = dir(robot2, i)
        elif i == "R":
            robot2 = dir(robot2, i)
        else:
            print(robot1)
            robot2 = move(robot2, int(i), X, Y)
            count += 1 
            
    C1 += 1

print(count)

#тест
# 8 6 5
# 2 4 0
# 4 L 2 L
# 6 1 1
# 6 5 R

