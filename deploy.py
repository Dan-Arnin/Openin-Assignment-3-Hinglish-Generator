import nltk
import requests
from googletrans import Translator
import streamlit as st


nltk.download('words')
translator = Translator()


API_URL = "https://api-inference.huggingface.co/models/VasRosa/Hinglish-finetuned"
headers = {"Authorization": "Bearer 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"}


def check_word(word):
    return word in nltk.corpus.words.words()

def englishtohindi(src_text, type = 0):
  def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload).json()
    return response[0]['generated_text']
  final = query(src_text)
  if type == 1:
    final = translate_main(final.lower())
  return final

def translate_main(sent):
  translated_sent = ""
  sent = sent.split(" ")
  for i in sent:
    if check_word(i) == True and len(i) > 2:
      translated_sent += i + " "
    else:
      trans = translator.translate(i, dest = 'hi').text
      translated_sent += trans + " "


  return translated_sent


# Streamlit app title
st.title("Hinglish Generator")

# Input text box for user input

user_input = st.text_input("Enter text for API request")

option = st.radio("Choose output option:", ("Hinglish", "Hinglish with Hindi"))


# Button to trigger API request
if st.button("Generate"):
    if user_input:
        # Define the API endpoint URL
        if option == "Hinglish":
            st.write(englishtohindi(user_input, 0))

        else:
            st.write(englishtohindi(user_input, 1))
    else:
        st.warning("Please enter some text for the API request.")  