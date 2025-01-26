from locust import HttpUser, task, between
import random

class AddPosts(HttpUser):
    waite_time = between(1, 2)

    def on_start(self):
        self.client.post("/users/sign-in", json={"userId": "topojs12",
                                                 "password": "1234"})

    @task
    def add_post(self):
        # 게시글 추가 요청
        self.client.post("/posts", json={
            "name": "게시글 제목",
            "contents": "게시글 내용",
            "userId": 1,
            "categoryId": 2,
            "tagDTOList": [
                {"name": "개발 블로그3", "url": "https://localhost:8080"},
                {"name": "자유 블로그3", "url": "https://localhost:8080"}
            ]
        })