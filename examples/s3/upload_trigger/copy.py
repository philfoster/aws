import boto3

def lambda_handler(event, context):
	# This should be setup to run as a trigger on a new 
	# file arriving in as S3 bucket

	# Setup local variables
	target_folder = "incoming/copy/"

	# Configure the s3 client
	s3 = boto3.client("s3")

	# Parse the event
	incoming_file = event["Records"][0]["s3"]["object"]["key"]
	incoming_bucket = event["Records"][0]["s3"]["bucket"]["name"]

	# Strip off everything up to the last slash (strip path)
	file_basename = incoming_file[incoming_file.rfind("/") + 1:]
	local_file = "/tmp/" + file_basename

	# Download locally to get the file
	s3.download_file(incoming_bucket, incoming_file, local_file)

	# Process the file locally

	# setup the upload location
	upload_location = target_folder + file_basename

	# Now push it back up to the new path
	s3.upload_file(local_file, incoming_bucket, upload_location)

	return "wrote '{0}' to '{1}'".format(file_basename, upload_location)
