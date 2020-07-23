import loader


if __name__ == "__main__":
    screen = loader.load_screen()
    scenes = loader.load_scenes(screen)
    pong_scene_manager = loader.load_scene_manager(scenes, initial="menu")

    while True:
        pong_scene_manager.run()
