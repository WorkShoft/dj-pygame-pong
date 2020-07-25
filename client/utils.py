import os

def get_resource(resource_name):
        dirname = os.path.dirname(__file__)
        return os.path.join(dirname, f"resources/{resource_name}")
