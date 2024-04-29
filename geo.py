import json
import csv


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
            'name': province_name,
            'cities': []
        }

    def append(self, province_name: str, coordinates: list):
        """
        Add new province
        """
        self.__check_province_name(province_name)
        self.__result[province_name]['coordinates'] = coordinates

    def add_city(self, province_name: str, city):
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

        j = json.dumps(self.__result, ensure_ascii=False).encode('utf-8')
        j = json.dumps(self.__result, ensure_ascii=False).encode('utf-8')
        with open(file_name, 'wb') as f:
            f.write(j)
