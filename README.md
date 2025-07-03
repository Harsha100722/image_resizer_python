# Image Resizer Tool 

A simple Python tool to resize and convert images in batch, built using the Pillow library.

## Objective

Resize all images in a folder to a specified size and convert them to a chosen format (JPEG or PNG).  
Useful for:
- Optimizing images for web
- Creating uniform thumbnails
- Batch processing large image sets

## Tools Used

- Python 3.x
- Pillow (PIL)
- os (for file and folder handling)

## Folder Structure

image_resizer_python/
├── image_resizer.py         # Main script
├── images/                  # Put your original images here
│   ├── sample1.png
│   └── sample2.jpeg
└── output/                  # Resized images will be saved here

## How to Run

1. Install Pillow

   pip install Pillow

2. Add Images

Place your .jpg, .jpeg, .png, .bmp, or .gif files inside the images/ folder.

3. Run the Script

   python image_resizer.py

Resized and converted images will be saved to the output/ folder.

## Configuration

You can modify these variables in image_resizer.py to fit your needs:

target_size = (800, 600)          # Resize to width x height  
output_format = "JPEG"            # Options: 'JPEG', 'PNG', etc.

## Notes

- JPEG does not support transparency, so palette-based images will be converted to RGB.
- To preserve transparency, use output_format = "PNG".

## Example Output

If sample1.png and sample2.jpeg are in the images/ folder, after running the script, you will see:

✅ Resized and saved: sample1.jpeg  
✅ Resized and saved: sample2.jpeg

