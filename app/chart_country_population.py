import read_csv
import re

world_population = read_csv.read_csv('./app/world_population.csv')

def get_country_data(country_name):
    new_list = filter(lambda item : item['Country/Territory'] == country_name, world_population)
    new_list = list(new_list)
    return new_list


country_data = get_country_data('Argentina')

for element in country_data:
    result = { key for key in element}
    result = list(result)
    # result = re.findall('[0-9]+', result)
    print(result)


# print(type(country_data))
# print(country_data)

# result = { key for key in country_data}
# # print(type(country_data))
# print(result)