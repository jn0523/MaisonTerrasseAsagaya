import codecs

def replace_images(filepath):
    # Read with UTF-8 BOM detection
    with open(filepath, 'rb') as f:
        raw = f.read()
    
    # Check for BOM and decode accordingly
    if raw.startswith(codecs.BOM_UTF8):
        content = raw[3:].decode('utf-8')
        has_bom = True
    else:
        content = raw.decode('utf-8')
        has_bom = False
    
    # Replace image paths
    content = content.replace('images/', 'images_forweb/')
    content = content.replace('.JPG', '.webp')
    content = content.replace('.jpg', '.webp')
    content = content.replace('.PNG', '.webp')
    content = content.replace('.jpeg', '.webp')
    
    # Write with same encoding
    with open(filepath, 'wb') as f:
        if has_bom:
            f.write(codecs.BOM_UTF8)
        f.write(content.encode('utf-8'))
    
    print(f"Updated: {filepath} (BOM: {has_bom})")

# Update both HTML files
replace_images('101.html')
replace_images('201.html')

print("Done!")
