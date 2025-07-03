import os
from PIL import Image


base_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(base_dir, "images")
output_folder = os.path.join(base_dir, "output")
target_size = (100, 100)
output_format = "JPEG"

def resize_images(input_dir, output_dir, size, img_format):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    found_images = False
    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            found_images = True
            input_path = os.path.join(input_dir, filename)
            img = Image.open(input_path)


            if img_format.upper() == "PNG":
                img_resized = img.resize(size).convert("RGBA")
            else:
                img_resized = img.resize(size).convert("RGB")


            output_filename = os.path.splitext(filename)[0] + "." + img_format.lower()
            output_path = os.path.join(output_dir, output_filename)
            img_resized.save(output_path, img_format)

            print(f"✅ Resized and saved: {output_filename}")

    if not found_images:
        print("⚠️ No valid image files found in the folder.")


resize_images(input_folder, output_folder, target_size, output_format)
