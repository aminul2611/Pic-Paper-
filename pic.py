from PIL import Image, ImageDraw, ImageFont
import os
image_data = [
    ('a.png', '(a) Plain 3D CNN Baseline.'),
    ('b.png', '(b) 3D ResNet-18 (Heavy).'),
    ('c.png', '(c) Proposed R(2+1)D-Light.')
]

images = []

for file, caption in image_data:
    if os.path.exists(file):
        img = Image.open(file)
        images.append((img, caption))
    else:
        print(f"Error! Could not find the image named '{file}'.")
        print("Please check the file name and folder.")
        exit()

if not images:
    print("No images found!")
    exit()

widths = [img.size[0] for img, _ in images]
max_width = max(widths)
caption_height = 180
gap = 30

total_height = 0
for img, _ in images:
    total_height += img.size[1] + caption_height

new_image = Image.new('RGB', (max_width, total_height), (255, 255, 255))
draw = ImageDraw.Draw(new_image)
font_size = 70

try:
    font = ImageFont.truetype("times.ttf", font_size)
except IOError:
    try:
        font = ImageFont.truetype("/Library/Fonts/Times New Roman.ttf", font_size)
    except IOError:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf", font_size)
        except IOError:
            print("Times New Roman font not found. Using default font instead.")
            font = ImageFont.load_default()
y_offset = 0
for img, caption in images:
    x_offset = (max_width - img.size[0]) // 2
    new_image.paste(img, (x_offset, y_offset))

    caption_y = y_offset + img.size[1] + gap

    try:
        bbox = draw.textbbox((0, 0), caption, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except AttributeError:
        text_width, text_height = draw.textsize(caption, font=font)

    caption_x = (max_width - text_width) // 2

    draw.text((caption_x, caption_y), caption, fill=(0, 0, 0), font=font)

    y_offset += img.size[1] + caption_height

new_image.save('Final_Combined_Image.jpg', quality=95)
print("=" * 50)
print("Images successfully combined with captions!")
print("The file 'Final_Combined_Image.jpg' has been saved in your folder.")
print("=" * 50)