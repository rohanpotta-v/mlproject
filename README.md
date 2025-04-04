This is the end to end Machine Learning Project with AWS and Azure
Steps:
1 - Make a repository to commit your code
    a) Make a new env (conda create -p venv python==3.8 -y) -> Conda activate venv
    Steps for storing connecting the local and the repo:
        git init
        git add .\README.md
        git commit -m "Adding Readme.md"
        git branch -M  main
        git remote add origin https://github.com/rohanpotta-v/mlproject.git
        git push origin main
    b) project structure (setup.py) -> This is used to place the machine learning code as a package
    c) requirements.txt -> adding the -e . to requirements this allows us to setup the setup.py file as well , and both will run with the command=>
            pip intall -r requirements.txt

2 - Project Strucutre
    a) src foldent 
    b) __init__.py so that setup.py file can module/package it
        c) create a folder inside the src called component and this has the files regarding the "data-ingestion" or the "databases" and so on
        d) This should also have the __init__.py so that they can be moduled up/packaed
        e) You can have data_transforamtion , model_trainer
    f) We create another folder called "pipeline" and we usually have two pipelines
        g) train_pipline.py this is used to train the model and trigger all the files in the components folder
        h) predict_pipeline.py this is used to make predictions
        i) this should also have the __init__.py file as well
    j) logger.py this is used to store the logs -> This is used to log each and every step into a file 
    k) excpetion.py this is used for the exception handling
    l) utils.py this is there is any repetitive code which needs to be used or shared around the entire program -> This is made as and when it is required and needed

3- Project
Title -> Student Performace Indicator

4 - Data Ingestion
Objective is to read the data from any source and split the data as train and test. this was written in the "src\components\data_ingestion.py" and we read a csv file and split it as train and test split as well.

5 - Data Transformation 
The objective is to perform data preprocessing and like converting categorical features into numberic and so on

6 - Model Trainer
The objective here is to train different different models as see which have good score. The point is that we try every model because we dont know which one will perform better and then we can further refine it perform the hyper-parameter tuning.

7 - Creating a Prediction Pipline
The objective is to create an api to talk to the model build a html page to get the inputs and then make a predictive result of the maths result.

