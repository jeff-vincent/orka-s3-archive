docker run \
-e AWS_REGION_NAME="us-west-2" \
-e S3_BUCKET_NAME="<bucket_name>" \
-e AWS_ACCESS_KEY="<access_key>" \
-e AWS_SECRET_KEY="<secret_key>" \
-p 8888:8888 \
orka-s3-connect:latest