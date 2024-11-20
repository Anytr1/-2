import json
import csv

# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'rt') as f:
        with open(OUTPUT_FILENAME, 'w') as d:
            lines = [line_csv for line_csv in csv.DictReader(f)]
            json.dump(lines, d, indent=4)
      # TODO считать содержимое csv файла

      # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
