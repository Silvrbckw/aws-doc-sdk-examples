# This code is a sample only. Not for use in production.
#
# Author: Katreena Mullican
# Contact: mullicak@amazon.com
#
import boto3
import os
import json

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
dynamodb = boto3.client('dynamodb')

def handler(event, context):
    bucket_name = (os.environ['BUCKET_NAME'])
    key = event['Records'][0]['s3']['object']['key']
    image = {
        'S3Object': {
            'Bucket': bucket_name,
            'Name': key
            }
        }

    try:
        # Calls Amazon Rekognition DetectLabels API to classify images in Amazon Simple Storage Service (Amazon S3).
        response = rekognition.detect_labels(Image=image, MaxLabels=10, MinConfidence=70)

        # Print response to console, visible with Amazon CloudWatch logs.
        print(key,response["Labels"])

        # Write results to JSON file in bucket results folder.
        json_labels = json.dumps(response["Labels"])
        filename = os.path.basename(key)
        filename_prefix = os.path.splitext(filename)[0]
        obj = s3.put_object(
            Body=json_labels,
            Bucket=bucket_name,
            Key=f"results/{filename_prefix}.json",
        )

        db_labels = json.loads(json_labels)
        db_result = [label["Name"] for label in db_labels]
        # Write results to DynamoDB.
        dynamodb.put_item(TableName=(os.environ['TABLE_NAME']),
            Item = {
                'image_name':{'S': key},
                'labels':{'S': str(db_result)}
           }
        )

        return response

    except Exception as e:
        print(e)
        print(f"Error processing object {key} from bucket {bucket_name}. ")
        raise e