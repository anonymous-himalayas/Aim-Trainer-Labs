import pygame
import math
import random
import time
from Targets import Target


WIDTH, HEIGHT = 800, 600
TARGET_TIME = 600
TARGET_PADDING = 30
TOTAL_LIVES = 3

def draw_board(win, targets):
    win.fill((0,0,0))
    for target in targets:
        target.draw_target(win)
    

def draw_top(window, current_time, score, misses):
    pygame.draw.rect(window, 'grey', (0,0, WIDTH, 50))
    time_label = pygame.font.SysFont('arial', 24).render(f'Time: {int(current_time // 60):02d}:{int(round(current_time % 60, 1))}.{math.floor(int(current_time * 1000 % 1000) / 100)}', 1, 'black')
    speed = round(score / current_time, 1)
    speed_label = pygame.font.SysFont('arial', 24).render(f'Speed: {speed} t/s', 1, 'black')
    lives_label = pygame.font.SysFont('arial', 24).render(f'Lives: {TOTAL_LIVES - misses}', 1, 'black')
    hits_label = pygame.font.SysFont('arial', 24).render(f'Hits: {score}', 1, 'black')
    window.blit(time_label, (5, 5))
    window.blit(speed_label, (200, 5))
    window.blit(hits_label, (450, 5))
    window.blit(lives_label, (650, 5))

def middle(window):
    return WIDTH / 2 - window.get_width() / 2

def end_screen(window, current_time, score, clicks):
    if clicks == 0:
        clicks = 1 
    window.fill((0,0,0))
    time_label = pygame.font.SysFont('arial', 24).render(f'Time: {int(current_time // 60):02d}:{int(round(current_time % 60, 1))}.{math.floor(int(current_time * 1000 % 1000) / 100)}', 1, 'red')
    speed = round(score / current_time, 1)
    speed_label = pygame.font.SysFont('arial', 24).render(f'Speed: {speed} t/s', 1, 'red')
    acc = round(score / clicks * 100, 1)
    acc_label = pygame.font.SysFont('arial', 24).render(f'Accuracy: {acc}%', 1, 'red')
    hits_label = pygame.font.SysFont('arial', 24).render(f'Hits: {score}', 1, 'red')
    game_over = pygame.font.SysFont('arial', 40).render(f'GAME OVER', 1, 'red')
    window.blit(game_over, (middle(game_over), 100))
    window.blit(time_label, (middle(time_label), 200))
    window.blit(speed_label, (middle(speed_label), 300))
    window.blit(hits_label, (middle(hits_label), 400))
    window.blit(acc_label, (middle(acc_label), 500))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                return

def main():
    pygame.init()
    window = pygame.display.set_mode([WIDTH, HEIGHT])
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
        current_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.USEREVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + 50, HEIGHT - TARGET_PADDING)
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
            
        
        if misses >= TOTAL_LIVES:
            end_screen(window, current_time, target_points, clicks)
            run = False
        
    
        draw_board(window, targets)
        draw_top(window, current_time, target_points, misses) 
        pygame.display.update()

    pygame.quit()
    


if __name__ == '__main__':
    main()
