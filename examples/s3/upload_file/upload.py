import json
import boto3

def lambda_handler(event, context):

	# Setup target upload bucket and folder
	bucket_name = "my-bucket"
	bucket_path = "my-folder/"
	target_filename = "event.json"

	# upload_filename is the remote location in S3
    upload_filename = bucket_path + target_filename

	# output_path here is the location in /tmp to store the event
    output_path = "/tmp/" + target_filename
    
	# Read in the event object, convert it to json and dump it
	# to the output_path in /tmp
    output_filehandle = file(output_path, "w")
    output_filehandle.writelines(json.dumps(event))
    output_filehandle.close()
    
	# Setup the s3 client and upload the file
    s3 = boto3.client("s3")
    s3.upload_file(output_path, bucket_name, upload_filename)

    return 'saved to {0}'.format(upload_filename)
