from pygame import mixer
import pygame
from time import sleep

sound_test = input("a, b, c, or d: ")
mixer.init()


if sound_test == 'a':
    channel_1 = mixer.Channel(1)
    laser = mixer.Sound("sounds/fire_laser.wav")
    channel_1.play(laser)
    sleep(5)

