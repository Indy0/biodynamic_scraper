import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.save_to_db import save_to_db
import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.rhythmofnature.net/biodynamic-calendar-n-new_york"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0"
}

def scrape_calendar():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')

    data = {}

    cards = soup.find_all('div', class_='card-small')
    print(f"Found {len(cards)} cards.")

    for card in cards:
        month_day = card.find_previous_sibling('div', class_='month-day')
        if not month_day:
            continue

        date_link = month_day.find('a')
        if not (date_link and 'href' in date_link.attrs):
            continue

        href = date_link['href']
        match = re.search(r'lunar-calendar-(\d+)-n', href)
        if not match:
            continue

        date_str = match.group(1)
        date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
        
        events = []
        time_div = card.find('div', class_='card-hour')

        if time_div:
            time_str = time_div.text.strip()
            type_blocks = card.find_all('div', class_='day-element')
            for type_block in type_blocks:
                img = type_block.find('img')
                if img:
                    type_name = img['alt']
                    events.append({'time': time_str, 'state': type_name})
        else:
            # No time means whole day is one or more types
            type_blocks = card.find_all('div', class_='day-element')
            for type_block in type_blocks:
                img = type_block.find('img')
                if img:
                    type_name = img['alt']
                    events.append({'time': '00:00', 'state': type_name})

        print(f"Date: {date}, Events: {events}")

        if date not in data:
            data[date] = []
        data[date].extend(events)

    return data

if __name__ == "__main__":
    scraped_data = scrape_calendar()
    save_to_db(scraped_data)
