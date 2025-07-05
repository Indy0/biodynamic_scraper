# Natural Wine Biodynamic Calendar E-Ink Display 🌿

I started this project because of my interest and love for natural wine. The natural wine movement aims to grow and make wine using simpler, traditional methods. Including not using pesticides, using organic fertilizers, and not putting extra additives into the wine in order to "force" it to taste a certain way. Natural wine is the pure expression of the grape and it's environment.

Biodynamic wine, as an extension of the biodynamic farming methods, also uses organic and simpler methods to make wine but takes it a mystical step further. Biodynamic follows a planting calendar influenced by astrological movements, the changing of star signs and planets, and sees the Earth as "*a living and receptive organism.*" 

The part that interested me in biodynamics is the idea that as the planets move and cross between constellations, it determines the type of day for planting, sowing, harvesting, etc. These are **root** (earth), **water** (leaf), **flower** (air), and **fruit** (fire). According to biodynamics these *bio types* (as I call them) affect how a wine will taste when you open it. Root and leaf days are not considered good to drink wine while flower while flower and especially fruit days are considered good wine drinking days.

So back to the project, this project aims to create a e-ink display using a raspberry pi to display real-time bio type: root, leaf, flower, or fruit. Then, with a simple glance, you will know whether it is a great time to open a wine or if it's better to wait a while.

This project scrapes biodynamic calendar data from rhythmofnature.net, stores it locally in a SQLite database, and is designed to display the current biodynamic day type (Flower, Leaf, Root, or Fruit) on an e-ink screen connected to a Raspberry Pi.

---

## 📋 Project Overview

- Automatically collects biodynamic calendar data for New York time zone.
- Stores the information in a local SQLite database.
- Displays the current biodynamic type automatically based on the current time and date.
- Designed to run on a Raspberry Pi with an e-ink display.

---

## ✅ Features

- Python-based scraper using `requests` and `BeautifulSoup`.
- Local database using SQLite for fast lookups and to practice using SQL in real-world applications.
- Clean, modular project structure for future development.
- Built to automatically scrape data and update the screen without user intervention.
- Stylish e-ink screen with natural, wooden frame fit for any stylish wine bar.

---

## 🗂️ Project Structure
'''
biodynamic_scraper/
│
├── scraper/          → Scraper code
├── data/             → SQLite database + database scripts
├── display/          → Display logic for e-ink screen (coming soon)
├── utils/            → Database helpers
├── tests/            → Test scripts (optional)
│
├── venv/             → Virtual environment
│
├── README.md         → This file
├── requirements.txt  → Python dependencies
├── main.py           → (Optional) Master runner script
'''

