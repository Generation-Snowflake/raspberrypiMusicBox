import pygame
import time 
import os

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('2.SmartHeart15Sec.mp3')
pygame.mixer.music.queue('2.SmartHeart15Sec.mp3')
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.play()

