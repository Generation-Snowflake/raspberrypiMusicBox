import pygame

pygame.init()

x = pygame.mixer.Sound("~/raspberrypiMusicBox/playlist/3.MEOMe-O15Sec.mp3")
x = pygame.mixer.music.load("/playlist/3.MEOMe-O15Sec.mp3")

x.play()
