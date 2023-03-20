def get_data(event: dict, context):
    name = event["queryStringParameters"]["name"]
    return {
        'statusCode': 200,
        'body': str({'name': name})
    }
