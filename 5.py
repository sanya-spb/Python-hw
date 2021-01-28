"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
"""


# {
#   "model1": { on_store: 1, on_division: {"division1": 1, "division2": 1} },
#   "model2": { on_store: 2, on_division: {"division1": 1, "division2": 1} },
# }

class Store:
    store_detail = {}

    def __init__(self, name: str):
        self.name = name

    def to_store(self, model_name, count: int):
        if model_name in self.store_detail:
            self.store_detail[model_name]["on_store"] += count
        else:
            self.store_detail[model_name] = {"on_store": count}
            self.store_detail[model_name]["on_division"] = {}
        print(f"на склад поступило {model_name}: {count}шт.")

    def to_company(self, division: str, model_name, count: int):
        if model_name in self.store_detail:
            if self.store_detail[model_name]["on_store"] >= count:
                self.store_detail[model_name]["on_store"] -= count
                if division in self.store_detail[model_name]["on_division"]:
                    self.store_detail[model_name]["on_division"][division] += count
                else:
                    self.store_detail[model_name]["on_division"][division] = count
            else:
                print("нет небходимого количества а складе")
        else:
            print("данная модель отсутствует на складе")
        print(f"со склада ушло {model_name}: {count}шт в отдел: {division}.")


store = Store("Склад")
store.to_store("model1", 3)
store.to_store("model2", 4)
print(store.store_detail)
store.to_company("division1", "model1", 1)
store.to_company("division2", "model1", 1)
store.to_company("division1", "model2", 1)
store.to_company("division2", "model2", 1)
print(store.store_detail)
store.to_company("division1", "model1", 10)
store.to_company("division1", "modelZ", 1)
