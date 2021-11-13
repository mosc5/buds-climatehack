"""

IDE: PyCharm
Project: buds-climatehack
Author: mosc5
Filename: fixed_schedule.py
Date: 13.11.2021

"""
from datetime import datetime
from typing import List
# workaround
import six
import sys
sys.modules['sklearn.externals.six'] = six

import mlrose
from algorithms.algorithm import BaseAlgorithm, Event


class FixedSchedule(BaseAlgorithm):
    def __init__(self, starting_point: str, customer_data: dict(), stops: dict()):
        BaseAlgorithm.__init__(self, starting_point, customer_data, stops)

        # minutes until the route trip repeats
        self.trip_interval = 120

        # identify a static route
        self.fixed_route = self.determine_route()

    def determine_route(self) -> List[tuple]:
        coords = [stop["position"] for stop in self.stops]
        problem_fit = mlrose.TSPOpt(length=len(coords), coords=coords,
                                       maximize=False)
        best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state=2)
        return [self.stops[i] for i in best_state]

    def update_state(self, clock_time: datetime, events: List[Event] = []) -> List[Event]:
        pass


if __name__ == '__main__':
    algo = FixedSchedule("stop_a", [], [{
    "name": "stop_a",
    "position": [
      49,
      97
    ]},{
    "name": "stop_b",
    "position": [
      55,
      60
    ]},{
    "name": "stop_c",
    "position": [
      10,
      20
    ]}])

    print(algo.fixed_route)