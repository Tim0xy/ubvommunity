from pymongo import MongoClient
import certifi

"""
ca = certifi.where()
# В ковычки вставляем ссылку на подключение к БД, полученную выше
cluster = MongoClient(
    "mongodb+srv://nick:passQ@cluster0.9lm7j.mongodb.net/ForPeople?retryWrites=true&w=majority", tlsCAFile=ca
)

# Подключаемся к БД
db = cluster["ForPeople"]
# Подключаемся к таблице(коллекции)
workers = db["commands"]


for doc in workers.find():
    print (doc)
tok = doc['token']
print(tok)
token = tok
"""