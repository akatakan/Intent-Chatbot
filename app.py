import joblib
import json
import string
import time
import spacy
import streamlit as st
from random import choice

nlp = spacy.load("en_core_web_sm")

def remove_stopwords(text):
    doc = nlp(text)
    filtered_sentence = []
    for token in doc:
        if not token.is_stop:  # token.is_stop True ise, kelime bir stopword'dür
            filtered_sentence.append(token.text)
    return " ".join(filtered_sentence)


def preprocess_text(text):
    text = remove_stopwords(text)
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    return ' '.join(words)

def load():
    model = joblib.load("model.bin")
    vectorizer = joblib.load("vectorizer.bin")
    with open('intent.json',encoding='utf8') as f:
        data = json.load(f)

    return model,data,vectorizer


def get_name(prompt):
    if 'my name' in prompt.lower() or 'i am'.lower() in prompt.lower():
        doc = nlp(prompt)
        for x in doc.ents:
            if x.label_ == 'PERSON':
                return x.text

def get_responses(data,prompt):
    
    pre_prompt = preprocess_text(prompt)
    pre_prompt = vectorizer.transform([pre_prompt])
    tag = model.predict(pre_prompt)
    
    for intent in data['intents']:
        if intent['intent'] == tag:
            response = choice(intent['responses'])
            break
        
    if "<HUMAN>" in response:
        name = get_name(prompt)
        response = response.replace("<HUMAN>", name)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
    
model, data, vectorizer= load()
st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
if prompt := st.chat_input("Message Chatbot"):   
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        response = st.write_stream(get_responses(data,prompt))
        
    st.session_state.messages.append({"role": "assistant", "content": response})
