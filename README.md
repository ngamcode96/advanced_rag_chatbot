# Advanced RAG (Retrival Augmented Generation using multi sources: PDF, URL, VIDEO, AUDIO, IMAGE
# How does it work ?
## sources (each source is converted into text): 
### PDF: extract the text from the PDF
### URL: Extract the text (Web scrapping)
### Image: OCR: extract the text from an image
### : Video : extract audio from video and transcribe it into text
### : Audio: transcribe the audio into text

## Embeddings
extracting text from an source and splitting it into small chunks. each chunk is converted into numerical values (text-embedding) using openai embedding model

## store locally vectors into Qdrant database

## extract top 5 relevants informations base on the user query using cosine similarity

## Passing these top 5 relevant informations into LLM (Large language model) as a context: llama-3.1-70B:

## get the result

# How to run the app

## clone the project
## copy .env.example to .env file
  Add values for variables environnment
## create virtual environment and install requirements
  python3 -m venv venv (to create virtual environment)
  source venv/bin/activate (for linux) or venv/Scripts/activate (for windows) 
  pip install -r requirements.txt (to install all requirements

## install Qdrant locally using docker
sudo docker pull qdrant/qdrant 
sudo docker run -p 6333:6333 -v .:/qdrant/storage qdrant/qdrant

## finally run the app
streamlit run app.py
  


