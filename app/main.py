import utils
import read_csv
import charts


def run():

    data                   = read_csv.read_csv('./app/world_population.csv')
    countries, percentages = utils.get_world_percentages(data)

    charts.generate_pie_chart(countries, percentages)
    country = input('Type country => ')

    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)
#* Entry point
if __name__ == '__main__':
    run()