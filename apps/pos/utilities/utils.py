# -*- encoding: utf-8 -*-
"""
__author__ = Cedrouseroll Omondi
__email__ = omondicedo@gmail.com
"""

import string
import secrets


# Function to generate random category id
def generate_category_id(length=6):
    return 'CAT-' + ''.join(
        secrets.choice(
            string.ascii_uppercase + string.digits) for _ in range(length))


# Function to generate random item id
def generate_item_sku(length=8):
    return 'IT-' + ''.join(
        secrets.choice(
            string.ascii_uppercase + string.digits) for _ in range(length))


# Function to generate random item id
def generate_item_upc_default(length=7):
    # this is to avoid collition with the unique constraint
    return 'IT-' + ''.join(
        secrets.choice(
            string.ascii_uppercase + string.digits) for _ in range(length))


# get to return a list of values from a list of dicts
def get_listof_values(listofdicts, value):
    default_value = 'None'
    return list(map(lambda d: d.get(value, default_value), listofdicts))
