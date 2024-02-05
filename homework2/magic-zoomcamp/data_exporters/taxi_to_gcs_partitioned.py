from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
import os
import pyarrow as pa
import pyarrow.parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/mage-zoomcamp-demo-key/elemental-leaf-411220-9c4fe2a5ffb4.json'

# config_path = path.join(get_repo_path(), 'io_config.yaml')
config_profile = 'zoomcamp-gcp-acct'
bucket_name = 'fe-magezoomcamp-6942069'
object_key = 'nyc_taxi_data.parquet'
project_id = 'elemental-leaf-411220'
table_name = 'nyc_taxi_data'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data_to_google_cloud_storage(data, *args, **kwargs) -> None:

    data['tpep_pickup_datetime'] = data['tpep_pickup_datetime'].dt.date

    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols = ['tpep_pickup_datetime'],
        filesystem = gcs
    )

    # GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
    #     df,
    #     bucket_name,
    #     object_key,
    # )
