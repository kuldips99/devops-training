import boto3

# Create an S3 client
s3 = boto3.client('s3')

filename = 'C:\Users\Administrator\Downloads\Python_Boto3-master\S3.py'
bucket_name = 'devops-training08'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.

try:
	response = s3.upload_file(filename, bucket_name, filename)
	print (response)
except Exception as error:
	print (error)
