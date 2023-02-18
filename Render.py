import pygame
pygame.init()


GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font_score = pygame.font.SysFont('Calibri', 25, True, False)
font_game_over = pygame.font.SysFont('Calibri', 65, True, False)

def renderMainMenu():
    idk = True

def renderGame(game, screen):
    if not game.state == "gameover":
        renderField(game, screen)
        renderFigure(game, screen)
        renderScore(game, screen)
    else:
        renderGameOver(screen)

    pygame.display.flip()


def renderField(game, screen):
    screen.fill(BLACK)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, WHITE, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] != 0:
                pygame.draw.rect(screen, game.field[i][j],
                            [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

def renderFigure(game, screen):
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, game.figure.color,
                                [game.x + game.zoom * (j + game.figure.x) + 1,
                                game.y + game.zoom * (i + game.figure.y) + 1,
                                game.zoom - 2, game.zoom - 2])
                    
def renderScore(game, screen):
    scoreText = font_score.render("Score: " + str(game.score), True, WHITE)
    screen.blit(scoreText, [0, 0])

def renderGameOver(screen):
    text_game_over = font_game_over.render("Game Over", True, (255, 255, 255))
    text_new_game = font_game_over.render("Press ESC", True, (125, 125, 125))
    screen.blit(text_game_over, [20, 200])
    screen.blit(text_new_game, [25, 265])



