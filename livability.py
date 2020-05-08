import requests 
import re

url = "https://www.areavibes.com/best-places/kentucky/"

response = requests.get(url)

pattern = re.compile(r'data-match=\"\">(\d{2})<\/i><ul><li><strong>([\w\s]*)\, (\D{2})[\w\s</>()]*: (\d{1,3}\,?\d{3}?)')

