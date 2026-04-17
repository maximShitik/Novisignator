

class NavigationService():
    def __init__(self, navigation_repo, redis_client):
        self.navigation_repo = navigation_repo
        self.redis_client = redis_client

    def get_route(self, scan_point_id, store_id):

        cache_key = f"nav:{scan_point_id}:{store_id}"
    
        try:    
            cached = self.redis_client.get(cache_key)
            if cached:
                return cached
            
            navigation_route = self.navigation_repo.get_navigation_route(scan_point_id, store_id)
            self.redis_client.set(cache_key,navigation_route,ex=2592000)

            return navigation_route

        except Exception as e:
            raise Exception(f"NavigationService.get_route failed: {e}")
        
    def warm_cache(self):
        try:
            all_routes = self.navigation_repo.get_all_routes()

            for route in all_routes:

                store_id = route[0]
                scan_point_id = route[1]
                route_path_d = route[2]

                cache_key = f"nav:{scan_point_id}:{store_id}"
                self.redis_client.set(cache_key,route_path_d,ex=2592000)
        except Exception as e:
            raise Exception(f"NavigationService.warm_cache failed: {e}")