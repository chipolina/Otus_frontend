import string
from enum import Enum
import random


class CategoryData(Enum):
    Desktops = "Desktops"
    Laptops_Notebooks = "Laptops & Notebooks"
    Components = 'Components'
    Tablets = 'Tablets'
    Software = 'Software'
    Phones_PDAs = 'Phones & PDAs'
    Cameras = 'Cameras'
    MP3_Players = 'MP3 Players'


class Currency_symbols(Enum):
    USD = "$"
    EUR = "€"
    GBP = "£"


def generate_text(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def generate_email():
    return generate_text(7) + "@gmail.com"
