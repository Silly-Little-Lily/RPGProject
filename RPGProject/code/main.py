import pygame
import start

pygame.init()

# Retrieving and reading global save data
save_data_file = open("data/save/global_data.txt")
save_data_lines = save_data_file.read()
save_data_list = save_data_lines.strip().split(",")

width = int(save_data_list[0].strip())
height = int(save_data_list[1].strip())

# Setting up the screen and system
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RPG Game")

start.run_start_menu(screen)
