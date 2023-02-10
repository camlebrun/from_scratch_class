import streamlit as st

st.title("Metrics Queries")
code = """
GET accounts/_search 
{ "size": 0,
  "aggs": {
    "type_count": {
      "cardinality": {
        "field": "gender"
      }
    }
    }
"""
st.write("**Requête 1: Combien de type de genre différents y a-t-il dans la base de données ?**")
st.write("La requête ci-dessous permet de compter le nombre de type de genre différents dans la base de données")
st.write("Y'a t'il des personnes dont leurs genres ne sont pas renseignés ? Notre base de données est elle inclusive ?")
st.code(code, language="json")

result = """
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
      "value": 2000,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "type_count": {
      "value": 2   <== Le résultat est ici, pas de NaN 
      ou de personnes non-bianaires je suis tristes :(
    }
  }
}

"""

with st.expander("Result"):
    st.metric("Nombre de type de genre différents", "2")
    st.markdown("Résultat afficher")
    st.code(result, language="json")

code_2 = """
GET accounts/_search 
{ 
  "size": 0,
  "aggs": {
    "max_age": {
      "max": {
        "field": "age"
      }
    }
  }
}


"""
st.write("**Requête 2: Quel est l'âge maximum des comptes ?**")
st.code(code_2, language="json")

result_2 = """
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
      "value": 2000,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "max_age": {
      "value": 40  <== Le résultat est ici,
       encore 24 jusqu'à la retraite (oui je troll)
    }
  }
}"""
with st.expander("Result"):
    st.markdown("Résultat afficher")
    st.metric("L'âge maximum des comptes", "40")
    st.code(result_2, language="json")
st.write("**Requête 3: Quel est l'âge moyen des comptes ?**")
code_3 = """
GET accounts/_search 
{ 
  "size": 0, 
  "aggs": {
    "avg_age": {
      "avg": {
        "field": "age"
      }
    }
  }
}
"""

result_3 = """
{
  "took": 18,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 2000,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "avg_age": {
      "value": 30.171  <== Le résultat est ici 
       (j'ai pas fait un arrondi, c'est pas très joli)
    }
  }
}
"""
st.code(code_3, language="json")
with st.expander("Result"):
    st.metric("L'âge moyen des comptes", "30 ans ")
    st.markdown("Résultat afficher")
    st.code(result_3, language="json")
