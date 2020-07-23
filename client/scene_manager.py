class SceneManager:
    def __init__(self, scenes):
        self.scenes = scenes
        self.current_scene = None

    def run(self):
        if self.current_scene:
            self.current_scene.update()
            self.current_scene.render()

    def switch_scene(self, scene):
        if scene in self.scenes:
            self.current_scene = self.scenes[scene]
