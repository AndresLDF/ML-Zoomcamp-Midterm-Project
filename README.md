# Welcome
This repository contains the files for the a Compression Strenge Predictor.
This is part of the midterm project for the Machine Learning Zoomcamp and is not intended to be a final model for general propurses

## How does it works? 
This is a prediction model based on gradient boosted trees using xgboost library. The model selection process is an important section on this midtrm project and the details can be found here:

For using the model you can:
* Use the ** live server ** (chek the live server section)
* Download, install and run it locally as a server (Check the Local Instalation section)

In both cases you need to do a POST request containing an JSON object with the following informaiton regarding the concrete micture:
* Cement: kg in a m3 mixture
* Flyash: kg in a m3 mixture
* Water: kg in a m3 mixture
* Super Plasticizer: kg in a m3 mixture
* Coarse Aggregate: kg in a m3 mixture
* Fine aggregate: kg in a m3 mixture
* Age: Days

The returned value will be the Compresion Strenght of the concrete for the indicated curing age in the units of MPa

## DataSet
The dataset was downloaded from https://www.kaggle.com/datasets/maajdl/yeh-concret-data

## Live Server
For using the live server follow the next steps:
1. Open a Rest API client like Thunder Client or Postman
2. Set the method to POST
3. Set the url to https://cspredictor.onrender.com/predict
4. set the JSON content with teh required information (JSON body example below)
5. Send the request
6. Check the response, it should be a number, it is the Compresion Strenght in MPa

JSON file example:
{
"cement": 380.00,
"slag": 0.00,
"flyash": 0.00,
"water": 228.00,
"superplasticizer" :0.00,
"coarseaggregate": 932.00,
"fineaggregate": 670.00,
"age": 90.00
}

To this example you will get a predicted strenght of 51.67 MPa.
There could be some delay on the first request as the server goes idle after a time of not receiving any request

