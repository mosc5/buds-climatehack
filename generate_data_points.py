#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: robin
@file: generate_data_points.py.py
@time: 13.11.21 14:03
@desc: 
"""
import json
import numpy as np
import random
random.seed(0)


def generate_data_points(filename: str, n_points: int = 5, average_speed: float = 50.0):
    """
    Generates a JSON-file with name points, distances and travel times based on average speed of vehicle
    :param average_speed: in kilometer per hour
    :param n_points:
    :param filename:
    :return:
    """
    points: list = []

    # generate points
    names = [f"stop_{chr(i)}" for i in range(97, n_points + 97)]
    for name in names:
        point_template = dict()
        point_template["name"] = name
        point_template["position"] = [random.randint(0, 100), random.randint(0, 100)]
        point_template["distances"] = dict()
        point_template["travel_time"] = dict()
        points.append(point_template)

    # calculate distances
    for point in points:
        a = np.array(point["position"])

        for second_point in points:
            if point["name"] != second_point["name"]:
                b = np.array(second_point["position"])
                dist = np.linalg.norm(a - b)
                point["distances"][second_point["name"]] = float(dist)
                # calculate travel time in seconds
                point["travel_time"][second_point["name"]] = round((float(dist)/average_speed)*3600)

    with open(filename, "w+", encoding="utf8") as json_file:
        json.dump(points, json_file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    generate_data_points("data/points.json")
