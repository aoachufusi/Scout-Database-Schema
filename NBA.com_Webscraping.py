import requests
from bs4 import BeautifulSoup

# Fetch the webpage
url = "https://www.nba.com/stats/player/1626164"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Name
name = soup.find(class_="PlayerSummary_playerNameText___MhqC").get_text()

# Points
points = soup.find_all(class_="PlayerSummary_playerStatValue___EDg_")[0].get_text()

# Assists
#assists = soup.find_all(class_="PlayerSummary_playerStatValue__EDg_")[2].get_text()

# Rebounds
#rebounds = soup.find_all(class_="PlayerSummary_playerStatValue__EDg_")[1].get_text()

# Position
position = soup.find(class_="PlayerSummary_mainInnerInfo__jv3LO").get_text().split(" | ")[2]

# Jersey Number
jersey_number = soup.find(class_="PlayerSummary_mainInnerInfo__jv3LO").get_text().split(" | ")[1]

# Alma Mater
alma_mater = soup.find_all(class_="PlayerSummary_playerInfoValue__JS8_v")[3].get_text()

# Birth Date
birth_date = soup.find_all(class_="PlayerSummary_playerInfoValue__JS8_v")[5].get_text()

# Height
height = soup.find_all(class_="PlayerSummary_playerInfoValue__JS8_v")[0].get_text()

# Weight
weight = soup.find_all(class_="PlayerSummary_playerInfoValue__JS8_v")[1].get_text()

# Current Team
current_team = soup.find(class_="PlayerSummary_mainInnerInfo__jv3LO").get_text().split(" | ")[0]

# Draft Pick
draft_pick = soup.find_all(class_="PlayerSummary_playerInfoValue__JS8_v")[6].get_text()

# Print extracted data
print(f"Name: {name}")
print(f"Points: {points}")
#print(f"Assists: {assists}")
#print(f"Rebounds: {rebounds}")
print(f"Position: {position}")
print(f"Jersey Number: {jersey_number}")
print(f"Alma Mater: {alma_mater}")
print(f"Birth Date: {birth_date}")
print(f"Height: {height}")
print(f"Weight: {weight}")
print(f"Current Team: {current_team}")
print(f"Draft Pick: {draft_pick}")