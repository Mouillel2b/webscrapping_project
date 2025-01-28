Restaurant Recommender 🍴
This project is a Streamlit application that provides personalized restaurant recommendations in Paris based on user preferences. The app uses advanced machine learning techniques to match user input with restaurant options, factoring in location, price, and user preferences.

Features

Personalized restaurant suggestions based on input text.
Filters recommendations by price and district (arrondissement) in Paris.
Ranks results using a weighted scoring system that considers price-to-quality ratios and semantic similarity.
Simple, user-friendly interface powered by Streamlit.
Requirements

Python 3.8 or higher
Required Python libraries:
streamlit
transformers
sentence-transformers
scikit-learn
pandas
numpy
Install all dependencies using the following command:

bash
Copier
Modifier
pip install -r requirements.txt
Dataset
The app uses a dataset named restaurants.csv with the following columns:

name: Name of the restaurant.
rating: Average rating (1 to 5 scale).
price: Estimated average price in euros (€).
restaurant_type: Type of cuisine (e.g., French, Italian, etc.).
address: Address of the restaurant.
embeding: Precomputed embedding vectors for restaurant descriptions.
How to Use

Place the restaurants.csv file in the same directory as the app.
Run the Streamlit app with the following command:
bash
Copier
Modifier
streamlit run app.py
Enter a description of the restaurant you’re looking for in the input box (e.g., "a cozy French bistro in the 5th arrondissement with a budget-friendly price").
The app will display the top 5 recommended restaurants based on your input.
Notes

This README was written without running or testing the code. Any potential issues in the implementation should be resolved by thoroughly reviewing the code or testing the application directly.
If the dataset structure or code logic requires adjustments, ensure that these are corrected before launching the app.
Limitations

Recommendations depend on the quality of the dataset and precomputed embeddings.
Models may not fully understand highly ambiguous or incomplete inputs.
License
This project is for academic purposes. Redistribution or commercial use is prohibited without prior permission.