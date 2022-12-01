import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

data_file_path = '/config/workspace/aps_failure_training_set1.csv'

# Database & Collection name
database_name = "db_aps"
collection_name = "colc_sensor"


if __name__ == "__main__":
    df = pd.read_csv(data_file_path)
    print(f"rows and columns: {df.shape}")

    # Convert dataframe to JSON to dump it in Mongodb
    df.reset_index(drop=True, inplace=True)

    json_record =list( json.loads( df.T.to_json() ).values() )    
    #print(json_record[0])

    # inserting to mongo db
    client[database_name][collection_name].insert_many(json_record)
    print("data inserted")