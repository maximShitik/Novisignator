

class NavigationService():
    def __init__(self, navigation_repo, redis_client):
        self.navigation_repo = navigation_repo
        self.redis_client = redis_client

    def get_route(self, scan_point_id, store_id): pass