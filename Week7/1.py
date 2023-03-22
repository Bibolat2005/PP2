import pygame
pygame.init()
clock = pygame.time.Clock()
W, H = 800, 800
x = W//2
y = H//2
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))
mickey = pygame.image.load(r"C:\Users\Биболат\Desktop\PP2\week 7\b.png")
leftHand = pygame.image.load(r"C:\Users\Биболат\Desktop\PP2\week 7\second.png")
rightHand = pygame.image.load(r"C:\Users\Биболат\Desktop\PP2\week 7\minute.png")
mickeyRect = mickey.get_rect()
def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = topleft).center)
    surf.blit(rotated_image, new_rect)
left_angle = 0
right_angle = 0
while True:
    sc.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    left_angle -= 0.06
    right_angle -= 0.000006
    sc.fill(WHITE)
    sc.blit(mickey, (x, y))
    sc.blit(mickey, mickeyRect)
    blitRotateCenter(sc, rightHand, (x,y), right_angle)
    blitRotateCenter(sc, leftHand, (x,y), left_angle) 
    pygame.display.update()