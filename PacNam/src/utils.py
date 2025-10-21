import pygame

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def draw_game_over(screen, height, size, life):
    font = pygame.font.SysFont('didot.ttc', 200)
    img  = font.render('Game Over', True, GREEN if life else RED )
    screen.blit(img, (10, (height + 1.5) * size))

    screen_width, screen_height = screen.get_width(), screen.get_height()
    img_width, img_height = img.get_width(), img.get_height()
    x_position = (screen_width - img_width) / 2
    y_position = (screen_height - img_height) / 2
    screen.blit(img, (x_position, y_position))


def draw_score(screen, height, size, score):
    font = pygame.font.SysFont('didot.ttc', 50)
    img  = font.render('{:0>9}'.format(score), True, YELLOW)
    screen.blit(img, (10, (2 * height + 1.5) * size))

def draw_life(screen, height, width, size, life):
    life_image = pygame.image.load("images/pngegg.png")
    life_image = pygame.transform.scale(life_image, (int(size * 0.9), int(size * 0.9)))
    for x in range(2 * width, 2 * width - life, -1):
        screen.blit(life_image, (int(x * size), int((2 * height + 1.5) * size)))


def draw_data(screen, height, width, size, pacnam):
    draw_score(screen, height, size, pacnam.score)
    draw_life(screen, height, width, size, pacnam.life)

def check_event(player, ghost):
    if player.power_up:
        player.score += 100
        ghost.kill()
    else :
        player.score -= 150
        player.kill()
    return player.life != 0

def check_hitbox(player, ghosts):
    player_pos = (int(player.pos.x / player.size), int(player.pos.y /player.size))
    for elt in ghosts:
        if (elt.real_pos == player_pos):
            return check_event(player, elt)
    return True
