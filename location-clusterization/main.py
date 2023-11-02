import pandas as pd
from location import Location
from cluster import LocationClusterCalculator

def read_file(file_path):
    locations = []
    try:
        df = pd.read_excel(file_path, sheet_name="Location")
        for _, row in df.iterrows():
            name = row["Location"]
            latitude = row["Lattitude"]
            longitude = row["Longitude"]
            location = Location(name, latitude, longitude)
            locations.append(location)
    except Exception as e:
        print(f"Error reading the Excel file: {str(e)}")
    return locations

def main():
    file_path = "F:/L&C/location-clusterization/Locations.xlsx"
    locations = read_file(file_path)
    location_cluster = LocationClusterCalculator(locations)

if __name__ == "__main__":
    main()