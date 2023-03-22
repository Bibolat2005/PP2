import pygame

screen = pygame.display.set_mode((600,300))
clock=pygame.time.Clock()
pygame.display.set_caption("Circle")
circle_speed=20
circle_x=300
circle_y=150

while True:
    screen.fill("white")
    circle = pygame.draw.circle(screen,("red"),(circle_x,circle_y),25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and circle_x > 50:
        circle_x -= circle_speed
    
    elif keys[pygame.K_RIGHT] and circle_x < 550:
        circle_x += circle_speed
    
    elif keys[pygame.K_DOWN] and circle_y < 260:
        circle_y += circle_speed
    
    elif keys[pygame.K_UP] and circle_y > 30:
        circle_y -= circle_speed
    clock.tick(50)
    pygame.display.update()