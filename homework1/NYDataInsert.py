import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('green_tripdata_2019-09.csv', nrows=200)

df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
test =engine.connect()

print(pd.io.sql.get_schema(df, name='green_tripdata_2019-09', con=engine))

df_iter = pd.read_csv('green_tripdata_2019-09.csv', iterator=True, chunksize=100000)

for df in df_iter:
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    df.to_sql(name = 'green_taxi_data', con=engine, if_exists='append')
    print('inserted chunk')

df_iter2 = pd.read_csv('taxi+_zone_lookup.csv', iterator=True, chunksize=100000)

for df in df_iter2:
    df.to_sql(name = 'taxi_zone_lookup', con=engine, if_exists='append')
    print('inserted chunk')

test.close()
engine.dispose()