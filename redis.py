from pymongo import MongoClient

def get_client():
    client= MongoClient()
    return client['bets']
