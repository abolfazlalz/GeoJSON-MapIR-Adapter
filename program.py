from geo import Geo
from feature import Feature


def main():
    """
    main program
    """
    city_features = Feature('./dataset_cities.geojson')
    province_features = Feature('./dataset_province.geojson')

    result = Geo()

    for i in range(len(province_features)):
        center = province_features.center_point(i)
        props = province_features.properties(i)
        result.append(props['province_name'], center)

    for i in range(len(city_features)):
        props = city_features.properties(i)
        result.add_city(props['province'], {
            'name': props['city'],
            'coordinates': props['point']['coordinates']
        })

    result.save('result.json')
    result.save_csv('result.csv')


if __name__ == "__main__":
    main()
