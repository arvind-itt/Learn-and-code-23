import math
class LocationClusterCalculator:
    def __init__(self, locations):
        self.locations = locations
        self.latitude_radius = 10.0  # Specify the latitude radius in degrees
        clusters = self._create_clusters(self.locations, self.latitude_radius)
        if clusters:
            self._display_result(clusters)
        else:
            print("No clusters found.")

    def _display_result(self, clusters):
        cluster_number = 1
        for cluster in clusters:
            print(f"\nCluster {cluster_number}:")
            for location in cluster:
                print(f"{location.name} - Latitude: {location.latitude}, Longitude: {location.longitude}")
            cluster_number += 1

    @staticmethod
    def calculate_haversine_distance(location_one, location_two):
        earth_radius = 6371  # Earth's radius in kilometers
        lat1 = math.radians(location_one.latitude)
        lon1 = math.radians(location_one.longitude)
        lat2 = math.radians(location_two.latitude)
        lon2 = math.radians(location_two.longitude)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = earth_radius * c
        return distance

    def _create_clusters(self, locations, latitude_radius):
        clusters = []
        for location in locations:
            clustered = False
            for cluster in clusters:
                if all(abs(location.latitude - cluster_location.latitude) <= latitude_radius for cluster_location in cluster):
                    cluster.append(location)
                    clustered = True
                    break
            if not clustered:
                clusters.append([location])
        return clusters