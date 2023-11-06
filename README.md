# Compression Strength Predictor for Concrete Mixtures

## Welcome
This repository contains the files for a Compression Strength Predictor. This is part of the midterm project for the Machine Learning Zoomcamp and is not intended to be a final model for general purposes.

## How Does It Work?
This prediction model is based on gradient boosted trees using the xgboost library. *** The model selection process *** is an important section of this midterm project and the details *** can be found [here](https://github.com/AndresLDF/ML-Zoomcamp-Midterm-Project/blob/main/Notebooks/1_Midterm_Project_Data_Analysis_and_Model_Selection.ipynb). ***

To use the model, you can:
- Use the live server (check the [Live Server](#live-server) section)
- Download, install, and run it locally as a server (Check the [Local Installation](#local-installation) section)

In both cases, you need to make a POST request containing a JSON object with the following information regarding the concrete mixture:
- Cement: kg in a m3 mixture
- Flyash: kg in a m3 mixture
- Water: kg in a m3 mixture
- Super Plasticizer: kg in a m3 mixture
- Coarse Aggregate: kg in a m3 mixture
- Fine Aggregate: kg in a m3 mixture
- Age: Days

The returned value will be the Compression Strength of the concrete for the indicated curing age in MPa.

## DataSet
The dataset was downloaded from [Kaggle](https://www.kaggle.com/datasets/maajdl/yeh-concret-data).

## Live Server
### Usage
To use the live server, follow these steps:
1. Open a REST API client like Thunder Client or Postman.
2. Set the method to POST.
3. Set the URL to [https://cspredictor.onrender.com/predict](https://cspredictor.onrender.com/predict).
4. Set the JSON content with the required information (JSON body example below).
5. Send the request.
6. Check the response; it should be a number, which represents the Compression Strength in MPa.

**JSON File Example:**
```json
{
  "cement": 380.00,
  "slag": 0.00,
  "flyash": 0.00,
  "water": 228.00,
  "superplasticizer": 0.00,
  "coarseaggregate": 932.00,
  "fineaggregate": 670.00,
  "age": 90.00
}
```
To this example you will get a predicted strenght of 51.67 MPa.
There could be some delay on the first request as the server goes idle after a time of not receiving any request

For information on how the model was deployed to the web server, please check the section "Web Service Deployment"

## Local Instalation
### Prerequisites
Before proceeding you need to install Docker in your local device. Please go to  [Docker](https://www.docker.com/) and install the desktop version before proceeding.

### Steps
To install an run locally this server follow these steps:
1. Download the Repository to your local machine
2. Open a terminal windows
3. Open the **Server** folder
4. typ the following command (be sure to include the final dot): docker build -t midterm .
5. After the image is built, run the following command: docker run -it --rm -p 9696:9696 midterm
6. Open a Rest API client like Thunder Client or Postman
7. Set the method to POST
8. Set the url to https://cspredictor.onrender.com/predict
9. set the JSON content with teh required information (JSON body example below)
10. Send the request
11. Check the response; it should be a number, which represents the Compression Strength in MPa.

**JSON File Example:**
```json
{
  "cement": 380.00,
  "slag": 0.00,
  "flyash": 0.00,
  "water": 228.00,
  "superplasticizer": 0.00,
  "coarseaggregate": 932.00,
  "fineaggregate": 670.00,
  "age": 90.00
}
```
## Web Service Deployment
For the Web service deployment the following steps were taken:

1. An account was created on https://render.com.
2. An account was created on https://www.docker.com/.
3. A repository was created on docker.com.
4. On my local machine, a Docker image was created using the provided Dockerfile and the command ``` docker build -t midterm . ```.
5. Then, I logged into the cloud repository from the terminal window using the command ``` docker login -u andresldf ```.
6. The local Docker image was tagged with the following command: ``` docker tag midterm:latest andresldf/cspredictor01:latest ```.
7. The image was pushed to the cloud repository using the command: ``` docker push andresldf/cspredictor01:latest ``` .
8. On the Render server, the option to establish a web service was selected.
9. Then, the option to use a Docker image from the web was chosen.
10. The URL https://hub.docker.com/repository/docker/andresldf/cspredictor01/general was used as the image URL.
11. The web service was deployed at https://cspredictor.onrender.com.
