import streamlit as st


st.title("Bool Queries")
code = """
GET account/_search
{"size": 0,
  "query": {
    "match": {
      "city": 
      {
        "query": "Jacksonburg"
      }
    }
  }
}

"""
st.write("**Requête 1 : Affiche les comptes qui ont comme ville Jacksonburg**")
st.code(code, language="json")
Result_1 =  """"

{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  }
}
Logique y'a que 63 habitants dans la ville de Jacksonburg.
"""
with st.expander("Result"):
    st.metric("Nombre de personnes ayant un compte à Jacksonburg", "1")
    st.markdown("Résultat afficher")
    st.code(Result_1, language="json")
st.write("**Requête 2 : Affiche les comptes qui ont 20 ans**")

code_2 = """
GET accounts/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "age": "20"
          }
        }
      ]
    }
  }
}

"""
st.code(code_2, language="json")
Result_2  = """
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 44,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "accounts",
        "_id": "LfmPOoYB2N4qgR1tODtY",
        "_score": 1,
        "_source": {
          "account_number": 157,
          "balance": 39868,
          "firstname": "Claudia",
          "lastname": "Terry",
          "age": 20,
          "gender": "F",
          "address": "132 Gunnison Court",
          "employer": "Lumbrex",
          "email": "claudiaterry@lumbrex.com",
          "city": "Castleton",
          "state": "MD"
        }
      },
      {
        "_index": "accounts",
        "_id": "RfmPOoYB2N4qgR1tODtY",
        "_score": 1,
        "_source": {
          "account_number": 215,
          "balance": 37427,
          "firstname": "Copeland",
          "lastname": "Solomon",
          "age": 20,
          "gender": "M",
          "address": "741 McDonald Avenue",
          "employer": "Recognia",
          "email": "copelandsolomon@recognia.com",
          "city": "Edmund",
          "state": "ME"
        }
      },
      {
        "_index": "accounts",
        "_id": "NfmPOoYB2N4qgR1tODxY",
        "_score": 1,
        "_source": {
          "account_number": 816,
          "balance": 9567,
          "firstname": "Cornelia",
          "lastname": "Lane",
          "age": 20,
          "gender": "F",
          "address": "384 Bainbridge Street",
          "employer": "Sulfax",
          "email": "cornelialane@sulfax.com",
          "city": "Elizaville",
          "state": "MS"
        }
      },
      {
        "_index": "accounts",
        "_id": "WfmPOoYB2N4qgR1tODxY",
        "_score": 1,
        "_source": {
          "account_number": 905,
          "balance": 29438,
          "firstname": "Schultz",
          "lastname": "Moreno",
          "age": 20,
          "gender": "F",
          "address": "761 Cedar Street",
          "employer": "Paragonia",
          "email": "schultzmoreno@paragonia.com",
          "city": "Glenshaw",
          "state": "SC"
        }
      },
      {
        "_index": "accounts",
        "_id": "pfmPOoYB2N4qgR1tODxY",
        "_score": 1,
        "_source": {
          "account_number": 95,
          "balance": 1650,
          "firstname": "Dominguez",
          "lastname": "Le",
          "age": 20,
          "gender": "M",
          "address": "539 Grace Court",
          "employer": "Portica",
          "email": "dominguezle@portica.com",
          "city": "Wollochet",
          "state": "KS"
        }
      },
      {
        "_index": "accounts",
        "_id": "w_mPOoYB2N4qgR1tODxY",
        "_score": 1,
        "_source": {
          "account_number": 172,
          "balance": 18356,
          "firstname": "Marie",
          "lastname": "Whitehead",
          "age": 20,
          "gender": "M",
          "address": "704 Monaco Place",
          "employer": "Sultrax",
          "email": "mariewhitehead@sultrax.com",
          "city": "Dragoon",
          "state": "IL"
        }
      },
      {
        "_index": "accounts",
        "_id": "2fmPOoYB2N4qgR1tODxY",
        "_score": 1,
        "_source": {
          "account_number": 228,
          "balance": 10543,
          "firstname": "Rosella",
          "lastname": "Albert",
          "age": 20,
          "gender": "M",
          "address": "185 Gotham Avenue",
          "employer": "Isoplex",
          "email": "rosellaalbert@isoplex.com",
          "city": "Finzel",
          "state": "NY"
        }
      },
      {
        "_index": "accounts",
        "_id": "6_mPOoYB2N4qgR1tODxY",
        "_score": 1,
        "_source": {
          "account_number": 273,
          "balance": 11181,
          "firstname": "Murphy",
          "lastname": "Chandler",
          "age": 20,
          "gender": "F",
          "address": "569 Bradford Street",
          "employer": "Zilch",
          "email": "murphychandler@zilch.com",
          "city": "Vicksburg",
          "state": "FL"
        }
      },
      {
        "_index": "accounts",
        "_id": "8_mPOoYB2N4qgR1tODxY",
        "_score": 1,
        "_source": {
          "account_number": 292,
          "balance": 26679,
          "firstname": "Morrow",
          "lastname": "Greene",
          "age": 20,
          "gender": "F",
          "address": "691 Nassau Street",
          "employer": "Columella",
          "email": "morrowgreene@columella.com",
          "city": "Sanborn",
          "state": "FL"
        }
      },
      {
        "_index": "accounts",
        "_id": "EfmPOoYB2N4qgR1tOD1Y",
        "_score": 1,
        "_source": {
          "account_number": 367,
          "balance": 40458,
          "firstname": "Elaine",
          "lastname": "Workman",
          "age": 20,
          "gender": "M",
          "address": "188 Ridge Boulevard",
          "employer": "Colaire",
          "email": "elaineworkman@colaire.com",
          "city": "Herbster",
          "state": "AK"
        }
      }
    ]
  }
}

"""
with st.expander("Result"):
    st.markdown("Résultat afficher")
    st.metric("Nombre de personnes ayant 20 ans", "20")
    st.code(Result_2, language="json")
st.write("")

code_3 = """
GET accounts/_search
{  "size" : 0,
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "state": "NY"
          }
        }
      ]
    }
  }
}
"""
st.write("**Requête 3 : Affiche les comptes qui ont le state = NY*")
st.code(code_3, language="json")
Result_3 = """
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 20,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  }
}
"""

with st.expander("Result"):
    st.markdown("Résultat afficher")
    st.metric("Nombre de personne dans l'Etat de Newyork", "20")
    st.code(Result_3, language="json")