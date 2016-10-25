import json
import os.path


# Загружает содержимое json - файла
def load_data(filepath):
    if(os.path.exists(filepath)):
        with open(filepath, "r") as json_file:
            list = json.loads(json_file.read())
    else:
        list = None
    return list


def pretty_print_json(data):
    format_data = json.dumps(data,
                             ensure_ascii=False,
                             indent=3,
                             separators=(',', ': '),
                             sort_keys=False)
    print(format_data)


def main():
    path = input("Введите абсолютный или относительный путь к файлу:\n")
    json_data = load_data(path)

    if json_data is not None:  # Если файл существует
        pretty_print_json(json_data)
    else:
        print("Файла с именем, которое вы ввели, не существует")


if __name__ == '__main__':
    main()