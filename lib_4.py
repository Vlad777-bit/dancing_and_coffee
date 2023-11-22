import json
import yaml

def convert_json_to_yaml(source_file, finish_file):
	try:
		file_json = open(source_file, "r", encoding="utf-8")
		python_dict = json.load(file_json)

		file_yaml = open(finish_file, "w", encoding="utf-8")
		yaml.dump(python_dict, file_yaml, allow_unicode=True)

		file_yaml.close()

		print("YAML file saved.")
	except Exception as err:
		print("Произошла ошибка: ", err)
		exit(1);

convert_json_to_yaml('data.json', 'data.yaml')
