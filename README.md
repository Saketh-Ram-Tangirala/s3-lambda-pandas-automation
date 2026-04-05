# s3-lambda-pandas-automation
# Automate Order Report Generation Using S3 & Lambda

## Project Overview
This project automates the generation of a city-wise revenue report. When a CSV file is uploaded to an S3 bucket, an AWS Lambda function is triggered to process the data using Pandas and save a summary report back to S3.

## Architecture
- **Storage**: AWS S3 (Folders: `incoming/` and `reports/`)
- **Compute**: AWS Lambda (Python 3.11)
- **Library**: AWS SDK Pandas Layer (Managed Layer)
- **Trigger**: S3 ObjectCreated Event (Prefix: `incoming/`)

## Setup Instructions
1. Create an S3 bucket with `incoming/` and `reports/` folders.
2. Create a Lambda function and attach the `AWSSDKPandas-Python311` layer (using the Stockholm region ARN).
3. Add an S3 Trigger to the Lambda for the `incoming/` prefix.
4. Update the Lambda IAM Role to include `AmazonS3FullAccess`.
5. Upload `orders.csv` to the `incoming/` folder to trigger the report generation.

## Screenshots
Check the `/screenshots` folder for:
- S3 Bucket structure
- Lambda Trigger configuration
- Generated report in S3
- CloudWatch execution logs
