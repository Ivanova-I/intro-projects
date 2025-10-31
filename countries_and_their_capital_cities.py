import requests
from bs4 import BeautifulSoup

def build_country_capital_dict():
    url = "https://geographyhost.com/countries-and-their-capital-cities/"
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    country_to_capital = {}

    table = soup.find("table")
    if table:
        for row in table.find_all("tr"):
            cols = row.find_all(["td","th"])
            if len(cols) >= 2:
                country = cols[0].get_text(strip=True)
                capital = cols[1].get_text(strip=True)
                country_to_capital[country.lower()] = capital
    else:

        for li in soup.find_all("li"):
            text = li.get_text(strip=True)
            if "–" in text:
                parts = text.split("–", 1)
            elif ":" in text:
                parts = text.split(":", 1)
            else:
                continue
            country = parts[0].strip()
            capital = parts[1].strip()
            country_to_capital[country.lower()] = capital

    return country_to_capital

def get_capital(country_name, lookup_dict):
    return lookup_dict.get(country_name.lower(), None)

def main():
    print("Country → Capital lookup")
    print("Please note that this may take a few seconds")
    lookup = build_country_capital_dict()
    print(f"Loaded {len(lookup)} entries.")
    while True:
        country = input("Enter a country name or 'quit' to exit: ").strip()
        if country.lower() in ["quit", "exit"]:
            break
        capital = get_capital(country, lookup)
        if capital:
            print(f"The capital of {country} is {capital}.")
        else:
            print(f"Sorry — could not find the capital for '{country}'. Try checking spelling or alternate country name.")

if __name__ == "__main__":
    main()
