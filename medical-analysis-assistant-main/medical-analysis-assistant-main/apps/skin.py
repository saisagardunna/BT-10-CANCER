# skin.py
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

def skin_page():
    interpreter_skin = tf.lite.Interpreter(model_path='models/skinmodel.tflite')
    interpreter_skin.allocate_tensors()
    input_details_skin = interpreter_skin.get_input_details()
    output_details_skin = interpreter_skin.get_output_details()

    # Map class indices to class names
    class_names = {
        0: 'Melanocytic nevi',
        1: 'Melanoma',
        2: 'Benign keratosis-like lesions',
        3: 'Basal cell carcinoma',
        4: 'Actinic keratoses',
        5: 'Vascular lesions',
        6: 'Dermatofibroma'
    }

    st.subheader("Skin Cancer Classification", divider='grey')
    st.caption("sample [image](https://www.kaggle.com/datasets/hasnainjaved/melanoma-skin-cancer-dataset-of-10000-images)")

    uploaded_file = st.file_uploader("Upload a Dermatocopic Image of Skin Lesion", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=False)

        img_array = np.asarray(image.resize((100, 75)))
        img_array = img_array.astype(np.float32) / 255.0  
        img_array = np.expand_dims(img_array, axis=0)  

        interpreter_skin.set_tensor(input_details_skin[0]['index'], img_array)
        interpreter_skin.invoke()
        prediction = interpreter_skin.get_tensor(output_details_skin[0]['index'])
        predicted_class = np.argmax(prediction)

        st.write(f"Predicted Class: {class_names[predicted_class]}")
        st.write(f"Confidence: {prediction[0][predicted_class]:.4f}")

if __name__ == "__main__":
    skin_page()
