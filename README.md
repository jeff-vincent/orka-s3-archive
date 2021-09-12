# Orka-s3-archive

Upload build artifacts to AWS s3 from your macOS VM in Orka with a simple POST request. 


## Usage
1. Set up your Orka env and kubectl. 
2. Populate the environment variables in `orka-s3-archive.yml`
3. Run: `kubectl apply -f orka-s3-archive.yml`
4. Upload build artifacts from your macOS VM with the following:
>```
>curl --verbose --header "Content-Type:multipart/form-data" --form "artifact=@/path/to/artifact.zip"  http://10.221.188.13/archive
>```

NOTE: the IP address `10.221.188.13` will need to be replaced with that of the node on which the Kubernetes Service `s3archive-service` is deployed in both the above line and in line number 14 of `orka-s3-archive.yml` itself.
