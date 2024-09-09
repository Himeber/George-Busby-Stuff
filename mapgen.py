import random
import time
class Room:
    def __init__(self):
        #weeeee
        self.coords = 0,0
        self.rng = random.random()
        self.enemy = 0
        self.chest = 0
        self.stairs = 0
        self.rest = 0
        if self.rng > 0.25:
            self.enemy = 1
        self.rng = random.random()
        if self.rng > 0.5:
            self.chest = 1
        self.rng = random.random()
        if self.rng > 0.9:
            self.stairs = 1
        if self.stairs == 0 and self.enemy == 0 and self.chest == 0:
            self.rest = 1
    def __repr__(self):
        return("Room at " + str(self.coords))
def generateroom(coords):
    room = Room()
    room.coords = coords
    return room
def cs():
    print('\033c')
coords = 0,0
rooms = []
print(coords)
roomcoords = coords
print(roomcoords)
coords = 1,0
print(coords)
print(roomcoords)
counter = 0
yes = 0
while True:
    roompos = None
    room = None
    for i in rooms:
        if i[1].coords == coords:
            room = i
            roompos = counter
        counter += 1
    if not room:
        room = generateroom(coords)
        rooms.append([yes,room])
        roompos = -1
    time.sleep(0.1)
    cs()
    yes += 1
    coords = coords[0]+random.randint(-1,1), coords[1] + random.randint(-1,1)
    if coords[0] < 0:
        coords = 0, coords[1]
    if coords[1] < 0:
        coords = coords[0], 0
    mappy = [[]]
    for i in rooms:
        room = i[1]
        appended = False
        while not appended:
            try:
                mappy[room.coords[0]][room.coords[1]] = room
                appended = True
            except:
                mappy.append([])
                for i in mappy:
                    i.append(None)
    mapstr = ""
    ycounter = 0
    for i in mappy:
        xcounter = 0
        linestr = ""
        for j in i:
            right = False
            left = False
            up = False
            down = False
            if j != None:
                if xcounter != 0:
                    if i[xcounter-1] != None:
                        left = True
                try:
                    if i[xcounter+1] != None:
                        right = True
                except:
                    pass
                try:
                    if ycounter != 0:
                        if mappy[ycounter-1][xcounter] != None:
                            up = True
                except:
                    pass
                try:
                    if mappy[ycounter+1][xcounter] != None:
                        down = True
                except:
                    pass
                if right and left and up and down:
                    linestr += "  "
                elif right and left and down and not up:
                    linestr += "﹊ "
                elif right and left and not down and up:
                    linestr += "﹎ "
                elif right and not left and down and up:
                    linestr += "| "
                elif not right and left and down and up:
                    linestr += " |"
                elif right and left and not down and not up:
                    linestr += ""
                elif right and not left and not down and up:
                    linestr += "|_ "
                elif not right and left and not down and up:
                    linestr += "_|"
            else:
                linestr += "  "
            xcounter += 1
        linestr += "\n"
        mapstr += linestr
        ycounter += 1
    print(mapstr)