# Load Module

import pygame
import threading
import time
import sys
import game

pygame.init()

## Loading Necessary Components ##
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
loading = True
bar_width, bar_height, margin, load_cap, x, y = 750, 50, 6, 3, 380, 800
loaded_height, status = int(bar_height-(2*margin)), "Loading tiles..."
default_font = pygame.font.Font(None, 30)

# Initializing empty dictionaries
tiles = {}
sprites = {}
tile_categories = {}
ui = {}
maps = {}

class Load:
  
    def __init__(self, load_to, screen):
        global progress
        self.load_to = load_to
        self.screen = screen
        progress = 0

        # Retrieving screen dimensions and blitting scaled background
        width, height = screen.get_size()
        self.background_art = pygame.transform.scale(pygame.image.load("RPGProject/images/loading_bg.jpg"), (width, height))
        self.background_rect = self.background_art.get_rect(topleft=(0,0))
  
    def run(self):
        if self.load_to == "startup":   # If "startup" is sent as a parameter, indcating game-launching loading
            
            # Set up the load_things function to run parallel
            loading_thread = threading.Thread(target=load_things)
            loading_thread.start()
          
        pygame.display.set_caption("RPG Game")
        screen.blit(self.background_art, self.background_rect)
      
        while loading:
            self.events()
            self.display(screen)
            pygame.display.flip()
          
        # Start the game once the loading is done
        loaded_game = game.Game(0,screen,tiles,tile_categories,sprites,"overworld",ui, maps)
        loaded_game.run()
        
      
    def events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
              
    def display(self, screen):
        loaded_width = int(((progress/load_cap)*bar_width)-(2*margin))
        outline_bar = pygame.Rect(x, y, bar_width, bar_height)
        progress_bar = pygame.Rect(x+margin, y+margin, loaded_width, loaded_height)
        pygame.draw.rect(screen, BLACK, outline_bar)
        pygame.draw.rect(screen,WHITE, progress_bar)
        note = default_font.render(status, True, BLACK)
        note_rect = note.get_rect(midtop = (755,865))
        text_bar = pygame.Rect(x + 200, y + 65, bar_width - 400, 20)
        pygame.draw.rect(screen, WHITE, text_bar)
        screen.blit(note, note_rect)
      
    def update(self):
        pygame.display.flip()


def load_things():
    global loading, progress, status, tiles, sprites, tile_categories, ui, maps
    
    with open("RPGProject/images/base_tiles_directory.txt","r") as base_tile_file:
      base_tile_all_text = base_tile_file.readlines()
      for line in base_tile_all_text:
        parts = line.split(",")
        id = int(parts[0].strip())
        animation_length = int(parts[1].strip())
        category = int(parts[2].strip())
        tiles[id] = []
        for i in range(animation_length):
          i += 1
          img = pygame.image.load(f"RPGProject/images/{id}-{i}.jpg")
          tiles[id].append(pygame.transform.scale(img,(64,64)))
        tile_categories[id] = category
          
    progress += 1
    status = "Loading UI components..."
    with open("RPGProject/images/image-directory.txt","r") as file:
      image_file_text = file.readlines()
      for line in image_file_text:
        parts = line.split(",")
        name = parts[0]
        key_name = parts[1]
        height, width = int(parts[2]), int(parts[3])

        img = pygame.image.load(f"RPGProject/images/{name}.jpg")
        ui[key_name] = pygame.transform.scale(img,(height,width))

    progress += 1

    status = "Loading maps..."
    with open(RPGProject/save/static/maps/map_directory) as file:
      map_file_text = file.readlines()
      for line in map_file_text:
        parts = line.split(",")
        map_id = int(parts[1])
        map_file_location = f"RPGProject/save/static/maps/{parts[0]}.txt"
    progress += 1
    time.sleep(1) # Looks cleaner when the screen has a moment to show 100% progress
    loading = False

if __name__ == "__main__":
  screen = pygame.display.set_mode((1510,930))
  loader = Load("startup",screen)
  loader.run()
