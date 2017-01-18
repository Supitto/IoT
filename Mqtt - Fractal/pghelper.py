import PIL.Image
import pygame

screen = pygame.display.set_mode((200,200))

def updateImage(imagem):
    pygame.event.pump()
    print("foi")
    output = imagem.convert("RGBA").tobytes("raw", "RGBA")
    res = pygame.image.fromstring(output,(200,200),'RGBA')
    screen.blit(res,(0,0))
    pygame.display.flip()
