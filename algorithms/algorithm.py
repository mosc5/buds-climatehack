#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: robin
@file: algorithm.py.py
@time: 13.11.21 16:08
@desc: 
"""
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
import enum


# JSON = Customer Data + enter,leave
# CSV = Events

class EventType(str, enum.Enum):
    # input
    CUSTOMER_ENTER = "CUSTOMER_ENTER"
    CUSTOMER_LEAVE = "CUSTOMER_LEAVE"

    # output
    # - event_data: new route, e.g. ["stop_b","stop_c"]
    CUSTOMER_SIGNAL = "CUSTOMER_SIGNAL"
    # - event_data: customers left, customers entered, customers in bus, e.g. [1, 0, 2]
    CUSTOMER_BUS_TOP = "CUSTOMER_BUS_TOP"


class Event:
    def __init__(self, event_type: EventType, event_time: datetime, event_data: [] = None):
        self.event_type = event_type
        self.event_time = event_time
        self.event_data = event_data

    def dict(self):
        return self.__dict__


class BaseAlgorithm(ABC):
    def __init__(self, starting_point: str, customer_data: dict(), stops: dict()):
        self.starting_point = starting_point
        self.customer_data = customer_data
        self.stops = stops

    @abstractmethod
    def update(self, clock_time: datetime, event: Event = None) -> List[Event]:
        raise NotImplementedError()

    def get_customer_data(self):
        return self.customer_data


