import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")
    #this will input the camera

if camera_image:
#we use this conditional to avoid actions
# to autostart when camera asks for permission

    img = Image.open(camera_image)

    #convert pillow image to grayscale
    gray_img = img.convert("L")
    # L is a notation for what type of algorithm to use

    # Render the grayscale image on webpage
    st.image(gray_img)