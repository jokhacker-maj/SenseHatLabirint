from sense_hat import SenseHat
import maze
sense = SenseHat()
coordinate = [0,0]


def draw(table, color):
    for y in range(0, 8):
        for x in range(0, 8):
            if x:
                sense.set_pixel(x, y, 255, 0, 0) ## barvo bo treba dodat
                
def move(position, table):
    sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    x=round(x, 0)
    y=round(y, 0)
    x1 = position[0]
    y1 = position[1]
    if x != 0 and y !=0 and acceleration['x'] >= acceleration['y']:
        x = x + x1
        y = y1
    elif x != 0 and y !=0 and acceleration['x'] < acceleration['y']:
        y = y +y1
        x = x1
    else:
        x = x + x1
        y = y +y1
    if table[x, y]:
        return position
    elif x<0 or x>7 or y<0 or y>7:
        return position
    else:
        position = [x, y]
        return position


def main():
    table =  maze.generate_maze
    coordinate = [0,0]
