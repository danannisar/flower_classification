# flower_classification
Flower images classification using CNN


docker build -t flowers2-model .

error when using port 8080:8080
it seems the port 8080 is taken by some other application
-p 3000:3000 doesn't work because it maps the port 3000 on your computer to the port 3000 in the container
instead, it should be -p 3000:8080, then it'll map the port 3000 on the host to 8080 in the container


docker run -it --rm -p 3000:8080 flowers2-model:latest

repository URI
 "repositoryUri": "606791026272.dkr.ecr.us-east-1.amazonaws.com/flowers-tflite-images"


https://h2lpfof2pc.execute-api.us-east-1.amazonaws.com/test/predict