import pandas as pd
import boto3
import io
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get file details from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Check if the file is in the incoming folder
    if not key.startswith('incoming/'):
        return {'body': 'File not in incoming folder, ignoring.'}

    # 1. Read CSV from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(response['Body'])

    # 2. Process Data
    df['revenue'] = df['quantity'] * df['price']
    summary = df.groupby('city')['revenue'].sum().reset_index()
    summary = summary.sort_values(by='revenue', ascending=False)

    # 3. Prepare Output
    csv_buffer = io.StringIO()
    summary.to_csv(csv_buffer, index=False)
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    output_key = f"reports/city_revenue_summary_{date_str}.csv"

    # 4. Upload back to S3
    s3.put_object(Bucket=bucket, Key=output_key, Body=csv_buffer.getvalue())

    return {'statusCode': 200, 'body': f'Success! Saved to {output_key}'}
