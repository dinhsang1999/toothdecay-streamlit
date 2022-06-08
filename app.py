import streamlit as st
st.sidebar.header('User Input Features')
selected_image = st.sidebar.file_uploader('Upload image from PC',type=['png', 'jpg'],help='Type of image should be PNG or JPEG')
st.write('Hello,world!')
