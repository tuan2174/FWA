import pandas as pd
from io import StringIO
from pymongo import MongoClient

class DataFrame:
    def toPandasDataFrame(self, csvString = None, mongoCursor = None):
        """ Add a csv string and return a pandas dataframe.
        \ncsvString: comma-delimited string
        \nmongoCursor: MongoDb cursor
        """
        if (csvString is not None):
            return pd.read_csv(StringIO(csvString), sep=",")
        if (mongoCursor is not None):
            list_cur = list(mongoCursor)
            return pd.DataFrame(list_cur)

def main():
    # Used as an example.
    dataFrame = DataFrame()
    df = dataFrame.toPandasDataFrame(csvString = """d1,d2
    1,2
    3,4""")
    print(df.head())

if __name__ == '__main__':
    main()

