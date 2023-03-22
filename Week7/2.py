import pygame
import os
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('My music playlist')
pygame.mixer.init()
running=True
player=r'C:\Users\Биболат\Desktop\PP2\music_lib'
files=os.listdir(player)
files=[os.path.join(player,file) for file in files if file.endswith('.mp3')]
label=pygame.font.Font('font/Roboto-Black.ttf',40)
lose_label=label.render('Enjoyable musics',False,(193,196,0))
i=0
pygame.mixer.music.load(files[i])
def playing_mus():
    pygame.mixer.music.play()
def stop_mus():
    pygame.mixer.music.pause()
def next_mus():
    global i
    i+=1
    if i>=len(files):
        i=0
    pygame.mixer.music.load(files[i])
    pygame.mixer.music.play()
def previous_mus():
    global i
    i-=1
    if i<0:
        i=len(files)-1
    pygame.mixer.music.load(files[i])
    pygame.mixer.music.play()
while running:
    screen.fill((0,0,255))
    screen.blit(lose_label,(180,250))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playing_mus()
            elif event.key == pygame.K_DOWN:
                stop_mus()
            elif event.key == pygame.K_RIGHT:
                next_mus()
            elif event.key == pygame.K_LEFT:
                previous_mus()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

