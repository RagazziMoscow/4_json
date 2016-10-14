import json

## Загружает содержимое json - файла
def loads_json(path):
	try:
		file = open(path, "r")
		list = json.loads(file.read())
		
	except:
		print("Файла с именем, которое вы ввели, не существует в текущей дирректории")
		list = ""
	finally:
		return list

print("Введите абсолютный или относительный путь к файлу:")
path = input()
data = loads_json(path)


#Если data не является пустой строкою
if data:
	format_data = json.dumps(data, ensure_ascii = False, indent=3, separators=(',', ': '), sort_keys = False)

	print(format_data)