import csv

def read_csv(path):
    with open(path, 'r', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        # print(header)
        data = []
        for row in reader:
            iterable = zip(header, row)
            iterable = list(iterable)
            # print('*' * 30)
            # print(iterable)
            country_dict = {key: value for key, value in iterable}
            # print(country_dict)
            data.append(country_dict)
        return data


if __name__ == '__main__':
    result = read_csv('./app/world_population.csv')
    print(result)