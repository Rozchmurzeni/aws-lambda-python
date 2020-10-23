from calculator import calculate


def handle(event, context):
    result = calculate()

    return {
        'statusCode': 200,
        'body': result,
    }
