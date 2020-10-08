# Practice with Streamlit

# Imports
import streamlit as st
import numpy as np
import pandas as pd
import spacy

# https://towardsdatascience.com/build-quick-and-beautiful-apps-using-streamlit-85f32ed01fb2

nlp_lg = spacy.load('en_core_web_lg')
# st.write("The Whole Dataframe is here:")
# The final dataframe
data = pd.read_csv('./data/chewy.csv')
# st.dataframe(data)

# Getting all of the data for the comparison
# @st.cache (hash_funcs={spacy.lang.en.English: my_hash_func})
# def create_list_docs(data):
list_docs = []
for i in range(len(data)):
    if data['combined_text'][i] != '':
        doc = nlp_lg("u" + str(data['combined_text'][i]) + "'")
        list_docs.append(doc)
    # return list_docs

# list_docs = create_list_docs(data)

# @st.cache # This functionwill be cashed
# Calculates how similar each toy is the to the text and scores them
# @st.cache # This functionwill be cashed
# @st.cache
def calculate_similarity_with_spacy(nlp, df, user_text, n=6):
    # Calculate similarity with Spacy
    list_sim = []
    toy_score = []
    doc1 = nlp(user_text + "'")
    vectors = doc1.vector # not quite sure if this will be useful bc not sure how to use the .most_similar here
    for i in df.index:
        try:
            doc2 = list_docs[i]
            score = doc1.similarity(doc2)
            list_sim.append((doc1, doc2, score))
            toy_score.append((score, df['title'][i], df['cat'][i]))
        except:
            continue
    return toy_score

# Finds the toys and ranks them from highest to lowest
# @st.cache
# @st.cache
def dog_toy_recommender(nlp, data, user_text):
    ranking_list = calculate_similarity_with_spacy(nlp_lg, data, user_text=user_text)
    ranked_dict = {}
    for i, score_toy in enumerate(ranking_list):
    #     print(i, score_toy[0], ranking_list[i][2])
        ranked_dict[score_toy[0]] = {i : [ranking_list[i][2], score_toy[1]]}
    final_dict = {}
    for i in sorted(ranked_dict, reverse=True) :
        final_dict[i] =  ranked_dict[i]
    return final_dict


# Runs the recommender
# @st.cache(hash_funcs={spacy.tokens.doc.Doc: dog_toy_recommender})
def run_recommender(nlp, data, user_text):
    toys = dog_toy_recommender(nlp_lg, data, user_text)
    toy_list = []
    for i in list(toys)[:10]:
        toy_list.append(toys)
    return toy_list

def main():

    analysis = st.sidebar.selectbox('Select an Option', ['Introduction', 'Data Analysis', 'Recommendation System'])

    if analysis == 'Introduction':

        # Adding a title
        st.title("Dog Toy Recommendation System")

        # Adding a subtitle, explaining the purpose of this app
        st.write("By Haley Taft")
        st.write("This Recommendation System takes a description of one's dog and returns the ten best toys for your dog from Chewy, an online pet store.")
        st.write("This app was created as part of a final capstone project from when I was a student at General Assembly in their Data Science Immersive course.")

        st.subheader("Problem Statement:")
        st.write("Based off the reviews, descriptions and key benefits of dog toys, and a person's description of their dog's general personality, I will create a recommendation system that will suggest ten dog toys that the dog might enjoy based off the similarity in what was written and the text provided about each toy.")

        st.subheader("Quick Summary:")
        st.write("Using Selenium and BeautfiulSoup, I scraped dog toys from Chewy it the chew, fetch, plush, interactive and rope & toy categories. I then used spaCy to tokenize, vectorize and then compare a user's input with the description, key benefits and a reviews from each toy to find the most similar toys to the provided dog description.")

        st.subheader("What to Expect:")
        st.write("From this system, you will receive the ten toys that seem to match the closest with the description of one's dog provided in the input.")

        # st.subheader("What I Hope to Add in the Future:")
        # st.write("Right now, my system only works off the text provided from the ")

    # Taking a look at the data and EDA
    elif analysis == 'Data Analysis':
        st.title("Let's take a Look at the Data")

        st.write("This data includes the dog toys' title, price, description, key benefits, rating, reviews, category and subcategory, combined text, number of sentences and number of words in combined text, the tokenized combined text with stop words removed, the tokenized vectors and average vectors.")

        st.subheader('Take a look at the dataframe:')

        data = pd.read_csv('./data/chewy.csv')
        data

        # ADD IN EDA STUFF ONCE DONE
        st.subheader('General Dataset stuff --FIX THIS TITLE')

        st.subheader('Most Common Words')

        st.subheader('Overall Rating Distrubtion by Categories')

        st.subheader('Average Vector Distribution by Categories')

    elif analysis == "Recommendation System":
        st.title("The System Itself")

        st.write("To use this system you will need to describe your dog's personality and some things about him or her. If you need some help with what sort of things to add, use the questions listed below as reference.")
        st.write("Note: For better results, try to only include what your dog IS like rather than what IS NOT like. This will help the model to make better predictions.")

        st.write("Questions to Consider: ")
        '''
        - What type of dog do you have?
         - Is your dog a puppy, or older?
         - Is your dog super energetic and playful or calmer?
         - Would you say your dog is smarter than most dogs?
         - Does your dog like to chase after toys, cuddle toys, or chew on them?
         - Does your dog get pretty bored after playing with a toy for a bit?
         - Does your dog already have an ideal toy that is their absolute favorite? (If yes, describe it.)
        '''

        # The actual System

        # defining the spaCy model

        # https://discuss.streamlit.io/t/how-to-take-text-input-from-a-user/187
        user_text = st.text_input("Insert your response here:")
        # user_input

        if st.button("Let's Find Some toys!"):

            toy_list = run_recommender(nlp_lg, data, user_text)
            st.success(toy_list)
            # st.dataframe(toy_list)



if __name__ == '__main__':
    main()
