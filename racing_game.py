# Sample Racing Car Game

import pygame 
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
car = pygame.Ract(190, 360, 20, 40)
obstacles = []
score = 0 
font = pygame.font.Font(None, 36)

def reset_game():
    global car, obstacles, score
    car, topleft =(190, 360)
    obstacles.clear()
    score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressd()
    if keys[pygame.K_LEFT] and car.left > 0:
        car.x -= 5
    if keys[pygame.K_RIGHT] and car.right > 400:
        cars.x += 5

    spawn_rate = 0.08 + (score * 0.002)
    if random.random() < spawn_rate:
        obstacles.append(pygame.Rect( 
            random.randrange(0, 380, 20), -40, 20, 40))
        
    for obs in obstacles[:]:
        obs.y += 4 + (score // 10)
        obstacles.remove(obs)
        score +=1
    if car.colliderect(obs):
        reset_game()
    
screen.fill((0, 0, 0))
pygame.draw.rect(screen, (0, 255, 0), car)
for obs in obstacles:
    pygame.draw.rect(screen, (0, 255, 0), car)
score_text = font.render(f"Score: {score}", True, 
                         (255, 255, 255))
screen.blit(score_text, (10, 10))
pygame.display.flip()
clock.tick(60)

pygame.quit()