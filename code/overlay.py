import pygame
from settings import *

class Overlay:
    def __init__(self, Player):
        # general set up
        self.display_serface = pygame.display.get_surface()
        self.player = Player

        # imports
        overlay_path = '../graphics/overlay/'
        self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in Player.tools}
        self.seeds_surf = {seed: pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in Player.seeds}
        print(self.tools_surf)
        print(self.seeds_surf)

    def display(self):

        # tools
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
        self.display_serface.blit(tool_surf, tool_rect)

        # seeds
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom = OVERLAY_POSITIONS['seed'])
        self.display_serface.blit(seed_surf, seed_rect)