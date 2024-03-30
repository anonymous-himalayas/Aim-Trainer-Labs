
import pygame
import random
import time
from Targets import Target


WIDTH, HEIGHT = 800, 600
TARGET_TIME = 600
TARGET_PADDING = 30


def draw_board(win, targets):
    win.fill((0,0,0))
    for target in targets:
        target.draw_target(win)
    
    pygame.display.update()

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Aim Trainer')

    run = True
    targets = []
    clock = pygame.time.Clock()

    target_points = 0
    clicks = 0
    misses = 0
    start_time = time.time()

    pygame.time.set_timer(pygame.USEREVENT, TARGET_TIME)

    while run:
        clock.tick(60)
        click = False
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.USEREVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1
            
            if click and target.collide(*mouse_position):
                targets.remove(target)
                target_points += 1

        draw_board(window, targets)

    pygame.quit()
    


if __name__ == '__main__':
    main()
