# Webscraping Project

This project focuses on scraping data about restaurants in Paris for a tourism project. The goal is to collect relevant information such as restaurant details, ratings, and other attributes using different tools and methods.

---

## **Data Collected**
We aimed to collect the following information for each restaurant:
- **Name**: The name of the restaurant.
- **Description**: A brief description of the restaurant.
- **Cuisine Type**: Types of cuisine served (e.g., Italian, French, etc.).
- **Rating**: The average user rating.
- **Opening Hours**: Information about the restaurant’s operating hours.
- **Location**: The restaurant’s address or location details.
- **Average Price**: The estimated average cost of a meal.
- **Review**: The review from a customer to a restaurant.

---

## **Sources**
### **1. Tripadvisor API**
- We utilized the "Free" API provided by Tripadvisor, which offers **5000 free requests per month**.
- This API allowed us to collect structured data for restaurants in Paris.
- You can find the data and the corresponding notebook in the `tripadvisor` folder.

### **2. Google Maps (Selenium & BeautifulSoup)**
- We used **Selenium** and **bs4** to scrape data from Google Maps.
- The data and the associated notebook are available in the `maps` folder.


---

## **App**

### **Restaurant Recommender 🍴**
This project also includes a Streamlit application that provides personalized restaurant recommendations in Paris based on user preferences. The app uses advanced machine learning techniques to match user input with restaurant options, factoring in location, price, and user preferences.

### **Features**
- Personalized restaurant suggestions based on input text.
- Filters recommendations by price and district (arrondissement) in Paris.
- Ranks results using a weighted scoring system that considers price-to-quality ratios and semantic similarity.
- Simple, user-friendly interface powered by Streamlit.

### **Requirements**
- **Python 3.8 or higher**
- Required Python libraries:
  - `streamlit`
  - `transformers`
  - `sentence-transformers`
  - `scikit-learn`
  - `pandas`
  - `numpy`
- Install all dependencies using the following command:
  ```bash
  pip install -r requirements.txt

### **Final Dataset**
The app uses a dataset named `restaurants.csv` with the following columns:
- **name**: Name of the restaurant.
- **rating**: Average rating (1 to 5 scale).
- **price**: Estimated average price in euros (€).
- **restaurant_type**: Type of cuisine (e.g., French, Italian, etc.).
- **address**: Address of the restaurant.
- **embedding**: Precomputed embedding vectors for restaurant descriptions.

### **How to Use**
1. Place the `restaurants.csv` file in the same directory as the app.
2. Run the Streamlit app with the following command:
   ```bash
   streamlit run app.py
