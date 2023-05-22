import requests
from bs4 import BeautifulSoup


URL = "http://www.nytimes.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="app")

job_elements = results.find_all("div", "css-xdandi")


for job_element in job_elements:
    title_element = job_element.find("h3", class_="indicate-hover")
    print(title_element.text.strip())