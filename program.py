import json


class Geo:
    """
    Update Geo class
    """

    __result: dict

    def __init__(self):
        self.__result = {}

    def __check_province_name(self, province_name: str):
        if province_name in self.__result:
            return
        self.__result[province_name] = {
            'coordinates': [],
            'name':  province_name,
            'cities': []
        }

    def append(self, province_name: str, city):
        """
        Add new city
        """
        self.__check_province_name(province_name)
        self.__result[province_name]['cities'].append(city)

    def result(self) -> dict:
        """
        Return final and result value
        """
        return self.__result

    def save(self, file_name: str):
        """
        Save final result from geo
        """

        j = json.dumps(self.__result)
        with open(file_name, 'w', encoding='utf8') as f:
            f.write(j)


def open_features(file_name: str):
    """
    open_features
    open geojson file and give features value
    """
    with open(file_name, 'r', encoding='utf8') as dataset_file:
        dataset = json.loads(dataset_file.read())
    if 'features' not in dataset:
        return []
    return dataset['features']


def feature_properties(feature: any) -> dict[str, any]:
    """
    get properties of a feature value
    """
    if 'properties' not in feature:
        return {}
    return feature['properties']


def main():
    """
    main program
    """
    province_features = open_features('./dataset_province.geojson')
    cities_features = open_features('./dataset_cities.geojson')

    print('province len:', len(province_features))
    print('cities len:', len(cities_features))

    province = [{}]
    cities = []
    result = Geo()

    for feature in cities_features:
        props = feature_properties(feature)
        result.append(props['province'], {
            'coordinates': props['point']['coordinates']
        })

        cities.append({
            'name': props['city'],
            'longitude': props['point']['coordinates'][0],
            'latitude': props['point']['coordinates'][1],
        })

    for feature in province_features:
        props = feature_properties(feature)

        province.append({
            'name': props['province_name'],
            'latitude': 0,
            'longitude': 0,
        })

    result.save('result.json')


if __name__ == "__main__":
    main()
