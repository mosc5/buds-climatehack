"""

IDE: PyCharm
Project: buds-climatehack
Author: mosc5
Filename: generate_customers.py
Date: 13.11.2021

"""

import random
import datetime
import json


def generate_customers(amount: int, random_seed: int, input_file, output_file):
    random.seed(random_seed)
    customer_list = []
    loc_list = []
    with open('data/' + input_file) as f:
        data = json.load(f)
    for point in data:
        loc_list.append(point['name'])
    for counter in range(amount):
        time = datetime.time(hour=random.randrange(24), minute=random.randrange(60), second=random.randrange(60))
        name = "customer" + str(counter)
        start = random.choice(loc_list)
        destination = random.choice(loc_list)
        while start == destination:
            destination = random.choice(loc_list)
        customer_dict = {
            'name': name,
            'starting_time': str(time),
            'starting_point': start,
            'destination': destination
        }
        customer_list.append(customer_dict)
    with open('data/' + output_file, 'w') as json_file:
        json.dump(customer_list, json_file)


if __name__ == '__main__':
    generate_customers(5, 0, 'points.json', 'customers.json')
