# Game Class

import pygame
import sys

pygame.init()

class Game:

  def __init__(self,slot,screen,tiles,tile_categories,sprites,mode,ui,maps,party):
    self.mode = mode
    self.slot = slot
    self.screen = screen
    self.tiles = tiles
    self.tile_categories = tile_categories
    self.sprites = sprites
    self.ui = ui
    self.maps = maps
    self.Party = party

  def run(self):
    running = True
    while running:
      # Check mode to see if we're rendering the map, a menu, or something else
      if self.mode == "overworld":
        # Blit the overworld contents
        self.blit_margins()
        
        # Event handling block
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
          elif event.type == pygame.MOUSEBUTTONUP:
            pass
          elif event.type == pygame.KEYUP:
            pass
            
        pygame.display.flip()

  def blit_margins(self):
    self.screen.blit(self.ui["u1"],(0,0))
    self.screen.blit(self.ui["u2"],(0,820-64))
    self.screen.blit(self.ui["u3"],(1280-64,0))
