if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

new_columns = ['vendor_id',
                'lpep_pickup_datetime',
                'lpep_dropoff_datetime',
                'store_and_fwd_flag',
                'ratecode_id',
                'pu_location_id',
                'do_location_id',
                'passenger_count',
                'trip_distance',
                'fare_amount',
                'extra',
                'mta_tax',
                'tip_amount',
                'tolls_amount',
                'ehail_fee',
                'improvement_surcharge',
                'total_amount',
                'payment_type',
                'trip_type',
                'congestion_surcharge']

@transformer
def transform(data, *args, **kwargs):
    # Specify your transformation logic here
    data.columns = new_columns
    data = data[(data['passenger_count'] > 0)]
    data = data[data['trip_distance'] != 0]
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime'], format= '%Y-%m-%d').dt.date
    
    return data


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
    assert output['vendor_id'] is not None
    passenger_count = len(output[output['passenger_count'] > 0])
    trip_distance = len(output[output['trip_distance'] > 0])
    assert passenger_count > 0, 'Error with passenger count'
    assert trip_distance > 0, 'Error with trip distance'
