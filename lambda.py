import boto3

def lambda_handler(event, context):
    pipeline_name = "my-pipeline"  # Change this

    client = boto3.client('codepipeline')

    response = client.start_pipeline_execution(
        name=pipeline_name
    )

    return {
        'statusCode': 200,
        'body': f'Pipeline {pipeline_name} triggered successfully!'
    }
