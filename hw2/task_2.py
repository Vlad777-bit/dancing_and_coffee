boys = ["Александр", "Иннокентий", "Добрыня", "Алиджон"]
girls = ["Петруша", "Любовь", "Зинаида", "Роза"]
sorted_girls = sorted(girls)
sorted_boys = sorted(boys)

if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары")
else:
    for idx in range(len(sorted_boys)):
        print(sorted_boys[idx], sorted_girls[idx])
