import streamlit as st
import ollama

# Initialize the model using 'create' function
def init_model(model_name):
    try:
        model = ollama.create(model_name)  # Create the model
        st.success(f"Model '{model_name}' loaded successfully.")
        return model
    except Exception as e:
        st.error(f"Error loading the model: {str(e)}")
        return None

# Test the model performance
def test_model_performance(model, input_text):
    try:
        # Use the 'generate' function to get output
        output = ollama.generate(model, input_text)  # Generate output using the model
        return output
    except Exception as e:
        st.error(f"Error during model inference: {str(e)}")
        return None

# Streamlit app
st.title("Ollama Model Performance Tester")

# Model selection
model_name = st.selectbox(
    "Select the Ollama Model",
    ["llama-7b", "llama-13b", "llama-70b"]  # Replace with your available models
)

# Initialize the model
model = init_model(model_name)

# Input field for user text
input_text = st.text_area("Enter text for model testing:", height=300)

# Test model performance button
if st.button("Test Model Performance"):
    if model:
        if input_text:
            output = test_model_performance(model, input_text)
            if output:
                st.write("Model Output:")
                st.write(output)
            else:
                st.error("Failed to get output from the model.")
        else:
            st.error("Please provide input text.")
    else:
        st.error("Model failed to load. Please try again.")
