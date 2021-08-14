import io
import os
import random
import string
import boto3
from bottle import Bottle, request

app = Bottle(__name__)
client = boto3.client(
    's3',
    region_name=os.environ['AWS_REGION_NAME'],
    aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
    aws_secret_access_key=os.environ['AWS_SECRET_KEY']
    )

def _generate_hash():
    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for i in range(10))
    
def _build_upload_filename(filename, hash):
    name, ext = os.path.splitext(filename)
    return f"{name}--{hash}{ext}"

def upload_to_s3(byte_stream, file):
    s3_bucket_name = os.environ['S3_BUCKET_NAME']
    hash = _generate_hash()
    filename = _build_upload_filename(file.filename, hash)
    client.upload_fileobj(byte_stream, s3_bucket_name, filename)

@app.route('/archive', method='POST')
def archive():
    try:
        file = request.files.get('artifact')
        byte_stream = io.BytesIO(file.file.read())
        upload_to_s3(byte_stream, file)
        return '0'
    except:
        return '1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888')
