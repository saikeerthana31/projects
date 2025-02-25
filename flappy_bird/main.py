import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_GAP = 150
PIPE_SPEED = 4

# Colors
WHITE = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load images
bird_img = pygame.image.load("bird.png")
bg_img = pygame.image.load("background.jpeg")
pipe_img = pygame.image.load("pipe.jpeg")

class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.vel = 0
    
    def jump(self):
        self.vel = JUMP_STRENGTH

    def move(self):
        self.vel += GRAVITY
        self.y += self.vel

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
    
    def move(self):
        self.x -= PIPE_SPEED

    def draw(self):
        screen.blit(pipe_img, (self.x, self.height - 500))
        screen.blit(pygame.transform.flip(pipe_img, False, True), (self.x, self.height + PIPE_GAP))

def check_collision(bird, pipes):
    for pipe in pipes:
        if (bird.x < pipe.x + 50 and bird.x + 30 > pipe.x and 
            (bird.y < pipe.height or bird.y + 30 > pipe.height + PIPE_GAP)):
            return True
    return bird.y > HEIGHT or bird.y < 0

# Game loop
bird = Bird()
pipes = [Pipe(WIDTH + i * 200) for i in range(3)]
running = True
while running:
    screen.blit(bg_img, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.jump()
    
    bird.move()
    bird.draw()

    # Pipe movement
    for pipe in pipes:
        pipe.move()
        pipe.draw()
        if pipe.x < -50:
            pipes.remove(pipe)
            pipes.append(Pipe(WIDTH))

    if check_collision(bird, pipes):
        running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
