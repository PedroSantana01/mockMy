from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task(1)
    def iniciar(self):
        self.index()

    @task(1)
    def click_registrar(self):
        self.registre()

    @task(1)
    def click_login(self):
        self.login()

    @task(1)
    def sair(self):
        self.index()


def index(self):
    self.client.get("https://swarmlb.atlastest.tk/")


def login(self):
    self.client.post("https://swarmlb.atlastest.tk/br/login/",
                     {"login[user]": "29496170", "login[pass]": "fernanda11", "submitted": "1",
                      "uniq": "3b81c90c8dfaeef6fd36508d59aea024"})


def register(self):
    self.cliente.post("https://swarmlb.atlastest.tk/br/registro/",
                      {"register[first_name]": "Fernanda", "register[last_name]": "Lira",
                       "register[email]": "fernanda@atlasproj.com", "register[country_code]": "++55 Brasil:+55",
                       "register_area_code": "011", "register[phone_number]": "99999-9999",
                       "register[terms]": "::before"})


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
