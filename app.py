import streamlit as st
import pandas as pd
import numpy as np
from numpy import array
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re
import ast
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
# modele chargé
tokenizerp = AutoTokenizer.from_pretrained("google/flan-t5-large")
modelp = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
model = SentenceTransformer('all-MiniLM-L6-v2')
# Dataset
df_subset = pd.read_csv('restaurants.csv')
df_subset['embeding']=df_subset['embeding'].apply(lambda x: array(ast.literal_eval(x)))
# Score pondéré
def calculate_weighted_score(row, user_similarity=0):
    similarity_weight = 0.5
    price_quality_weight = 1 # beacause in our dataset this ration range from 0 to 0.5

    weighted_score = (
        similarity_weight * user_similarity +
        price_quality_weight * row['rating']/row['price']
    )
    return weighted_score

# Fonction de recommandation
def recommend_restaurants_with_interface(user_input, dataset):
    # Encoder l'input utilisateur
    user_embedding = model.encode([user_input])

    # Préparer les prompts
    loc_prompt = f"In which district this text: '{user_input}' take place?"
    price_prompt = f"What is the price in this text: '{user_input}'?"

    # Localisation
    inputs = tokenizerp(loc_prompt, return_tensors="pt")
    outputs = modelp.generate(inputs.input_ids)
    out_text = tokenizerp.decode(outputs[0], skip_special_tokens=True)
    user_around = re.search(r'\d+', out_text)
    user_arrond = None
    if user_around:
        user_arrond = user_around.group()
        if len(user_arrond) == 1:
            user_arrond = f"7500{user_arrond}"
        elif len(user_arrond) == 2:
            user_arrond = f"750{user_arrond}"

    # Prix
    inputs = tokenizerp(price_prompt, return_tensors="pt")
    outputs = modelp.generate(inputs.input_ids)
    out_text = tokenizerp.decode(outputs[0], skip_special_tokens=True)
    price_match = re.search(r'\d+', out_text)
    user_price = int(price_match.group()) if price_match else None

    # Filtrage du dataset
    subset = dataset.copy()
    if user_price is not None:
        subset = subset[subset['price'] <= user_price]
    if user_arrond is not None:
        subset = subset[subset['address'].str.contains(user_arrond, case=False, regex=False)]

    if subset.empty:
        return None, "No restaurants found for this request. Try a less restrictive request."

    # Calcul des similarités cosinus
    embeddings = subset['embeding'].tolist()
    similarities = cosine_similarity(user_embedding, embeddings)[0]

    # Ajouter les similarités et calculer le score pondéré
    subset['similarity_score'] = similarities
    subset['weighted_score'] = subset.apply(
        lambda row: calculate_weighted_score(row, user_similarity=row['similarity_score']),
        axis=1
    )

    # Trier par score pondéré décroissant
    top_matches = subset.sort_values(by='weighted_score', ascending=False)

    # Résultats
    top_matches = top_matches[['name', 'rating', 'price', 'restaurant_type', 'address']].head(5)
    top_matches['rating'] = top_matches['rating'].round(1)
    top_matches['price'] = top_matches['price'].astype(int)

    # Renommer les colonnes
    top_matches = top_matches.rename(columns={
        'name': 'Restaurant Name',
        'rating': 'Rating (1-5)',
        'price': 'Price (€)',
        'restaurant_type': 'Type of Cuisine',
        'address': 'Address'
    })

    top_matches = top_matches.reset_index(drop=True)
    return top_matches, None

# Interface utilisateur avec Streamlit
st.title("Restaurant Recommender 🍴")
st.markdown("Find the perfect restaurant in Paris based on your preferences!")

# Inputs utilisateur
user_input = st.text_input("Describe the type of restaurant you're looking for:", placeholder="ex cozy French bistro ...")

# Bouton recherche
if st.button("Find Restaurants"):
    if not user_input:
        st.warning("Please describe the type of restaurant you're looking for.")
    else:
        # Lancer recommandation
        recommendations, error = recommend_restaurants_with_interface(user_input, df_subset)
        if error:
            st.error(error)
        else:
            st.success("Here are your top recommendations, bon appétit:")
            st.table(recommendations)