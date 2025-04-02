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
2 - 
