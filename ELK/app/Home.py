import streamlit as st

st.title("Mini projet Elasticsearch")
st.warning("L'appli n'est pas live car les serveurs sont KO")
st.write("Dans ce mini projet nous allons voir comment utiliser Elasticsearch pour la recherche de données")
st.write("**On dirait mais je suis pas sponsorisé par Streamlit. J'aimerai bien ^^**")
st.write("Les données ont été injectées dans Elasticsearch via Kibana")
st.write(" Le code est disponible ⤵️")
st.image("qrcode.png", width=200)
def page_0():
    st.empty()
def page_2():
    st.empty()

def page3():
    st.empty()

def page4():
     st.empty()

page_names_to_funcs = {
    "Home": page_0,
    "Indexation": page_2,
    "Question_2": page3,
    "cluster" :page4}