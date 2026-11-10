from datetime import datetime

class BusinessAgent:

def __init__(self):
    self.name = "My AI Business Agent"

def research_products(self):
    print("Ищу перспективные товары...")

def analyze_market(self):
    print("Анализирую рынок и конкурентов...")

def calculate_profit(self):
    print("Рассчитываю возможную прибыль...")

def prepare_advertising(self):
    print("Готовлю рекламную кампанию...")

def create_cartoon(self):
    print("Готовлю идею мультфильма...")

def run(self):
    print("Запуск агента:", datetime.now())

    self.research_products()
    self.analyze_market()
    self.calculate_profit()
    self.prepare_advertising()
    self.create_cartoon()

    print("Работа завершена!")
if name == "main":
agent = BusinessAgent()
agent.run()
