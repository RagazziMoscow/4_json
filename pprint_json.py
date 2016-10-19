import json

## Загружает содержимое json - файла
def load_data(filepath):
	try:
		with open(filepath, "r") as json_file:
		    list = json.loads(json_file.read())
		
	except FileNotFoundError:
		list = None
	finally:
		return list



def pretty_print_json(data):
	format_data = json.dumps(data, ensure_ascii = False, indent=3, separators=(',', ': '), sort_keys = False)
	print(format_data)


def main():
    print("Введите абсолютный или относительный путь к файлу:")
    path = input()
    json_data = load_data(path)


    #Если файл существует
    if json_data is not None:
        pretty_print_json(json_data)
    else:
	    print("Файла с именем, которое вы ввели, не существует")



if __name__ == '__main__':
    main()