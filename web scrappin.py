import requests
from bs4 import BeautifulSoup

# url of which site want to sracp
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

# getting content of site with beatifullsoup
soup = BeautifulSoup(page.content, 'html.parser')

# retriving data from the site
results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    print(job_elem.text)
