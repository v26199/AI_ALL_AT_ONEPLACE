from PIL import Image
import io

def load_image_from_file(image_data):
    try:
        # Convert byte data into an image
        image = Image.open(io.BytesIO(image_data))
        image = image.convert("RGB")  # Ensure the image is in RGB mode
        return image
    except Exception as e:
        raise ValueError("Invalid image data") from e
