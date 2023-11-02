class Location:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = self._convert_coordinate(latitude)
        self.longitude = self._convert_coordinate(longitude)

    @staticmethod
    def _convert_coordinate(coordinate_str):
        try:
            parts = coordinate_str.split('°')
            if len(parts) == 2:
                degrees, rest = parts[0], parts[1]
                minutes = rest.split("'")[0]
                decimal_degrees = round(float(degrees) + (float(minutes) / 60.0), 4)
                if 'S' in coordinate_str:
                    decimal_degrees = -decimal_degrees
                return decimal_degrees
        except Exception as ex:
            print("Error converting coordinate string: {ex}")
        return float('nan')
