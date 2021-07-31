import streamlit as st
import urllib
from PIL import Image
import time
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image

html_temp= '''
            <div>
            <center> <H1> AllerGenius </H1> </center> </div>'''
st.markdown(html_temp, unsafe_allow_html= True)
#@st.cache(allow_output_mutation= True, suppress_st_warning= True)
html_temp= '''
            <div>
            <center> <H3> Please upload an image of a product that you wish to check for allergens. </H3> </center> </div>'''
st.set_option ("deprecation.showfileUploaderEncoding", False)            
st.markdown(html_temp, unsafe_allow_html= True)
opt= st.selectbox('Select the mode of uploading the image.', ('Please select', 'Upload Image from Device', 'Upload Image via Link'),)
if opt == 'Upload Image from Device':
    file= st.file_uploader('Select', type= ['jpg', 'png', 'jpeg'])
    st.set_option ("deprecation.showfileUploaderEncoding", False) 
    if file is not None:
        image= Image.open(file) 
elif opt == 'Upload Image via Link':
    try:
        img= st.text_input("Enter the Image Address")
        image= Image.open(urllib.request.urlopen(img))
    except:
        if st.button("Submit"):
            show= st.error("Please Enter a Valid Image Address")
            time.sleep(8)
            show.empty()

try:
    if image is not None:
        st.image(image, width= 300, caption= "Uploaded Image")
        if st.button ("Detect Allergen"):
            img= np.array(image.resize((128,128), Image.ANTIALIAS))
            img= np.array(img, dtype='uint8')
            img= np.array(img)/(255.0)
            model= keras.models.load_model('Model/model.h5')
            train_labels= {'EGG': 0, 'FISH': 1, 'MILK': 2, 'NO ALLERGENS': 3, 'PEANUTS': 4, 'SOY': 5, 'TREE NUTS': 6, 'WHEAT': 7}
            labels= dict((value,key) for key, value in train_labels.items())
            predictions= model.predict(img[np.newaxis,...])
            result= labels[np.argmax(predictions[0], axis=-1)]
            st.info(f"The Allergen in the Product is: {result}")
            
except:
    pass 
       