# Создать список учеников подобной структуры.
pipils = [{"firstname": "Masha", "Group": 42, "physics": 2, "informatics": 5, "history": 4}, {"firstname": "Alex", "Group": 42, "physics": 8, "informatics": 6, "history": 9}]
# Определить средний балл каждого студента по всем предметам,

for data in pipils:
    aug = (data["physics"] + data["informatics"] + data["history"]) / 3
    if aug > 6:
        print(data)