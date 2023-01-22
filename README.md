# Flower Images Classification using Deep Learning

Each kind of flowers are having their own distinctive features which distinguish them with other species. Those features such as colors, sepals, petals, stamens (anther and filament), and carpels (stigma, style, ovary). Images from five kinds of flowers are provided in training and test dataset, there are daisy, sunflower, dandelion, rose, and tulip. With Convolutional Neural Network, we can build an image classification model to classify an image flower to one of these flower species.

Dataset source: Kaggle https://www.kaggle.com/datasets/alxmamaev/flowers-recognition

## How to Use this Repo?
1. Clone this repo to your local with command `git clone`
2. This analysis performed using `Ubuntu 22.04` and `Python 3.9.13`. The training and hyperparameter tuning was ran with the help of Jupyter Notebook in Saturn Cloud, because it would be faster using GPU. The tutorial to set up Saturn Cloud can be followed with this [video](https://www.youtube.com/watch?v=WZCjsyV8hZE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=76).
3. Before running this analysis on your machine, install the right version of packages in `requirements.txt` with this syntax: `pip install -r requirements.txt`.
4. EDA, training and tuning the hyperparameter syntax is provided in `flowers_classification.ipynb`. 
5. Deployment steps provided below. 

## Deployment in Local and Cloud (Amazon Lambda)
1. Convert tensorflow model (`model_xception.h5`) to tflite model, so we could have smaller docker image size. The syntax for conversion can be seen in `tf-model.ipynb`. The result of the conversion, or the tflite model is `flowers_model.tflite`.
2. Function for predicting has been created in `lambda_function.py`, basically it loads the tflite model, obtain the output for image classification, and lambda handler for serverless (cloud) deployment.
3. Open Docker Desktop. Using Dockerfile that's been cloned, we can build the Docker Images `docker build -t flowers2-model .`
4. Without closing the Docker Desktop, run the Docker Images with specific port `docker run -it --rm -p 8080:8080 flowers2-model:latest`
   In my case, port 8080 in my computer has been taken by other apps so it gave me this error:
   
   ![Error using port 8080 in my computer](images/docker-run-error-8080.png)
   
   So the command changed to `docker run -it --rm -p 3000:8080 flowers2-model:latest`, it'll map the port 3000 on the host to 8080 in the container.
   
   ![Success running docker](images/docker-run-success.png)
5. Doing the test with `test.py`. There are two deployment URL in this file, make sure you use the first one for **local deployment**, remove the hash tag #.


repository URI
 "repositoryUri": "606791026272.dkr.ecr.us-east-1.amazonaws.com/flowers-tflite-images"


https://h2lpfof2pc.execute-api.us-east-1.amazonaws.com/test/predict