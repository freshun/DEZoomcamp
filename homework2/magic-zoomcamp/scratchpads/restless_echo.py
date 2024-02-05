"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
from mage_ai.data_preparation.variable_manager import get_variable


df = get_variable('green_taxi_etl', 'load_green_taxi', 'output_0')
# df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
# df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])
df_columns = df.columns.tolist()
df = df[(df['passenger_count'] > 0)]
df = df[df['trip_distance'] != 0]

print(pd.unique(df['VendorID']))  ### Answer to number 4
