# Создать список учеников подобной структуры.
pipils = [{"firstname": "Masha", "Group": 42, "physics": 2, "informatics": 5, "history": 4}, {"firstname": "Alex", "Group": 42, "physics": 8, "informatics": 6, "history": 9}]
# Определить средний балл каждого студента по всем предметам,
pipils1 = pipils[0]
pipils2 = pipils[1]
del pipils1["firstname"]
del pipils2["firstname"]
del pipils1["Group"]
del pipils2["Group"]
print(pipils1)
print(pipils2)
result1 = sum(pipils1.values()) / len(pipils1)
result2 = sum(pipils2.values()) / len(pipils2)
print(result1)
print(result2)
name1 = {}
name2 = {}
name1["firstname"] = 'Masha'
name1["result"] = sum(pipils1.values()) / len(pipils1)
name2["firstname"] = 'Alex'
name2["result"] = sum(pipils2.values()) / len(pipils2)
print(name1)
print(name2)
# и вывести сведения о студентах, средний балл которых больше 4.
if result1 > 4:
    print(name1)
if result2 > 4:
    print(name2)