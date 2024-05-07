from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_TYPES_WAITERS = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter
    }
    VALID_TYPES_CLIENTS = {
        "RegularClient" : RegularClient,
        "VIPClient": VIPClient
    }

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.VALID_TYPES_WAITERS:
            # try:
        #     waiter = self.VALID_TYPES_WAITERS[waiter_type](waiter_name, hours_worked)
        # except KeyError:
            return f"{waiter_type} is not a recognized waiter type."

        try:
            waiter = [d for d in self.waiters if d.name == waiter_name][0]
            #next(filter(lambda c: c.name == waiter_name, self.waiters))
            return f"{waiter_name} is already on the staff."

        except IndexError:
        #except StopIteration:
            new_waiter = self.VALID_TYPES_WAITERS[waiter_type](waiter_name, hours_worked)
            self.waiters.append(new_waiter)
            return f"{waiter_name} is successfully hired as a {waiter_type}."


    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.VALID_TYPES_CLIENTS:
            # try:
            #     waiter = self.VALID_TYPES_WAITERS[waiter_type](waiter_name, hours_worked)
            # except KeyError:
            return f"{client_type} is not a recognized client type."

        try:
            client = [d for d in self.clients if d.name == client_name][0]
            # next(filter(lambda c: c.name == waiter_name, self.waiters))
            return f"{client_name} is already a client."

        except IndexError:
            # except StopIteration:
            new_client = self.VALID_TYPES_CLIENTS[client_type](client_name)
            self.clients.append(new_client)
            return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        pass

    def process_client_order(self, client_name: str, order_amount: float):
        pass

    def apply_discount_to_client(self, client_name: str):
        # if client_name in self.clients:
        #     return f"{client_name} received a {self.discount_percentage}% discount. Remaining points {self.points}"
        # else:
        #     f"{client_name} cannot get a discount because this client is not admitted!"
        for client in self.clients:
            if client.name == client_name:
                discount_percentage, remaining_points = client['object'].apply_discount()
                return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"
            return f"{client_name} cannot get a discount because this client is not admitted!"
    def generate_report(self):
        pass
