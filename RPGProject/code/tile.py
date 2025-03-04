# Tile Class
# (only meant to be used as a parent class)
import pygame
pygame.init()

class Tile:

  def __init__(self, Id, Images):
    self.Id = Id
    if len(Images) == 1:
      self.Images = Images*8
    elif len(Images) == 2:
      self.Images = [x for x in Images for i in range(4)]
    elif len(Images) == 4:
      self.Images = [x for x in Images for i in range(4)]
    else:
      self.Images = Images


def Default():
  return Tile(1,[None])
