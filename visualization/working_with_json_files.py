import json
import pygal
filename = '/Users/nataliakalinina/Desktop/population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        # print(country_name + ': ' + str(population))

wm = pygal.Worldmap()
wm.title('Populations of countries in North America')
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_population.svg')