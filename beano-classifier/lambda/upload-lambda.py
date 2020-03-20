import boto3
s3 = boto3.resource('s3')
# replace 'mybucket' with the name of your S3 bucket
s3.meta.client.upload_file('../beano-images/models/prod.tar.gz', 'owennewo-fastai-lesson2', './models/prod.tar.gz')