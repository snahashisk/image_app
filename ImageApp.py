import streamlit as st
from PIL import Image, ImageEnhance
st.set_page_config(
    page_title="Image Processing App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

col1, col2, col3 = st.columns([3, 5, 2])
with col1:

    choice = st.selectbox("Select the attribute to be changed: ", [
        "Sharpness", "Brightness", "Contrast", "Color"])


imagePixelValues = []
with col2:
    st.title("Image Processing App")
    file = st.file_uploader("Upload your Image File", type=["png", "jpg"])
    if file is not None:
        im = Image.open(file)
        pix_val = list(im.getdata())
        imagePixelValues = pix_val
        st.write("File Uploaded Successfully")
        st.write(file)
        st.write("File Name:", file.name)
        st.write("File Type:", file.type)
        st.write("File Size:", file.size)
        st.image(file)
        st.text("Image Pixel Values:")

        if choice == "Sharpness":
            sharpnessValue = st.slider("Sharpness", 0.0, 10.0, 0.1)
            st.write("Sharpness")
            im1 = ImageEnhance.Sharpness(im)
            st.image(im1.enhance(sharpnessValue))
        if choice == "Brightness":
            brightnessValue = st.slider("Brightness", 0.0, 10.0, 0.1)
            st.write("Brightness")
            im2 = ImageEnhance.Brightness(im)
            st.image(im2.enhance(brightnessValue))
        if choice == "Contrast":
            contrastValue = st.slider("Contrast", 0.0, 10.0, 0.1)
            st.write("Contrast")
            im3 = ImageEnhance.Contrast(im)
            st.image(im3.enhance(contrastValue))

with col3:
    if(imagePixelValues != []):
        st.write(imagePixelValues)
