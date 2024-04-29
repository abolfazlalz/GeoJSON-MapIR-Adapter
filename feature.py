import json


class Feature:
    def __init__(self, file_name: str):
        with open(file_name, 'r', encoding='utf-8') as dataset_file:
            dataset = json.loads(dataset_file.read())
        if 'features' not in dataset:
            self.features = []
        self.features = dataset['features']

    def properties(self, i: int) -> dict[str, any]:
        """
        get properties of a feature value
        """
        feature = self.features[i]

        if 'properties' not in feature:
            return {}
        return feature['properties']

    def center_point(self, i: int):
        feature = self.features[i]
        if 'geometry' not in feature:
            return 0
        coordinates: list = feature['geometry']['coordinates'][0]
        longitude = list(map(lambda coord: coord[0], coordinates))
        latitude = list(map(lambda coord: coord[1], coordinates))
        return sum(longitude) / len(longitude), sum(latitude) / len(latitude)

    def __len__(self):
        return len(self.features)
