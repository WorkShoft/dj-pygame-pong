import json

import pygame

import websocket_client


class SceneManager:
    def __init__(self, scenes):
        self.scenes = scenes
        self.current_scene = None
        self.clock = pygame.time.Clock()

    def run(self):
        if self.current_scene:
            self.current_scene.update()
            self.current_scene.render()
            self.clock.tick(120)

    def switch_scene(self, scene, **scene_data):
        if scene in self.scenes:
            self.current_scene = self.scenes[scene]

        if scene_data:
            self.current_scene.set_data(scene_data)
