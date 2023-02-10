import streamlit as st
st.title("Bucket Aggregation")
st.markdown("<h4>Pas sponso par KFC 🍗</h4>", unsafe_allow_html=True)
st.write("Dans cette partie nous allons voir comment utiliser les buckets aggregations pour la recherche de données")

code = """
GET accounts/_search
{
  "size" :0,
  "aggs": {
    "age": {
      "histogram": {
        "field": "age",
        "interval": 5
      }
    }
  }
}
"""

st.write("**Requête 1: Affiche les ages des comptes par tranche de 5 ans**")
st.code(code, language="json")

result = """
{
  "took": 3,
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
    "age": {
      "buckets": [
        {
          "key": 20,
          "doc_count": 225  <== Le résultat est ici 
        },
        {
          "key": 25,
          "doc_count": 226  <== Le résultat est ici 
        },
        {
          "key": 30,
          "doc_count": 259 <== vous avez compris le principe
        },
        {
          "key": 35,
          "doc_count": 245 <== vous avez compris le principe
        },
        {
          "key": 40,
          "doc_count": 45 <== vous avez compris le principe
        }
      ]
    }
  }
}
"""
with st.expander("Result"):
  st.code(result, language="json")
st.write("**Requête 2: Affiche les employeurs**")

code_2 = """"
GET accounts/_search
{ "size": 0, 
  "aggs": {
    "employer": {
      "terms": { "field": "employer" }
    }
  }
}
"""
result_2 = """
{
  "took": 15,
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
    "employer": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 989,
      "buckets": [
        {
          "key": "Xurban",
          "doc_count": 2 <== vous avez compris le principe
        },
        {
          "key": "Accel",
          "doc_count": 1 <== vous avez compris le principe
        },
        {
          "key": "Accidency",
          "doc_count": 1 <== vous avez compris le principe
        },
        {
          "key": "Accruex",
          "doc_count": 1 <== vous avez compris le principe
        },
        {
          "key": "Accufarm",
          "doc_count": 1 <== vous avez compris le principe
        },
        {
          "key": "Accupharm",
          "doc_count": 1 <== vous avez compris le principe
        },
        {
          "key": "Accuprint",
          "doc_count": 1 <== vous avez compris le principe
        },
        {
          "key": "Accusage",
          "doc_count": 1 <== vous avez compris le principe
        },
        {
          "key": "Acium",
          "doc_count": 1 <== Bref 
        },
        {
          "key": "Aclima",
          "doc_count": 1 
        }
      ]
    }
  }
}"""
st.code(code_2, language="json")
with st.expander("Result"):
    st.code(result_2, language="json")

st.write("**Requête 3: Affiche les soldes entre 1000 et 3500 avec un pas de 500*")
code_3 = """
GET accounts/_search
{ "size" : 0,
  "aggs": {
    "balance_range": {
      "range": {
        "field": "balance",
        "ranges": [
          { "to": 1000.0 },
          { "from": 1000.0, "to": 1500.0 },
          { "from": 1500.0, "to": 2000.0 },
          { "from": 2000.0, "to": 2500.0 },
          { "from": 2500.0, "to": 3000.0 },
          { "from": 3000.0, "to": 3500.0 },
          { "from": 3500.0 } 
        ]
      }
    }
  }
}


"""
st.code(code_3, language="json")
result_3 = """
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
    "balance_range": {
      "buckets": [
        {
          "key": "*-1000.0",
          "to": 1000,
          "doc_count": 0
        },
        {
          "key": "1000.0-1500.0",
          "from": 1000,
          "to": 1500,
          "doc_count": 13 <== vous avez compris le principe
        },
        {
          "key": "1500.0-2000.0",
          "from": 1500,
          "to": 2000,
          "doc_count": 6
        },
        {
          "key": "2000.0-2500.0",
          "from": 2000,
          "to": 2500,
          "doc_count": 6
        },
        {
          "key": "2500.0-3000.0",
          "from": 2500,
          "to": 3000,
          "doc_count": 7
        },
        {
          "key": "3000.0-3500.0",
          "from": 3000,
          "to": 3500,
          "doc_count": 16
        },
        {
          "key": "3500.0-*",
          "from": 3500,
          "doc_count": 952
        }
      ]
    }
  }
}"""
with st.expander("Result"):
    st.image("app/bo.gif")
    st.code(result_3, language="json")
    