items = {
    'milk15':{'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
    'cheese':{'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
    'sausage':{'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}

price_less_20 = {item: items[item]['count'] < 20 for item in items}

# price_less_20 = {}

# for item in items:
#     price_less_20[item] = items[item]['count'] < 20

print(f"price_less_20 = {price_less_20}")
