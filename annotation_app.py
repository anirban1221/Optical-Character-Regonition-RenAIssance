
import streamlit as st
from PIL import Image

# App setup
st.set_page_config(page_title="OCR Annotator", layout="wide")
st.header("Text Recognition Annotation Tool")

# Upload image (though in prototype version, in final version the website can extract image from 
# any kind of document)
uploaded_file=st.file_uploader(" ### Upload an early modern Spanish document image",type=["jpg", "jpeg", "png"])


if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    ##here we will do the following things:
    #preprocessing and cleaning
    #text detection
    #tokenization and encoding
    #text extraction by transformer model
    #post processing of the extracted text

    # Columns layout
    col1, col2 = st.columns(2,gap='small')

    # LEFT = Image
    with col1:
        st.markdown("### Uploaded Image")
        st.image(image, use_container_width=True)

    # RIGHT = Text
    with col2:
        st.markdown("### Extracted Text ") 
        st.text_area(
            "You can edit the OCR result here:",
            value="Extracted text by the transformer model will appear here... \n \n This field is editable ",
            height=450,
            label_visibility="collapsed"
        )

    # Bottom: Feedback section
    st.markdown("---")
    st.markdown("### Feedback to Model Developers")
    st.text_area(
        "Let us know if anything is wrong in the text extraction:",
        placeholder="write your feedback here",
        height=150
    )

    # Save button
    if st.button("Save Correction & Feedback"):
        st.success(" Correction and feedback saved!")




