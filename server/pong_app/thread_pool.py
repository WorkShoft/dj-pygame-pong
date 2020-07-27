import threading

class ThreadPool:
    """
    threads: {"my_game": {"thread": threading.Thread(), "player_count": 1, }, ...}
    """
    
    threads = {}

    @classmethod
    def add_game(cls, game_name, consumer_instance):
        cls.threads[game_name] = {"thread": threading.Thread(target=consumer_instance.propagate_state), "player_count": 0, }
        thread = cls.threads[game_name]["thread"]
        thread.daemon = True
        thread.start()
