import streamlit as st
st.title("Indexation")
st.write("Dans cette partie nous allons voir comment indexé des données dans Elasticsearch")
code = """GET account_temp

PUT  account_temp
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

POST _reindex
{
  "source": {
    "index": "account_temp"
}, "dest": {
    "index": "account"
  }
}

GET accounts
"""

st.code(code, language="json")
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
    st.markdown("This is an explanation of the code")
    st.code(Result, language="json")
