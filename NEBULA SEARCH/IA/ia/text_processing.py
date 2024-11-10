
import spacy

nlp = spacy.load("es_core_news_sm")

def preprocess_text(text):
    """
    Procesa el texto: tokeniza, convierte a minúsculas y elimina puntuación.
    """
    doc = nlp(text.lower())  # Convertir el texto a minúsculas y procesarlo con spaCy
    tokens = [token.text for token in doc if not token.is_punct]  # Elimina la puntuación
    return tokens

def text_to_vector(text):
    """
    Convierte el texto en un vector usando los embeddings de spaCy.
    """
    doc = nlp(text.lower())
    return doc.vector  # Retorna el vector promedio del texto
