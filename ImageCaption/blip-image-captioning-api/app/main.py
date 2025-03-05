import streamlit as st
from PIL import Image
from io import BytesIO
from model import load_model, generate_caption
from utils import load_image_from_file
from config import settings

# Load the BLIP model once when the app starts
model, processor = load_model(settings.blip_model_name)

# Streamlit Interface
def app():
    st.title("Image Captioning with BLIP Model")
    st.write("Upload an image, and we will generate a caption for it.")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Log the file details for debugging
        st.write(f"File type: {uploaded_file.type}")
        st.write(f"File size: {uploaded_file.size} bytes")

        try:
            # Check the first few bytes to ensure this is image data
            image_data = uploaded_file.read()
            st.write(f"First few bytes of the image data: {image_data[:10]}")

            # Ensure the file is valid image data
            try:
                image = Image.open(BytesIO(image_data))
                st.image(image, caption="Uploaded Image", use_container_width=True)

                # Now, load the image properly for captioning
                loaded_image = load_image_from_file(image_data)
                caption = generate_caption(model,processor,loaded_image,text="Provide a detailed and accurate description of the image, focusing on key elements and objects.")
                
                st.write(f"Generated Caption: {caption}")

            except Exception as e:
                st.error(f"Error opening the image: {e}")
                st.write("Error details:")
                st.write(e)

        except Exception as e:
            st.error(f"Error processing the image data: {e}")
            st.write("Error details:")
            st.write(e)

if __name__ == "__main__":
    app()
