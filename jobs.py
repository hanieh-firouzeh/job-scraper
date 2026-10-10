import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h2", class_="title is-5")
companies = soup.find_all("h3", class_="company")
locations = soup.find_all("p", class_="location")

links = soup.find_all("a")


apply_links = []

for link in links:
    if  link.text.strip() == "Apply":
        apply_links.append(link["href"])



with open("jobs.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Link"])

    for title, company, location, apply_link in zip(titles, companies, locations, apply_links):
            if "python" in title.text.lower():
                writer.writerow([
                    title.text.strip(),
                    company.text.strip(),
                    location.text.strip(),
                    apply_link
            ])


