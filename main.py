import os
from urllib.parse import urlparse, parse_qs

import colorama
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

# основная либа проекта, здесь происходит авторизация и отправка решений
class Driver:
    topic = ""

    # установка драйвера и логин в систему
    def __init__(self, nickname, password):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.get("https://acmp.ru")
        self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/table/tbody/tr[3]/td[4]/form/nobr/b/input[1]").send_keys(nickname)
        self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/table/tbody/tr[3]/td[4]/form/nobr/b/input[2]").send_keys(password)
        self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/table/tbody/tr[3]/td[4]/form/nobr/b/input[3]").click()

    # устанавливаем тему
    def set_topic(self, link):
        self.topic = link

    # отправить решение задачи по ссылке
    def send_solution(self, link, filename):
        if not self.driver: return

        self.driver.get(linkм)

        problem_text = self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[3]").text
        problem_number = problem_text.join(i for i in problem_text if i.isdigit())
        filename = "solutions/" + problem_number.zfill(4) + ".cpp"

        if not os.path.isfile(filename):
            print(colorama.Fore.RED + "Problem " + problem_number + " solution is not found" + colorama.Fore.RESET)
            return

        with open(filename, "r") as f:
            solution = f.read()
            self.driver.implicitly_wait(10)
            file_upload = self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/form/input[1]")
            file_upload.send_keys(os.path.abspath(filename))
            self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/form/input[2]").click()
            print("problem " + problem_number + " solution is sended")

    # получаем список задач, если установлена тема через set_topic()
    def get_all_problems_in_topic(self):
        if not self.topic: return []
        self.driver.get(self.topic)
        self.driver.implicitly_wait(3)
        elements = self.driver.find_elements(By.XPATH, "//a[@href]")
        links = []
        needed_args = ['main', 'id_course', 'id_section', 'id_topic', 'id_problem']
        for l in [e.get_attribute("href") for e in elements]:
            args = parse_qs(urlparse(l).query)
            print(args.keys())
            print(needed_args)
            if list(args.keys()) == needed_args: links.append(l)
        return links



