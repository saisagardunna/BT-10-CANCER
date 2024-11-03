# tb.py
import numpy as np
import tensorflow as tf
import streamlit as st
from PIL import Image

def tb_page():
    interpreter_tb = tf.lite.Interpreter(model_path='models/tb_model.tflite')
    interpreter_tb.allocate_tensors()
    input_details_tb = interpreter_tb.get_input_details()
    output_details_tb = interpreter_tb.get_output_details()

    st.subheader("Tuberculosis Detection", divider='grey')
    st.caption("sample [image](https://www.kaggle.com/datasets/raddar/tuberculosis-chest-xrays-shenzhen)")

    uploaded_file = st.file_uploader("Upload a Chest X-ray Image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=False)

        image_array = np.asarray (image.resize((224, 224)))
        image_array = image_array.astype(np.float32) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        interpreter_tb.set_tensor(input_details_tb[0]['index'], image_array)
        interpreter_tb.invoke()
        predictions = interpreter_tb.get_tensor(output_details_tb[0]['index'])
        class_index = np.argmax(predictions)

        if class_index == 1:
            st.success("Tuberculosis Detected!")
        else:
            st.success("No Tuberculosis Detected.")

if __name__ == "__main__":
    tb_page()
