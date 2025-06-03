import streamlit as st
import base64

st.set_page_config(page_title="Hope website",layout="wide",initial_sidebar_state="collapsed",menu_items=None)




# Change these to match your image

image_file = "images/techniques_image.png"  # <--- Replace with your actual image file name

def get_base64_of_bin_file(bin_file):
    '''
    Opens a png image file and converts it to a base64 string so it can be used by streamlit
    '''
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#method below uses the method above to display a background image




#method below uses the method above to display a background image
def set_png_as_page_bg(png_file):
    '''
    displays an image as a background
    code from: https://discuss.streamlit.io/t/how-do-i-use-a-background-image-on-streamlit/5067
    '''
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
      background-image: url("data:image/png;base64,%s");
      background-size: cover: contain;
      background-repeat: no-repeat;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

# # Inject background CSS
# st.markdown(bg_img, unsafe_allow_html=True)

#set_png_as_page_bg(image_file)
st.image(image_file, use_column_width=True)



st.subheader("Welcome to the Technique page! Here, you’ll discover the basic skills and movements for swimming, boxing, and equestrian. This page will guide you step by step to help you build strong techniques and stay safe!", divider="gray")