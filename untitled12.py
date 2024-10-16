# import streamlit as st
# import pinecone
# from sentence_transformers import SentenceTransformer
# import cohere
# import os
# from pinecone import Pinecone, ServerlessSpec

# # Initialize Pinecone using the API key from environment variables
# pinecone_api_key = os.getenv('2e07d605-eb83-457f-ae12-9596b03c33ba')  # Replace with your actual env variable name

# # Create an instance of the Pinecone class
# pc = Pinecone(api_key=pinecone_api_key)

# index_name = "quickstart"

# # Create Pinecone index if it doesn't exist
# if index_name not in pc.list_indexes().names():
#     pc.create_index(
#         name=index_name,
#         dimension=8,  # Update with your actual model dimension
#         metric="cosine",
#         spec=ServerlessSpec(
#             cloud="aws",
#             region="us-east-1"
#         )
#     )

# # Initialize the index with the host URL
# index = pc.Index(index_name)

# # Initialize the Cohere client using the API key from environment variables
# cohere_api_key = os.getenv('ltqwZ1leSxX9DArKiHc7TZsFcmOQwd9QScYZAwR8')  # Replace with your actual env variable name
# co = cohere.Client(cohere_api_key)

# # Load pre-trained embedding model
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Streamlit UI
# st.title("AI-Powered Q&A App")

# message = st.text_input("Enter your question:", value="What is Machine Learning?")

# if st.button("Get Answer"):
#     # Get embeddings for the input message
#     embeddings = model.encode([message])
    
#     # Query Cohere's Chat API
#     response = co.chat(
#         message=message,
#         model="command",
#         temperature=0.3
#     )
    
#     # Display Cohere's response
#     st.write("Cohere's Response:")
#     st.write(response.text)

#     # Store the embeddings in Pinecone
#     st.write("Storing embeddings in Pinecone...")
#     pinecone_upsert = index.upsert(
#         vectors=[
#             ("message_id", embeddings.tolist())  # Ensure the embedding is converted to a list
#         ]
#     )
#     st.write("Embeddings stored successfully!")

import streamlit as st
import pinecone
from sentence_transformers import SentenceTransformer
import cohere
import os
from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone using the API key from environment variables
pinecone_api_key = os.getenv('2e07d605-eb83-457f-ae12-9596b03c33ba')  # Replace with your actual env variable name

# Create an instance of the Pinecone class
pc = Pinecone(api_key=pinecone_api_key)

index_name = "quickstart"

# Create Pinecone index if it doesn't exist
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=8,  # Update with your actual model dimension
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# Initialize the index with the host URL
index = pc.Index(index_name)

# Initialize the Cohere client using the API key from environment variables
cohere_api_key = os.getenv('ltqwZ1leSxX9DArKiHc7TZsFcmOQwd9QScYZAwR8')  # Replace with your actual env variable name
co = cohere.Client(cohere_api_key)

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Streamlit UI
st.title("AI-Powered Q&A App")

message = st.text_input("Enter your question:", value="What is Machine Learning?")

if st.button("Get Answer"):
    # Get embeddings for the input message
    embeddings = model.encode([message])
    
    # Query Cohere's Chat API
    response = co.chat(
        message=message,
        model="command",
        temperature=0.3
    )
    
    # Display Cohere's response
    st.write("Cohere's Response:")
    st.write(response.text)

    # Store the embeddings in Pinecone
    st.write("Storing embeddings in Pinecone...")
    pinecone_upsert = index.upsert(
        vectors=[
            ("message_id", embeddings.tolist())  # Ensure the embedding is converted to a list
        ]
    )
    st.write("Embeddings stored successfully!")
