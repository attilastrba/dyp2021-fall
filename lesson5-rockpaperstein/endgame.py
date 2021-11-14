import pygame
from time import sleep
import random
from pygame.locals import *


class endgame:

  def __init__(self):
    pygame.init()
    self.options = ["Schere","Stein","Papier"]
    self.screen = pygame.display.set_mode((600, 370))
    self.createBackground()
    pygame.display.update()
    print ("\n" + 30 * "*")
    print ("Willkommen bei Endgame (How it should have ended)\n")
  
  def createBackground(self):
    self.screen.fill((255,255,255))
    pygame.display.set_caption('Endgame - How it should have ended!')
    imageBackground = pygame.image.load("background.png")
    self.screen.blit(imageBackground, (0, 0))
    imageThanos = pygame.image.load("thanos.png")
    self.screen.blit(imageThanos, (340, 120))    
    imageIronman = pygame.image.load("ironman.png")
    self.screen.blit(imageIronman, (0, 155))

  def makeChoice(self, choice=None):
    print ("\nDu spielst Ironman. Wähle aus: ")
    print ("Schere")
    print ("Stein")
    print ("Papier")
    while choice not in self.options:
      choice = input ("-> ")
      if choice not in self.options:
        print ("Du hast einen ungültigen Wert eingegeben. Bitte wiederholen.")
    print ("")
    self.choice = choice
    return self.choice

  def startBattle(self, choice):
    handIndexThanos = 0
    handIndexIronman = 1
    if choice not in self.options:
      choice = self.options[random.randint(0,2)]
      print ("Warnung, du hast beim Aufruf von startBattle keine gültige Auwahl mitgegeben. Es wird eine zufällige Auswahl getroffen.")
    for loopCounter in range(0,14):
      imageHandThanosStone = pygame.image.load("handThanos"+self.options[handIndexThanos]+".png")
      self.screen.blit(imageHandThanosStone, (280, 150))
      imageHandIronmanPaper = pygame.image.load("handIronman"+self.options[handIndexIronman]+".png")
      self.screen.blit(imageHandIronmanPaper, (100, 110))
      pygame.display.update()
      handIndexIronman += 1
      if handIndexIronman > 2:
        handIndexIronman = 0
      handIndexThanos += 1
      if handIndexThanos > 2:
        handIndexThanos = 0
      sleep(0.15)
    thanosResult = self.options[random.randint(0,2)]
    imageHandThanosStone = pygame.image.load("handThanos"+thanosResult+".png")
    self.screen.blit(imageHandThanosStone, (280, 150))
    imageHandIronmanPaper = pygame.image.load("handIronman"+choice+".png")
    self.screen.blit(imageHandIronmanPaper, (100, 110))
    pygame.display.update()
    return thanosResult