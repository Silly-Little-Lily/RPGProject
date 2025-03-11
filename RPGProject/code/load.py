# Load Module

import pygame
import threading
import time

## Loading Necessary Components ##
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
loading = True
bar_width, bar_height, margin, load_cap, x, y = 750, 50, 6, 3, 380, 800
loaded_height, status = int(bar_height-(2*margin)), "Loading tiles..."
default_font = pygame.font.Font(None, 30)

class Load:
  
    def __init__(self, load_to, screen):
        global progress
        self.load_to = load_to
        self.screen = screen
        progress = 0

        width, height = screen.get_size()
        background_art = pygame.transform.scale(pygame.image.load("images/load_bg.jpg"), (width, height))
        background_rect = background_art.get_rect(topleft=(0,0))
  
    def run(self):
        if self.load_to == "startup":   # If "startup" is sent as a parameter, indcating game-launching loading
            loading_thread = threading.Thread(target=load_things)
            loading_thread.start()
        pygame.display.set_caption("RPG Game")
        screen.blit(background_art, background_rect)
        while loading:
            self.events()
            self.display(screen)
            pygame.display.flip()
        pygame.quit()
        return cc_assets
      
    def events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
              
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
    global loading, progress, status, tiles, sprites
    ## Loading Tiles ##

    progress += 1
    status = "Loading sprites"
    ## Loading Sprites ##
    
    progress += 1
    status = "Last details..."
    ## Ending ##
    time.sleep(3)
    progress += 1
  
    status = "Finishing..."
    print(f"Done! Ending progress: {progress}")
    loading = False

if __name__ == "__main__":
  screen = pygame.display.set_mode((1510,930))
  loader = Load("startup",screen)
  loader.run()
