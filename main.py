"""

IDE: PyCharm
Project: buds-climatehack
Author: mosc5
Filename: main.py
Date: 13.11.2021

"""

import algorithms
import algorithms.simulation as simulation
import json
from datetime import datetime

from algorithms.fixed_schedule import FixedSchedule


def parse_customers(file_name):
    """
    Parse customer JSON from data directory with specified name
    :param file_name: "example.json"
    :return:
    """
    with open("data/"+file_name) as f:
        data = json.load(f)
    for customer in data:
        # now song is a dictionary
        for attribute, value in customer.items():
            if 'time' in attribute:
                customer[attribute] = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    return data


if __name__ == '__main__':
    customers = parse_customers("customers.json")
    with open("data/points.json") as p:
        points = json.load(p)
    alg1 = FixedSchedule("stop_a", [], points)
    alg_list = []
    sim = simulation.Simulation(alg_list)
    sim.run()
