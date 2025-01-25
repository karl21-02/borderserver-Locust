from locust import HttpUser, task, between
import random

class BoardServer(HttpUser):
    waite_time = between(1, 2)

    def on_start(self):
        self.client.post("/users/sign-in", json={"userId": "topojs12",
                                                 "password": "1234"})

