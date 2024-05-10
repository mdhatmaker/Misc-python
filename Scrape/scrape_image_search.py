import requests

from bs4 import BeautifulSoup


#"https://www.google.com/search?q=hera+hilmar+nude&sa=X&sca_esv=2677688350dc5440&udm=2&biw=1284&bih=1039&prmd=ivsnmbtz&ved=0ahUKEwilspW4naaFAxVRjYkEHcPaAVQQkYoICAE"

searchUrl = "https://www.google.com/search?q=hera+hilmar+nude"

def scrape_image_search(search_for: str):
    #search_for = "hera+hilmar+nude"
    searchUrl = f"https://www.google.com/search?q={search_for}"


def scrape(url: str):
    page = requests.get(url)
    #print(page.text)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    #print(soup.prettify())
    job_elements = results.find_all("div", class_="card-content")
    for job_element in job_elements:
        print(job_element, end="\n"*2)

