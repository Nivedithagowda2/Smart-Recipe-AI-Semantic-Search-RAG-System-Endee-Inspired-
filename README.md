SmartRecipe AI – Semantic Search & RAG System (Endee-Inspired)
🚀 Overview

SmartRecipe AI is an intelligent recipe search and recommendation system that leverages semantic search and a lightweight vector database architecture inspired by Endee.

Unlike traditional keyword-based search, this system understands the meaning of user queries using embeddings and retrieves the most relevant recipes. It also includes a simple RAG-style chatbot for contextual responses.


🧠 Key Features
🔍 Semantic Search using vector embeddings
⚡ Fast similarity search with cosine similarity
🧩 Custom vector database (Endee-inspired)
🤖 RAG-based chatbot for contextual answers
🎨 Interactive UI using Streamlit
📚 Real-world dataset with multiple recipes


🏗️ System Architecture
Convert recipe descriptions into embeddings
Store vectors in a lightweight in-memory vector store (Endee-style)
Convert user query into embedding
Compute similarity between query and stored vectors
Retrieve top-K relevant recipes
Generate contextual chatbot response (RAG)

🛠️ Tech Stack
Python
Sentence Transformers
NumPy
Streamlit
Cosine Similarity


📂 Project Structure
SmartRecipe-Endee-Pro/
│── app.py                # Streamlit UI + search + chatbot
│── embeddings.py         # Embedding generation
│── endee_client.py       # Endee-style vector database
│── data/
│   └── recipes.json      # Dataset
│── requirements.txt
│── README.md


▶️ How to Run
1. Install dependencies
pip install -r requirements.txt
2. Run the application
streamlit run app.py


🔍 Example Usage
Semantic Search

User Query:

healthy breakfast

Top Results:

Oatmeal with fruits
Smoothie bowl
Avocado toast
Chatbot (RAG)

User Question:

What can I eat for dinner?

Response:

Based on recipes: [relevant recipe suggestions...]


💡 Key Concepts Demonstrated
Semantic search vs keyword search
Vector embeddings
Similarity-based retrieval
Vector database design (Endee-inspired)
Retrieval-Augmented Generation (RAG)


📈 Future Improvements
Integrate with real vector databases (Endee / FAISS)
Add filtering (veg/non-veg, calories)
Improve chatbot using LLM APIs
Deploy as a web application


🎯 Learning Outcome
Built an end-to-end semantic search system
Implemented a custom vector database
Understood how systems like Endee work internally
Developed a mini RAG-based AI assistant




# SmartRecipe AI (Endee Inspired)

## Features:
- 1000+ recipes dataset
- Semantic search using embeddings
- Endee-style vector database simulation
- Simple RAG chatbot

## Run:
pip install -r requirements.txt
streamlit run app.py

## About:
This project simulates Endee vector DB for semantic search and RAG systems.

🤝 Conclusion

This project demonstrates how modern AI-powered search systems work and provides a strong foundation for building scalable applications using vector databases like Endee.
