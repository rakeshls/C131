import csv
import plotly.express as px
rows=[]
with open('main.csv','r')as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        rows.append(row)
headers = rows[0]
planet_data = rows[1:]
print(headers)
print(planet_data[0])
solar_system_planet_count = {}
headers[0] = 'row__Num'
for data in planet_data:
    if solar_system_planet_count.get(data[11]):
        solar_system_planet_count[data[11]]+=1
    else:
        solar_system_planet_count[data[11]]=1
max_solar_system = max(solar_system_planet_count,key=solar_system_planet_count.get)
print('Solar System {} has maximum planets {} out of the total disovered'.format(max_solar_system,solar_system_planet_count[max_solar_system]))
HD_planets = []
for data in planet_data:
    if max_solar_system == data[11]:
        HD_planets.append(data)
print(HD_planets)
temp_planet_data = list(planet_data)
for data in temp_planet_data:
    planet_mass = data[3]
    if planet_mass.lower()=='unknown':
        planet_data.remove(data)
        continue 
    else:
        planet_mass_value =planet_mass.split(' ')[0]
        planet_mass_ref = planet_mass.split(' ')[1]
        if planet_mass_ref == 'Jupiters':
            planet_mass_value = float(planet_mass_value)*317.8
            data[3] = planet_mass_value
    planet_radius = data[7]
    if planet_radius.lower() == 'unknown':
        planet_data.remove(data)
        continue
    else:
        planet_radius_value = planet_radius.split(' ')[0]
        planet_radius_ref = planet_radius.split(' ')[2]
        if planet_radius_ref == 'Jupiter':
            planet_radius_value = float(planet_radius_value)*11.2
            data[7] = planet_radius_value
HD_planets_masses = []
HD_planets_names = []
for data in HD_planets:
    HD_planets_masses.append(data[3])
    HD_planets_names.append(data[1])
HD_planets_names.append(1)
HD_planets_masses.append('Earth')
fig = px.bar(x=HD_planets_names,y=HD_planets_masses)
#fig.show()
planet_masses =[]
planet_radiuses = []
planet_names = []
for data in planet_data:
    planet_masses.append(data[3])
    planet_radiuses.append(data[7])
    planet_names.append(data[1])
planet_gavity = []
for index,name in enumerate(planet_names):
    print(index)
    gravity = (float(planet_masses[index])*5.972e+24)/(float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
    planet_gavity.append(gravity)
fig =px.scatter(x=planet_radiuses,y=planet_masses,size= planet_gavity,hover_data=[planet_names])
fig.show()