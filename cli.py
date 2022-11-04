# не работает, консольный интерфейс для программы
from main import Driver

# colorama.init()
# print(Fore.LIGHTGREEN_EX + text2art("acmp-solver") + Fore.BLUE + "by rimgro")


PROBLEM = "https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=26&id_problem=142"
TOPIC = "https://acmp.ru/asp/do/index.asp?main=topic&id_course=1&id_section=1&id_topic=26"

d = Driver(LOGIN, PASSWORD)
d.set_topic(TOPIC)
d.get_all_problems_in_topic()