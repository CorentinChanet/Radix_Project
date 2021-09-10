<div align='center'>
  
  <h3>Becode AI training

Radix Project</h3>


<img width = "200" src = https://becode.org/app/uploads/2020/03/cropped-becode-logo-seal.png>



</div>

# Radix Project
## Table of contents
[Description](#Description)  
[Installation](#Installation)  
[Usage](#Usage)  
[How it works](#How-it-works)  
[Examples](#Examples)  
[Authors](#Authors) 


## Description

We developed a Minimum Viable Product (MVP) at the request of Radix. The purpose of this project is to use NLP technologies to process Curriculum Vitae. 
In doing so, the end goal is to automate parts of the matching process between job seekers and job offers, and make it faster and easier.

This application has 2 main features : 
* **Information extraction**. The user must be able to extract relevant information for each resume from the data set.
Some information are more difficult to extract than other, or more complex to format (such as the institution-year for the curriculum); 
  therefore this feature could be further optimize <br></br>
    
* **Finding similar profiles**. The goal is to be able to compare section-by-section a given CV against a whole dataset, and display the 
  10 most similar profiles, whether in terms of working experience, skills
  or education.<br></br>

This MVP was developped with a selection of CV (.pdf) taken from : https://github.com/arefinnomi/curriculum_vitae_data 

Below are additional informations regarding the installation and the use of this MVP

## Installation
1. Clone the repository:
```
git clone https://github.com/Misterkadrix/Radix_Project.git
``` 
2. Install the required libraries:
```
pip install [required library]
```

## Usage
To start the program on your local machine, you just need to go to the terminal and enter :
```
streamlit run streamlit_app.py
```


## How it works


The streamlit application is divided in 3 sections:
1. Information Extraction : It will extract extract key features from the chosen resume from the dataset.
2. Resume Matching (from dataset) : It will find matches between a resume from the dataset and the rest of the dataset
3. Resume Matching (uploaded file) : It will find matches between an uploaded resume (only works with .pdf) and the dataset

For every section you can either choose the features or the section of interest.
Please keep in mind this application is not and end-product. It should however be stable and handle out-of-range values, wrong file extensions etc.

## Examples

**Extraction Information**
<img width = '2000' src = /images/extr.gif>

**Resume Matching**
<img width = '2000' src = /images/Matching.gif>


**Resume Matching with upload file**
<img width = '2000' src = '/images/MatchingUpload.gif'>


## Authors

[Kadri Salija](https://github.com/Misterkadrix?tab=repositories) - Project Manager/dev

[Corentin Chanet](https://github.com/CorentinChanet) - dev   


## Languages and tools
<p float="left">
<img height="32" width="32" src='https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png'>
<img height="32" width="32" src="https://image.flaticon.com/icons/png/512/25/25231.png" />
<img height="32" width="32" src='https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png'>
<img height="32" width="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/jupyter-notebook/jupyter-notebook.png" />
<img height="32" width="32" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png" />
<img height="32" width="32" src="https://media-exp3.licdn.com/dms/image/C4D0BAQEA_8lZLUHyww/company-logo_200_200/0/1586263619650?e=2159024400&v=beta&t=vP2ulubqaSF7FkDudqaPDGqxZqlnsQa0ooaduT_VZjQ" />
<img height="32" width="32" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2QBYBpWFe-4E3moGldWvlQ5XdAcEBnPTj2zJRMfpmODTlOPb_PVCz8wohqGPtNY7lYjY&usqp=CAU" />
  
 </p>

