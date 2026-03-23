
import streamlit as st
from embeddings import get_embedding
from endee_client import EndeeClient
import json

st.set_page_config(page_title="SmartRecipe AI", layout="wide")

st.title("🍲 SmartRecipe AI (Endee Inspired)")
st.sidebar.title("🤖 Chat Assistant")

# Load data
with open("data/recipes.json", "r") as f:
    recipes = json.load(f)

client = EndeeClient()
for r in recipes:
    emb = get_embedding(r["description"])
    client.insert(r["name"], emb, r)

# Search UI
query = st.text_input("🔍 Search recipes")

if query:
    q_emb = get_embedding(query)
    results = client.search(q_emb, top_k=5)

    st.subheader("Top Matches:")
    for res in results:
        st.write(f"### {res['metadata']['name']}")
        st.write(res["metadata"]["description"])

# Chatbot (simple RAG)
user_q = st.sidebar.text_input("Ask about recipes:")

if user_q:
    q_emb = get_embedding(user_q)
    results = client.search(q_emb, top_k=3)

    context = " ".join([r["metadata"]["description"] for r in results])
    answer = f"Based on recipes: {context}"
    st.sidebar.write(answer)
