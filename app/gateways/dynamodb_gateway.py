import os
import boto3
import itertools

from boto3.dynamodb.conditions import Key

class DynamodbGateway():
    """
    usage:

    response = DynamodbMappingGateway.query_by_partition_key(
        table_name=table_name,
        partition_key_name="mms_product_hierarchy_code",
        partition_key_query_value=partition_key_query_value
    )

    for item in response:
    """
    @classmethod
    def query_by_partition_key(cls, table_name, partition_key_name, partition_key_query_value):
        print(f"Reading from table {table_name}")
        dynamodb = boto3.resource('dynamodb', region_name=os.getenv('DYNAMODB_REGION_NAME'))
        table = dynamodb.Table(table_name)

        response = table.query(
            KeyConditionExpression=Key(partition_key_name).eq(partition_key_query_value)
        )

        print("=====")
        print("DynamoDB")
        print(response)
        print("=====")


        return response['Items']

    @classmethod
    def grouper(cls, iterable, n, fillvalue=None):
        "Collect data into fixed-length chunks or blocks"
        # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return itertools.zip_longest(*args, fillvalue=fillvalue)

    @classmethod
    def upsert(cls, table_name, mapping_data):
        print(f"Inserting into table {table_name}")
        dynamodb = boto3.resource('dynamodb', region_name=os.getenv('DYNAMODB_REGION_NAME'))
        table = dynamodb.Table(table_name)

        for group in cls.grouper(mapping_data, 100):
            batch_entries = list(filter(None.__ne__, group))

            print("=====")
            print("WRITING THIS BATCH in batches of 100")
            print(batch_entries)
            print("=====")

            with table.batch_writer(overwrite_by_pkeys=["card_number",]) as batch:
                for entry in batch_entries:
                    batch.put_item(
                        Item = entry
                    )
