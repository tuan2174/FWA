from pymongo import MongoClient, ReplaceOne
import dataFrame as df
from datetime import datetime, timedelta

class EntityLoad:
    """ Load entity records from MongoDb.
        \nmongoDbConnStr: MongoDb connection string.
    """
    def __init__(self, mongoClient):
        """Constructor. 
        pytest cannot mock MongoClient(connStr), therefore use MongoClient for constructor to make it unit testable.
        """
        self.__mongoClient = mongoClient
 
    def load(self, collection, query = {}):
        """load data from MongoDb."""
        db = self.__mongoClient.get_database("entity_store")
        cursor = db.get_collection(collection).find(query) #.sort("_id", 1})       
        return df.DataFrame().toPandasDataFrame(mongoCursor=cursor)

def main():
    import pandas as pd
    entityLoad = EntityLoad(MongoClient("127.0.0.1:27017"))
    startdate = datetime.datetime.strptime("2024-10-01",'%Y-%m-%d')
    loadedDf = entityLoad.load("entity_claims", { "EntityTimestamp": {'$gte': startdate} })
    print(loadedDf)


if __name__ == '__main__':
    main()
