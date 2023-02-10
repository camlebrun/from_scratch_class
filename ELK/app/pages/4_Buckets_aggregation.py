import streamlit as st
st.title("Question 3")
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

st.write("Requête 1: Affiche les ages des comptes par tranche de 5 ans")
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
          "doc_count": 225
        },
        {
          "key": 25,
          "doc_count": 226
        },
        {
          "key": 30,
          "doc_count": 259
        },
        {
          "key": 35,
          "doc_count": 245
        },
        {
          "key": 40,
          "doc_count": 45
        }
      ]
    }
  }
}
"""
with st.expander("Result"):
    st.code(result, language="json")
st.write("Requête 2: Affiche les employeurs des comptes")
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
          "doc_count": 2
        },
        {
          "key": "Accel",
          "doc_count": 1
        },
        {
          "key": "Accidency",
          "doc_count": 1
        },
        {
          "key": "Accruex",
          "doc_count": 1
        },
        {
          "key": "Accufarm",
          "doc_count": 1
        },
        {
          "key": "Accupharm",
          "doc_count": 1
        },
        {
          "key": "Accuprint",
          "doc_count": 1
        },
        {
          "key": "Accusage",
          "doc_count": 1
        },
        {
          "key": "Acium",
          "doc_count": 1
        },
        {
          "key": "Aclima",
          "doc_count": 1
        }
      ]
    }
  }
}"""
with st.expander("Result"):
    st.code(result_2, language="json")
st.write("Requête 3: Affiche les balances des comptes par tranche de 100")
code_3 = """
GET accounts/_search
{ "size" : 0,
  "aggs": {
    "balance_range": {
      "range": {
        "field": "balance",
        "ranges": [
          { "to": 100.0 },
          { "from": 100.0, "to": 200.0 },
          { "from": 20000.0 }
        ]
      }
    }
  }
}

"""

result_3 = """
{
  "took": 6,
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
          "key": "*-100.0",
          "to": 100,
          "doc_count": 0
        },
        {
          "key": "100.0-200.0",
          "from": 100,
          "to": 200,
          "doc_count": 0
        },
        {
          "key": "20000.0-*",
          "from": 20000,
          "doc_count": 619
        }
      ]
    }
  }
}"""
with st.expander("Result"):
    st.code(result_3, language="json")
    