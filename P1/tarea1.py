from PIL import Image, ImageOps

def generate_negative(image_path, output_path):
    # Open the image
    image = Image.open(image_path)

    # Generate the negative
    negative_image = ImageOps.invert(image.convert("RGB"))

    # Save the negative image
    negative_image.save(output_path)
    print(f"Negative image saved to {output_path}")

if __name__ == "__main__":
    
    input_image_path = "minion.jpg"  # Replace with your input image path
    output_image_path = "bananoide3000.jpg"  # Replace with your desired output image path

    generate_negative(input_image_path, output_image_path)
