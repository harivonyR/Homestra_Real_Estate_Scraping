# 🏡 Homestra_Real_Estate_Scraping  

**Automated real estate data scraper built with Python and Piloterr API**  

This project allows you to **scrape property listings from Homestra**, enrich them with detailed information, and export clean, structured datasets in JSON format.  
It combines the **Piloterr Homestra Search API** and **Piloterr Website Crawler** to make real estate data extraction fast, scalable, and developer-friendly.  

---

## GET STARTED

Clone  the repository   
```bash
git clone https://github.com/harivonyR/Homestra_Real_Estate_Scraping
```

Browse into the project
```bash
cd Homestra_Real_Estate_Scraping
```

Install dependecies
```bash
pip install requests pandas tqdm beautifulsoup4
```

Copy the example credentials file:  
```bash
cp credential.example.py credential.py
```

Open `credential.py` and paste your API key inside:  
```python
x_api_key = "YOUR API KEY HERE!"
```

---

## RUN THE SCRIPT

Open `main.py` and set the maximum page to scrape
```python
MAX_PAGE = 2
```

Run the main script to start scraping Homestra listings:  
```bash
python main.py
```

This will:  
- Fetch Homestra listings based on the filters you set in `query_builder()`  
- Enrich results with property details  
- Save output to the `/output` directory as structured JSON  

---

## Project Structure  

```
Homestra_Real_Estate_Scraping/
│
├── main.py                     # Main script to run scraping
├── credentials.example.py      # Example for API key configuration
├── script/
│   ├── homestra.py             # Tailored function for Homestra scraping : build query, scrape detail/summary
│   └── piloterr.py             # Homestra Search API request 
│
├── output/                     # Default folder for JSON output
└── README.md                   # Project documentation
```

---

## Use Cases  

- **Housing market analysis**  
- **Real estate price prediction** (machine learning models)  
- **Competitor monitoring** across regions or countries  
- **Marketing intelligence** for property trends  

---

## Documentation  

- Official Piloterr API Docs: [https://docs.piloterr.com/](https://docs.piloterr.com/)  
- Blog Tutorial (coming soon): [https://piloterr.com/blog](https://piloterr.com/blog)  

---

## License  
This project is licensed under the **MIT License** — free to use, modify, and distribute.  

---

## Keywords
`Homestra API`, `Piloterr API`, `real estate data scraping`, `Python scraper`, `property data extraction`, `housing market analysis`, `machine learning dataset`, `price prediction model`, `web scraping real estate`, `property listings scraper`
