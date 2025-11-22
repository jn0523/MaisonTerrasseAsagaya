import os
from PIL import Image, ImageDraw, ImageFont

def create_thumbnail(bg_path, qr_path, text, output_path, size, is_vertical=False):
    # Target size
    target_w, target_h = size
    
    # Load images
    try:
        bg = Image.open(bg_path).convert("RGBA")
        qr = Image.open(qr_path).convert("RGBA")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # Resize/Crop Background to fill target size
    bg_ratio = bg.width / bg.height
    target_ratio = target_w / target_h

    if bg_ratio > target_ratio:
        # Background is wider than target
        new_h = target_h
        new_w = int(new_h * bg_ratio)
    else:
        # Background is taller than target
        new_w = target_w
        new_h = int(new_w / bg_ratio)
    
    bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Center crop
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    bg = bg.crop((left, top, left + target_w, top + target_h))

    # Create a semi-transparent overlay to make text/QR pop
    overlay = Image.new('RGBA', bg.size, (0, 0, 0, 100))
    bg = Image.alpha_composite(bg, overlay)

    # Resize QR code
    # Make QR code about 1/3 of the smaller dimension
    qr_size = min(target_w, target_h) // 3
    qr = qr.resize((qr_size, qr_size), Image.Resampling.LANCZOS)

    # Calculate positions
    # Center everything
    center_x = target_w // 2
    center_y = target_h // 2

    # Font settings
    # Try to load a Japanese font
    font_path = "C:\\Windows\\Fonts\\meiryo.ttc"
    if not os.path.exists(font_path):
        font_path = "C:\\Windows\\Fonts\\msgothic.ttc"
    
    try:
        font_size = int(min(target_w, target_h) * 0.05) # 5% of smaller dimension
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Warning: Japanese font not found, using default.")
        font = ImageFont.load_default()

    # Draw text
    draw = ImageDraw.Draw(bg)
    
    # Text wrapping (simple)
    # For this specific short text, we might not need complex wrapping, 
    # but let's split if it's too long or just center it.
    # The text is "都心近郊の家事ラク ヘーベルメゾン"
    # Let's put it above or below the QR code?
    # User said "add the phrase... and background maison". 
    # Let's put QR in center and text below it.
    
    # Calculate text size
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    # Layout:
    # Vertical: QR slightly above center, Text below
    # Horizontal: QR center, Text below? Or side by side?
    # Let's stick to a vertical stack layout for simplicity and readability in both.
    
    total_h = qr_size + text_h + 40 # 40px padding
    start_y = (target_h - total_h) // 2
    
    qr_x = (target_w - qr_size) // 2
    qr_y = start_y
    
    text_x = (target_w - text_w) // 2
    text_y = qr_y + qr_size + 40

    # Paste QR
    bg.paste(qr, (qr_x, qr_y), qr)
    
    # Draw Text
    # Add a slight shadow or outline for better readability
    shadow_offset = 2
    draw.text((text_x + shadow_offset, text_y + shadow_offset), text, font=font, fill=(0, 0, 0, 200))
    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255, 255))

    # Save
    bg.save(output_path)
    print(f"Saved {output_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir)
    
    bg_image = os.path.join(project_root, "images", "maison.jpeg")
    qr_image = os.path.join(base_dir, "MaisonTerrasseAsagaya_QR.png")
    
    text = "都心近郊の家事ラク ヘーベルメゾン"
    
    # Horizontal 16:9 (e.g., 1280x720)
    create_thumbnail(
        bg_image, 
        qr_image, 
        text, 
        os.path.join(base_dir, "thumbnail_horizontal.png"), 
        (1280, 720)
    )
    
    # Vertical 9:16 (e.g., 720x1280)
    create_thumbnail(
        bg_image, 
        qr_image, 
        text, 
        os.path.join(base_dir, "thumbnail_vertical.png"), 
        (720, 1280),
        is_vertical=True
    )
