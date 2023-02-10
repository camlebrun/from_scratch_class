import streamlit as st
st.title("Indexation")

st.write("Dans cette partie nous allons voir comment indexé des données dans Elasticsearch")
st.write("Création d'un index et modification de l'index")
st.write("L'index créee par ELK n'est pas adapter pour notre projet, il faut donc le modifier")
st.write("**On va créer un index temporaire pour y injecter des données puis on va créer un index définitif avec les bon mapping. Qui servira à la suite du projet**")
code = """
GET account_temp <== Voir l'index fourni par ELK

PUT  account_temp <== Création d'un index temporaire
{
  "mappings": {
    "properties": {
      "account_number" : {
        "type" : "integer"
      }, 
      "age" : {
        "type" : "integer"
      },
      "gender" : {
        "type" : "keyword"
      }
    }
  }
}

POST _reindex <== On copie les données de l'index temporaire vers l'index définitif
{
  "source": {
    "index": "account_temp"
}, "dest": {
    "index": "accounts"
  }
}

GET accounts <== On vérifie que les données ont bien été copiées
"""

st.code(code, language="json")
st.image("app/coucou.gif")
Result = """"


{
  "accounts": {
    "aliases": {},
    "mappings": {
      "_meta": {
        "created_by": "file-data-visualizer"
      },
      "properties": {
        "account_number": {
          "type": "long"
        },
        "address": {
          "type": "keyword"
        },
        "age": {
          "type": "long"
        },
        "balance": {
          "type": "long"
        },
        "city": {
          "type": "keyword"
        },
        "email": {
          "type": "keyword"
        },
        "employer": {
          "type": "keyword"
        },
        "firstname": {
          "type": "keyword"
        },
        "gender": {
          "type": "keyword"
        },
        "index": {
          "properties": {
            "_id": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "lastname": {
          "type": "keyword"
        },
        "state": {
          "type": "keyword"
        }
      }
    },
    "settings": {
      "index": {
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_content"
            }
          }
        },
        "number_of_shards": "1",
        "provided_name": "accounts",
        "creation_date": "1676019709872",
        "number_of_replicas": "1",
        "uuid": "tDO2AWmLQZ6FKH9re_MNfw",
        "version": {
          "created": "8060199"
        }
      }
    }
  }
}
"""

with st.expander("Result"):
    st.markdown("It's working !")
    st.code(Result, language="json")
