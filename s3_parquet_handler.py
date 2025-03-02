import boto3
import pandas as pd
import pyarrow.parquet as pq

class S3ParquetHandler:
    """
    A class to handle reading and writing Parquet files from/to AWS S3
    """
    def __init__(self, bucket_name, aws_access_key_id=None, aws_secret_access_key=None, region_name='us-east-1'):
        """
        Initialize S3 client and resources
        
        :param bucket_name: Name of the S3 bucket
        :param aws_access_key_id: AWS Access Key ID (optional, can use environment variables)
        :param aws_secret_access_key: AWS Secret Access Key (optional, can use environment variables)
        :param region_name: AWS region name
        """
        # Create S3 client and resource
        self.s3_client = boto3.client(
            's3', 
            aws_access_key_id=aws_access_key_id, 
            aws_secret_access_key=aws_secret_access_key, 
            region_name=region_name
        )
        self.s3_resource = boto3.resource(
            's3', 
            aws_access_key_id=aws_access_key_id, 
            aws_secret_access_key=aws_secret_access_key, 
            region_name=region_name
        )
        self.bucket_name = bucket_name

    def read_parquet_from_s3(self, s3_key):
        """
        Read a Parquet file from S3 into a pandas DataFrame
        
        :param s3_key: Path to the Parquet file in the S3 bucket
        :return: pandas DataFrame
        """
        try:
            # Download the Parquet file to a local temporary file
            local_file_name = f'/tmp/{s3_key.split("/")[-1]}'
            self.s3_client.download_file(self.bucket_name, s3_key, local_file_name)
            
            # Read the Parquet file
            df = pd.read_parquet(local_file_name)
            return df
        except Exception as e:
            print(f"Error reading Parquet file from S3: {e}")
            return None

    def write_parquet_to_s3(self, dataframe, s3_key):
        """
        Write a pandas DataFrame to a Parquet file in S3
        
        :param dataframe: pandas DataFrame to write
        :param s3_key: Destination path in the S3 bucket
        """
        try:
            # Write to a local temporary file first
            local_file_name = f'/tmp/{s3_key.split("/")[-1]}'
            dataframe.to_parquet(local_file_name)
            
            # Upload to S3
            self.s3_client.upload_file(local_file_name, self.bucket_name, s3_key)
            print(f"Successfully uploaded Parquet file to s3://{self.bucket_name}/{s3_key}")
        except Exception as e:
            print(f"Error writing Parquet file to S3: {e}")

    def list_parquet_files(self, prefix=''):
        """
        List Parquet files in the S3 bucket
        
        :param prefix: Optional prefix to filter files
        :return: List of Parquet file keys
        """
        try:
            # List objects with .parquet extension
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name, 
                Prefix=prefix
            )
            
            parquet_files = [
                obj['Key'] for obj in response.get('Contents', []) 
                if obj['Key'].lower().endswith('.parquet')
            ]
            return parquet_files
        except Exception as e:
            print(f"Error listing Parquet files: {e}")
            return []

def main():
    # Example usage
    # Note: Replace with your actual bucket name and credentials
    handler = S3ParquetHandler(
        bucket_name='your-bucket-name',
        # aws_access_key_id='your-access-key',
        # aws_secret_access_key='your-secret-key'
    )
    
    # List Parquet files
    parquet_files = handler.list_parquet_files()
    print("Parquet files in bucket:", parquet_files)
    
    # Read a specific Parquet file (uncomment and modify as needed)
    # df = handler.read_parquet_from_s3('path/to/your/file.parquet')
    # print(df)

if __name__ == '__main__':
    main()
