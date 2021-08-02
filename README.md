# AllerGenius
## Problem statement 
There are a lot of people who suffer from certain allergies and struggle to find medicines and eatables that don't contain those allergens. I have also faced that problem a billion times because i have a severe tree nut allergy and sometimes when i purchase packaged foods the allergen information aren't mentioned or even if they are, it is in such a fine print that it is really easy to miss. This has caused a lot of problems and turmoil in my life and in the lives of a lot of other people too.

## Proposed solution 
For dealing with this problem, it is necessary that people become aware as soon as possible about the brands that they're purchasing, the goods that they are purchasing or eating; is safe for them or not. This can be applied for the foods in restaurants too but for that, the software has to be city-specific where all the restaurants of the city are given a list of all the common allergens and then they have to give out a list of the dishes they serve which have any of those allergens. Then that data can be updated on the software database. The software for allergen detection can be a cv based scanner for goods and packaged items and just a normal database for restaurants. Then this software can be launched as an android app or a web app. 

## Dataset
For this project, I have collected the data by *web scraping* which presently contains 770 images belonging to 8 classes viz *'PEANUTS', 'TREE NUTS', 'MILK', 'NO ALLERGENS', 'FISH', 'EGG', 'SOY', 'WHEAT'*. The data has been split into 607 training+validation and 163 test images. <br>
One can  send a request for accessing the dataset <a href= "https://drive.google.com/drive/folders/1tDJpAPi3p5VSeuhVHSeMoAENMuUEsJ1Y?usp=sharing">here</a>.

### Visualizing a part of the dataset.
<img src= "assets/visualize.PNG">

## Model components
The model has 3 conv2D Layers each followed by a MaxPooling2D. The Flatten layer follows before the forward pass and classification task performed by the Fully Connected Layers with ReLU and Softmax activation function respectively. <br> <br>
<img src= "assets/model.png" height= 580 width= 250> <img src= "assets/sequential.PNG">
