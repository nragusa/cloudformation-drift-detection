# CloudFormation Drift Detection

This is a sample application which will update the Drift Detection status across all stacks within
a given region. 

To deploy this, you'll first need to create an S3 bucket. You will use this bucket to store the Lambda build
artifact. 

Once the S3 bucket is created, you can 

```bash
# Create S3 bucket
aws s3 mb s3://BUCKET_NAME

# Build this lambda function into an artifact
sam build

# Package and upload to S3 as an artifact
sam package \
    --output-template-file packaged.yaml \
    --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME

# Deploy SAM template as a CloudFormation stack
sam deploy \
    --template-file packaged.yaml \
    --stack-name REPLACE_WITH_USEFUL_STACK_NAME \
    --capabilities CAPABILITY_IAM
```

