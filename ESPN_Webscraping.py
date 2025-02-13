import requests
from bs4 import BeautifulSoup

# Fetch the webpage
url = "https://www.espn.com/nba/player/stats/_/id/6450/kawhi-leonard"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# First Name
#first_name = soup.find(class_="truncate min-w-0 fw-light").get_text()

# Last Name
#last_name = soup.find_all(class_="truncate min-w-0")[1].get_text()

# Points
#points = soup.find_all(class_="StatBlockInner__Value tc fw-medium n3 clr-gray-02")[0].get_text()

# Assists
assists = soup.find_all(class_="StatBlockInner__Value tc fw-medium n3 clr-gray-02")[2].get_text()

# Rebounds
rebounds = soup.find_all(class_="StatBlockInner__Value tc fw-medium n3 clr-gray-02")[1].get_text()

# Field Goal %
field_goal_percent = soup.find_all(class_="StatBlockInner__Value tc fw-medium n3 clr-gray-02")[3].get_text()

# Position
position = soup.find_all("li")[5].get_text()

# Jersey Number
jersey_number = soup.find_all("li")[4].get_text()

# Alma Mater
alma_mater = soup.find_all("li")[8].get_text().split("\n")[1]

# Birth Date
birth_date = soup.find_all("li")[7].get_text().split("\n")[1].split(" ")[0]

# Height
height = soup.find(class_="fw-medium clr-black").get_text().split(", ")[0]

# Weight
weight = soup.find(class_="fw-medium clr-black").get_text().split(", ")[1]

# Current Team
current_team = soup.find_all("li")[3].get_text()

# Draft Pick
draft_pick = soup.find_all("li")[9].get_text().split(": ")[1]

# Print extracted data
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Points: {points}")
print(f"Assists: {assists}")
print(f"Rebounds: {rebounds}")
print(f"Field Goal %: {field_goal_percent}")
print(f"Position: {position}")
print(f"Jersey Number: {jersey_number}")
print(f"Alma Mater: {alma_mater}")
print(f"Birth Date: {birth_date}")
print(f"Height: {height}")
print(f"Weight: {weight}")
print(f"Current Team: {current_team}")
print(f"Draft Pick: {draft_pick}")
