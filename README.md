# 🏡 Homestra_Real_Estate_Scraping  

**Automated real estate data scraper built with Python and Piloterr API**  

This project allows you to **scrape property listings from Homestra**, enrich them with detailed information, and export clean, structured datasets in JSON format.  
It combines the **Piloterr Homestra Search API** and **Piloterr Website Crawler** to make real estate data extraction fast, scalable, and developer-friendly.  

---

## 🚀 Features  

- Scrape Homestra property listings using the **Piloterr Search API**  
- Enrich listings with details like room features, parking, and pricing  
- Custom filters for **country, price range, and pagination**  
- Export structured **JSON datasets** ready for data analysis or machine learning  
- Fully Python-based, lightweight, and easy to reproduce  

---

## Tech Stack  

- **Language:** Python 3.x  
- **Libraries:** `requests`, `tqdm`, `BeautifulSoup4`  
- **API:** [Piloterr API](https://docs.piloterr.com/)  

---

## Installation  

Clone this repository and install all dependencies with a single command:  

```bash
git clone https://github.com/harivonyR/Homestra_Real_Estate_Scraping
cd Homestra_Real_Estate_Scraping
pip install requests pandas tqdm beautifulsoup4
```

---

## Configuration  

To use the Piloterr API, you need a free API key.  

1. Sign up on [Piloterr](https://piloterr.com)  
2. Copy the example credentials file:  
   ```bash
   cp credential.example.py credential.py
   ```  
3. Open `credential.py` and paste your API key inside:  

   ```python
   x_api_key = "YOUR API KEY HERE!"
   ```

---

## 🧠 Usage  

Run the main script to start scraping Homestra listings:  

```bash
python main.py
```

By default, the scraper will:  
- Fetch Homestra listings based on the filters you set in `query_builder()`  
- Enrich results with property details  
- Save output to the `/output` directory as structured JSON  

---

## 🏗Project Structure  

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

## Example Use Cases  

- **Housing market analysis**  
- **Real estate price prediction** (machine learning models)  
- **Competitor monitoring** across regions or countries  
- **Marketing intelligence** for property trends  

---

## 📘 Documentation  

- Official Piloterr API Docs: [https://docs.piloterr.com/](https://docs.piloterr.com/)  
- Blog Tutorial (coming soon): [https://piloterr.com/blog](https://piloterr.com/blog)  

---

## 📄 License  

This project is licensed under the **MIT License** — free to use, modify, and distribute.  

---

## Keywords
`Homestra API`, `Piloterr API`, `real estate data scraping`, `Python scraper`, `property data extraction`, `housing market analysis`, `machine learning dataset`, `price prediction model`, `web scraping real estate`, `property listings scraper`
