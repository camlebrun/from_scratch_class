import streamlit as st

st.title("Bool Queries")
code = """
GET account_f/_search 
{ "size": 0,
  "aggs": {
    "type_count": {
      "cardinality": {
        "field": "gender"
      }
    }
    }
"""
st.write("Requête 1: Combien de type de genre différents y a-t-il dans la base de données ?")
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
      "value": 2
    }
  }
}

"""

with st.expander("Result"):
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
st.write("Requête 2: Quel est l'âge maximum des comptes ?")
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
    "avg_age": {
      "value": 40
    }
  }
}"""
with st.expander("Result"):
    st.markdown("Résultat afficher")
    st.code(result_2, language="json")
st.write("Requête 3: Quel est l'âge moyen des comptes ?")
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
with st.expander("Result"):
    st.markdown("Résultat afficher")
    st.code(result_3, language="json")
