pip install -r requirements.txt

ollama serve

ollama pull llama3

ollama pull nomic-embed-text

python ingest.py

streamlit run app.py


Note: If re-running
rmdir /s /q chroma_db
python ingest.py