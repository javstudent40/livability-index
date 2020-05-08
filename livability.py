import requests 
import re
import pandas as pd

data = []

url = "https://www.areavibes.com/best-places/kentucky/"

response = requests.get(url)

pattern = re.compile(r'data-match=\"\">(\d{2})<\/i><ul><li><strong>([\w\s]*)\, (\D{2})[\w\s</>()]*: (\d{1,3}\,?\d{3}?)')

locations = re.findall(pattern, response.text)

for place in locations[:5]:
    rating = place[0]
    city = place[1]
    state = place[2]
    population = place[3]
    data.append((city, state, population, rating))

df = pd.DataFrame(data, columns=["City", "State", "Population", "Livability Index"])

df.to_csv('livescrape.csv', index=False)


