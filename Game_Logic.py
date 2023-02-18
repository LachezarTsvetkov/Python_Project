from Shapes import Figure

class Tetris:
    def __init__(self, height, width, level):
        self.idk = 0
        self.height = height
        self.width = width

        self.x = 100
        self.y = 60
        self.score = 0

        self.level = level
        self.state = "start"
        self.field = []
        self.zoom = 20
        self.figure = None  

        #Creating the map
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)


    def newFigure(self):
        self.figure = Figure(3, 0)


    def collides(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if self.height - 1 < i + self.figure.y:
                            return True
                    if j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] != 0:
                        return True
        return False
    

    #Freeze the shape once it hits something
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()

        self.newFigure()
        
        #if the new block instantly intersects, end the game
        if self.collides():
            self.state = "gameover"


    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0

            #check for empty spaces
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1

            #if there's are no empty spaces, break
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
                
        self.score += lines ** 2

    def go_space(self):
        while not self.collides():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()


    def go_down(self):
        self.figure.y += 1
        if self.collides():
            self.figure.y -= 1
            self.freeze()


    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.collides():
            self.figure.x = old_x


    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.collides():
            self.figure.rotation = old_rotation
