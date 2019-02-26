this was a project I used to test out how to make a serverless application using cognito, api gateways, and lambda functions and s3.

the code itself is extremely hacky as I was just trying to get things to work.

right now I can host this folder on a s3 bucket and after creating a cognito account manually (there is code to make it
but I havn't figured out verificaiton yet so I still have to verify manually)

once you are authenticated with cognito you can request that a temporary ec2 instance gets spun up and it will discplay
the ip and password for you to log in when ready. the ec2 instance will terminate when it is shutdown so no need to log
into aws to clean up after yourself.

project uses cognito as authentication, and you use post requests to start lambda functions that spin up the ec2 instance.

This code is to be kept as a reference rather than to be used as the code itself is fragile and messy.