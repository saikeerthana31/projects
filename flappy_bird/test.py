import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.6
JUMP_STRENGTH = -9
PIPE_GAP = 160
PIPE_SPEED = 3.5
PIPE_WIDTH = 70
BIRD_SIZE = 34
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Load images
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (BIRD_SIZE, BIRD_SIZE))
bg_img = pygame.image.load("background.jpeg")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
pipe_img = pygame.image.load("pipe.jpeg")
pipe_img = pygame.transform.scale(pipe_img, (PIPE_WIDTH, 400))

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_text(text, x, y):
    label = FONT.render(text, True, WHITE)
    screen.blit(label, (x, y))

class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.vel = 0
        self.angle = 0
    
    def jump(self):
        self.vel = JUMP_STRENGTH

    def move(self):
        self.vel += GRAVITY
        self.y += self.vel
        self.angle = max(-30, min(30, -self.vel * 2))

    def draw(self):
        rotated_bird = pygame.transform.rotate(bird_img, self.angle)
        screen.blit(rotated_bird, (self.x, self.y))

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 350)
    
    def move(self):
        self.x -= PIPE_SPEED

    def draw(self):
        screen.blit(pipe_img, (self.x, self.height - pipe_img.get_height()))
        screen.blit(pygame.transform.flip(pipe_img, False, True), (self.x, self.height + PIPE_GAP))

def check_collision(bird, pipes):
    for pipe in pipes:
        if (bird.x < pipe.x + PIPE_WIDTH and bird.x + BIRD_SIZE > pipe.x and 
            (bird.y < pipe.height or bird.y + BIRD_SIZE > pipe.height + PIPE_GAP)):
            return True
    return bird.y > HEIGHT or bird.y < 0

def game():
    bird = Bird()
    pipes = [Pipe(WIDTH + i * 200) for i in range(3)]
    score = 0
    running = True

    while running:
        screen.blit(bg_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()
        
        bird.move()
        bird.draw()

        for pipe in pipes:
            pipe.move()
            pipe.draw()
            if pipe.x < -PIPE_WIDTH:
                pipes.remove(pipe)
                pipes.append(Pipe(WIDTH))
                score += 1
        
        draw_text(f"Score: {score}", 10, 10)

        if check_collision(bird, pipes):
            return game_over(score)
        
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

def game_over(score):
    while True:
        screen.fill((0, 0, 0))
        draw_text("Game Over!", WIDTH // 2 - 70, HEIGHT // 3)
        draw_text(f"Final Score: {score}", WIDTH // 2 - 70, HEIGHT // 2)
        draw_text("Press SPACE to Restart", WIDTH // 2 - 110, HEIGHT // 1.5)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return game()

game()
