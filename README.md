# Autistic Child Classification
This is one of my machine learning project, focused to classify autistic and non-autistic child based on face image. This project is already can be accessed in REST API created using Fastapi. This project is created using Convolutional Neural Network (CNN).

## Requirements
This project use an external library such as pandas, numpy, tensorflow, keras, zipfile, and fastapi (library to create a REST API for python).

## Datasets
The datasets i used was from https://www.kaggle.com/datasets/imrankhan77/autistic-children-facial-data-set

## How to Run
Before running this project, you need to train and save the machine learning model by running the train.py using this command:

python train.py
Then, you have to wait untill training precess finish and the vegetable_model folder created. In this folder, your machine learning model will be saved.

After having a model, we need to run the api by the following command:

uvicorn app:app --reload
Then, access the REST API by accessing this url in your browser 127.0.0.1:8000/docs

### Containerized
```
    docker-compose up
```