"""

IDE: PyCharm
Project: buds-climatehack
Author: mosc5
Filename: simulation.py
Date: 13.11.2021

"""

from typing import List
from algorithm import BaseAlgorithm
from datetime import datetime, timedelta


class Simulation:
    def __init__(self, algorithm_list: List[BaseAlgorithm]):
        self.algorithms = algorithm_list
        self.start_time = datetime(2021, 11, 13)
        self.end_time = self.start_time + timedelta(days=1)

    def run(self):
        looptime = self.start_time
        while looptime < self.end_time:
            for alg in self.algorithms:
                alg.update(looptime)
            looptime += timedelta(seconds=1)

    def dict(self):
        return self.__dict__
