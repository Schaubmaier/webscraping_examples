import os

import requests
import pandas as pd
from bs4 import BeautifulSoup

# get url of the desired website
url = 'https://www.karriere.at/jobs/data-scientist/wien'

try:
    # make a http-request
    response = requests.get(url)

except:
    raise ConnectionError("Connection to website failed.")

# raw content to html format
soup = BeautifulSoup(response.content, "html.parser").find_all('div', class_="m-jobsListItem")
print(soup[0])

job_titles, companies, locations, detail_list, extras, salaries = [], [], [], [], [], []

for data in soup:
    job_title = data.find('h2', class_="m-jobsListItem__title").text
    job_titles.append(job_title)
    # print(job_title)

    company = data.find('div', class_="m-jobsListItem__company").text
    companies.append(company)
    # print(data.find('div', class_="m-jobsListItem__company"))

    location = data.find('span', class_="m-jobsListItem__locations m-jobsListItem__pill").text
    locations.append(location)
    # print(location)

    details = data.find_all('span', class_="m-jobsListItem__pill")
    details = [detail.text for detail in details]

    if len(details) == 2:
        details.insert(1, "No Homeoffice")

    extras.append(details[1])
    salaries.append(details[2])


dict = {'job_title': job_titles, 'company': companies, 'location': locations, 'extra': extras,
        'salary': salaries}
# print(dict)

# create dataframe
df = pd.DataFrame(dict)

print(df.to_string())

wd = os.getcwd()
#os.mkdir("output")
path = wd + "\output\jobs.csv"
df.to_csv(path, index=False)
