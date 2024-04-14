import os

import requests
import pandas as pd
from bs4 import BeautifulSoup

# get url of the desired website
url = 'https://de.wikipedia.org/wiki/Liste_der_größten_Unternehmen_der_Welt'




try:
    # make a http-request
    response = requests.get(url)

except:
    raise ConnectionError("Connection to website failed.")


# raw content to html format
soup = BeautifulSoup(response.content, "html.parser")
#print(response.content)
#print(soup)

# get heading
title = soup.find(id="firstHeading")
print(title.string)


# get html table
table = soup.find_all('table')[0] # returns a list with all the tables on this site
#print(soup.find('table'))

# get categories
# use .strip() to remove extra whitespaces and specified characters like \n
#print(table.find_all('th'))
categories = [val.text.strip() for val in table.find_all('th')]
print(categories)


# create dataframe
df = pd.DataFrame(columns = categories)

print(df)

# get content
table_content = table.find_all('tr')
#print(table_content[0])

for row in table_content[1:]:
    row_data = row.find_all('td')
    #print(row_data[0])
    #print(row_data[0].text)

    individual_data = [data.text.strip() for data in row_data]
    #print(individual_data)

    # append datarow at the end
    len_df = len(df)
    df.loc[len_df] = individual_data

print(df.to_string())



wd = os.getcwd()
#os.mkdir("output")
path = wd + "\output\wiki.csv"
df.to_csv(path, index=False)

