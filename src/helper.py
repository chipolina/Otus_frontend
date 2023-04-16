from enum import Enum, IntEnum

BASE_URL = 'http://192.168.15.101:8081/en-gb/'
CATALOG_URL = BASE_URL + "catalog/tablet"
SINGLE_CARD_URL = BASE_URL + "product/laptop-notebook/hp-lp3065"


class CategoryData(Enum):
    Desktops = "Desktops"
    Laptops_Notebooks = "Laptops & Notebooks"
    Components = 'Components'
    Tablets = 'Tablets'
    Software = 'Software'
    Phones_PDAs = 'Phones & PDAs'
    Cameras = 'Cameras'
    MP3_Players = 'MP3 Players'


