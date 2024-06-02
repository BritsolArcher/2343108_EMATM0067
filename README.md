# 2343108_EMATM0067
## Overview
This project consisting of the following two parts:
* `Penguin Species Identification`: Penguin Species Identification is a project that utilizes machine learning techniques to identify and classify different species of penguins. By analyzing physical characteristics of penguins such as body size, feather coloration, and geographical location data, our model can accurately distinguish between species. This project aims to provide a reliable tool for researchers and biologists to enhance field studies and data collection efficiency.
* `Text Analytics`: The Text Analytics component of our project is designed to extract meaningful insights from text data through various natural language processing techniques. It involves preprocessing text, recognizing named entities, and classifying emotions in tweets. This component aims to provide tools that can automatically analyze text data, reducing the need for manual effort and providing quicker, more accurate analyses.

## Environment Setup
To ensure that all dependencies are properly installed and the project runs smoothly, environment setup files are provided for both components of the project.
### Penguin Species Identification
* This YAML file contains all the necessary Python packages and their versions required for the penguin species identification component of the project.
* Modify the `prefix` to match the path of your Anaconda installation and the desired environment name. 
* To create and activate the environment, use the following commands
```
conda env create -f penguin_environment.yml
conda activate penguin_env
```

### Penguin Species Identification
* This YAML file lists all dependencies needed for the text analytics part of the project.
* Modify the `prefix` to match the path of your Anaconda installation and the desired environment name. 
* To create and activate the environment, use the following commands
```
conda env create -f text_environment.yml
conda activate text_analytics_env
```