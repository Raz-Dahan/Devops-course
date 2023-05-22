import requests
from bs4 import BeautifulSoup


URL = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

print(soup.text)
"""
results = soup.find(id="app-root")

job_elements = results.find_all("div", "css-xdandi")


for job_element in job_elements:
    title_element = job_element.find("h3", class_="indicate-hover")
    print(title_element.text.strip())
"""
