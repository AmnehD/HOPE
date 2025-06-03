import streamlit as st
import base64

st.set_page_config(page_title="Hope website",layout="wide",initial_sidebar_state="collapsed",menu_items=None)




# Change these to match your image

image_file = "images/equestrian_image.png"  # <--- Replace with your actual image file name

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



st.subheader("Welcome to the Equestrian page! 🐎 Here, you'll learn all about horses and how to ride them safely. From getting to know your horse to learning how to sit and steer, this page will help you feel confident and have fun in the saddle!", divider="gray")


# Create two columns
col1, col2 = st.columns(2)

# Place each image in a separate column
with col1:
    st.image("images/equestrianadult_image.jpg", caption="Standard equestrian", width=550)

with col2:
    st.image("images/equestriankid_image.jpg", caption="child equestrian", width=550)