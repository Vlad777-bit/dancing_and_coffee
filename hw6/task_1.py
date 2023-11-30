purchases = {}

def read_file(sourcePath):
	file = open('./purchase_log.txt', 'r', encoding='utf-8');

	for line in file:
		line = line.strip().split(' ')

		if len(line) >= 2:
			user_id, category = line[0], line[1]
			purchases[user_id] = category

def print_result():
	read_file('./purchase_log.txt')

	for user_id, category in list(purchases.items())[:2]:
		print(f"{user_id} {category}")

print_result()
