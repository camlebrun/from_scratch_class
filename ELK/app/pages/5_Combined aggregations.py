import streamlit as st

st.title("Combined aggregations")
st.write("Dans cette partie nous allons voir comment faire des aggregations combinées")
st.write("**Requête 1: Combien de femmes ont plus de 20 ans ?**")
code = """
GET accounts/_search
{ "size" : 0,
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "age": {
              "gt": 20
            }
          }
        },
        {
          "term": {
            "gender": "F"
          }
        }
      ]
    }
  }
}

"""

st.code(code, language="json")

result = """
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
}
"""
with st.expander("Result"):
    st.code(result, language="json")
st.write("**Requête 2: Affiche les soldes moyens des comptes par tranche d'âge de 10 ans**")
code2= """
GET accounts/_search
{
  "aggs": {
    "age_ranges": {
      "range": {
        "field": "age",
        "ranges": [
          { "to": 20 },
          { "from": 20, "to": 25 },
          { "from": 26, "to": 29 },
          { "from": 30, "to": 40 },
          { "from": 40, "to": 50 },
          { "from": 50, "to": 60 },
          { "from": 60, "to": 70 },
          { "from": 70, "to": 80 },
          { "from": 80, "to": 90 },
          { "from": 90 }
        ]
      },
      "aggs": {
        "avg_balance": {
          "avg": {
            "field": "balance"
          }
        }
      }
    }
  }
}
"""
st.code(code2, language="json")

result2 = """
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
    "max_score": 1,
    "hits": [
      {
        "_index": "accounts",
        "_id": "7vmPOoYB2N4qgR1tODpY",
        "_score": 1,
        "_source": {
          "index": {
            "_id": "1"
          }
        }
      },
      {
        "_index": "accounts",
        "_id": "7_mPOoYB2N4qgR1tODpY",
        "_score": 1,
        "_source": {
          "account_number": 1,
          "balance": 39225,
          "firstname": "Amber",
          "lastname": "Duke",
          "age": 32,
          "gender": "M",
          "address": "880 Holmes Lane",
          "employer": "Pyrami",
          "email": "amberduke@pyrami.com",
          "city": "Brogan",
          "state": "IL"
        }
      },
      {
        "_index": "accounts",
        "_id": "8PmPOoYB2N4qgR1tODpY",
        "_score": 1,
        "_source": {
          "index": {
            "_id": "6"
          }
        }
      },
      {
        "_index": "accounts",
        "_id": "8fmPOoYB2N4qgR1tODpY",
        "_score": 1,
        "_source": {
          "account_number": 6,
          "balance": 5686,
          "firstname": "Hattie",
          "lastname": "Bond",
          "age": 36,
          "gender": "M",
          "address": "671 Bristol Street",
          "employer": "Netagy",
          "email": "hattiebond@netagy.com",
          "city": "Dante",
          "state": "TN"
        }
      },
      {
        "_index": "accounts",
        "_id": "8vmPOoYB2N4qgR1tODpY",
        "_score": 1,
        "_source": {
          "index": {
            "_id": "13"
          }
        }
      },
      {
        "_index": "accounts",
        "_id": "8_mPOoYB2N4qgR1tODpY",
        "_score": 1,
        "_source": {
          "account_number": 13,
          "balance": 32838,
          "firstname": "Nanette",
          "lastname": "Bates",
          "age": 28,
          "gender": "F",
          "address": "789 Madison Street",
          "employer": "Quility",
          "email": "nanettebates@quility.com",
          "city": "Nogal",
          "state": "VA"
        }
      },
      {
        "_index": "accounts",
        "_id": "9PmPOoYB2N4qgR1tODpY",
        "_score": 1,
        "_source": {
          "index": {
            "_id": "18"
          }
        }
      },
      {
        "_index": "accounts",
        "_id": "9fmPOoYB2N4qgR1tODpY",
        "_score": 1,
        "_source": {
          "account_number": 18,
          "balance": 4180,
          "firstname": "Dale",
          "lastname": "Adams",
          "age": 33,
          "gender": "M",
          "address": "467 Hutchinson Court",
          "employer": "Boink",
          "email": "daleadams@boink.com",
          "city": "Orick",
          "state": "MD"
        }
      },
      {
        "_index": "accounts",
        "_id": "9vmPOoYB2N4qgR1tODpY",
        "_score": 1,
        "_source": {
          "index": {
            "_id": "20"
          }
        }
      },
      {
        "_index": "accounts",
        "_id": "9_mPOoYB2N4qgR1tODpY",
        "_score": 1,
        "_source": {
          "account_number": 20,
          "balance": 16418,
          "firstname": "Elinor",
          "lastname": "Ratliff",
          "age": 36,
          "gender": "M",
          "address": "282 Kings Place",
          "employer": "Scentric",
          "email": "elinorratliff@scentric.com",
          "city": "Ribera",
          "state": "WA"
        }
      }
    ]
  },
  "aggregations": {
    "age_ranges": {
      "buckets": [
        {
          "key": "*-20.0",
          "to": 20,
          "doc_count": 0,
          "avg_balance": {
            "value": null
          }
        },
        {
          "key": "20.0-25.0",
          "from": 20,
          "to": 25,
          "doc_count": 225,
          "avg_balance": {
            "value": 26969.075555555555
          }
        },
        {
          "key": "26.0-29.0",
          "from": 26,
          "to": 29,
          "doc_count": 149,
          "avg_balance": {
            "value": 24482.31543624161
          }
        },
        {
          "key": "30.0-40.0",
          "from": 30,
          "to": 40,
          "doc_count": 504,
          "avg_balance": {
            "value": 24982.29761904762
          }
        },
        {
          "key": "40.0-50.0",
          "from": 40,
          "to": 50,
          "doc_count": 45,
          "avg_balance": {
            "value": 27183.17777777778
          }
        },
        {
          "key": "50.0-60.0",
          "from": 50,
          "to": 60,
          "doc_count": 0,
          "avg_balance": {
            "value": null
          }
        },
        {
          "key": "60.0-70.0",
          "from": 60,
          "to": 70,
          "doc_count": 0,
          "avg_balance": {
            "value": null
          }
        },
        {
          "key": "70.0-80.0",
          "from": 70,
          "to": 80,
          "doc_count": 0,
          "avg_balance": {
            "value": null
          }
        },
        {
          "key": "80.0-90.0",
          "from": 80,
          "to": 90,
          "doc_count": 0,
          "avg_balance": {
            "value": null
          }
        },
        {
          "key": "90.0-*",
          "from": 90,
          "doc_count": 0,
          "avg_balance": {
            "value": null
          }
        }
      ]
    }
  }
}
"""
st.warning("Bon week-end !")
with st.expander("Show results"):
    st.code(result2, language="json")