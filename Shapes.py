import random

class Tetromino:
    def __init__(self, color, coords):
        self.coords = coords
        self.color = color

class Figure:
    x = 0
    y = 0

    figures = [
        Tetromino((49, 69, 240), [[1, 2, 5, 9], [0, 4, 5, 6], [2, 6, 9, 10], [1, 2, 3, 7]]), #Blue
        Tetromino((255, 185, 73), [[2, 4, 5, 6], [1, 5, 9, 10], [0, 1, 2, 4], [1, 2, 6, 10]]), #Orange
        Tetromino((95, 240, 255), [[4, 5, 6, 7], [1, 5, 9, 13]]), #Cyan
        Tetromino((51, 255, 79), [[2, 3, 5, 6], [1, 5, 6, 10]]), #Lime
        Tetromino((249, 28, 28), [[1, 2, 6, 7], [2, 5, 6, 9]]), #Red
        Tetromino((172, 26, 255), [[1, 4, 5, 6], [1, 5, 6, 9], [4, 5, 6, 9], [1, 4, 5, 9]]), #Purple
        Tetromino((238, 253, 30), [[5, 6, 9, 10]]), #Yellow
    ]


    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.type = random.randint(0, len(self.figures) - 1)
        self.color = self.figures[self.type].color
        self.rotation = 0

    def image(self):
        return self.figures[self.type].coords[self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type].coords)