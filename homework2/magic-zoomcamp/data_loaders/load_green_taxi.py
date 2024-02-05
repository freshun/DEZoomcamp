import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float,
                }


parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']


@data_loader
def load_data_from_api(*args, **kwargs):
    final_qtr_2020_green_taxi = pd.DataFrame()
    for i in range(10,13):
        print(i)
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{i}.csv.gz'
        df = pd.read_csv(url, sep=',', compression='gzip', dtype = taxi_dtypes, parse_dates = parse_dates)
        final_qtr_2020_green_taxi = pd.concat([final_qtr_2020_green_taxi, df])

        
    
    # df = pd.read_csv(url, sep=',', compression='gzip', dtype = taxi_dtypes, parse_dates = parse_dates)
    # df = df[(df['lpep_pickup_datetime'] > pd.Timestamp('2021-10')) & (df['lpep_pickup_datetime'] <= pd.Timestamp('2021-11'))]
    return final_qtr_2020_green_taxi
