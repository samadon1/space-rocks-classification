import streamlit as st
st.set_page_config(page_title='Space Rocks', page_icon='https://mpng.subpng.com/20190618/jpw/kisspng-sphere-5d08cbf5a66033.7135118215608575896815.jpg', layout='centered', initial_sidebar_state='auto')
import tensorflow as tf
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model('rocks.h5')

st.write("""
# Classify Moon Rocks :new_moon: :first_quarter_moon: :full_moon:
""")

st.write("""
## An AI model that can classify the type of space rock in a random photo.""")

#st.image('https://www.thevintagenews.com/wp-content/uploads/2019/08/moon_rock-1280x720.jpg', width = 700)

new_width  = 512
new_height = 512

uploaded_image = st.sidebar.file_uploader("Upload a space rock", type="jpg")
if uploaded_image:
    image = Image.open(uploaded_image)
    st.sidebar.info('Uploaded image:')
    st.sidebar.image(image, use_column_width=True)
    st.image(image, caption = 'Uploaded image', width = 500)
    if st.button('Classify'):
      image = image.resize((new_width, new_height), Image.ANTIALIAS)
      #img = tf.keras.preprocessing.image.load_img(image, target_size=(512,512))
      img_array = tf.keras.preprocessing.image.img_to_array(image)
      img_array = tf.expand_dims(img_array, 0)
      predictions = model.predict(img_array)
      score = predictions[0]
    
      if score < 0.5:
        rock = 'Basalt'
      else:
        rock = 'Highland'
      st.write('### The image contains a sample of a ', rock, ' rock')
      
