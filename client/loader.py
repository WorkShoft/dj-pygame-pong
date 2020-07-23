import pygame
import constants

from game import Game
from menu import Menu
from scene_manager import SceneManager


def load_screen():
    pygame.init()

    screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

    return screen


def load_scenes(screen):
    menu = Menu(screen)
    game = Game(screen)

    scenes = {
        "menu": menu,
        "game": game,
    }

    return scenes


def load_scene_manager(scenes, initial=None):
    scene_manager = SceneManager(scenes)

    for scene in scenes.values():
        scene.scene_manager = scene_manager

    if initial:
        scene_manager.switch_scene(initial)

    return scene_manager
