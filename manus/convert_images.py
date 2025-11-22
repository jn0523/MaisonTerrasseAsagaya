#!/usr/bin/env python3
import os
from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener

# HEIF形式のサポートを有効化
register_heif_opener()

# 画像ディレクトリ
images_dir = Path("/home/ubuntu/MaisonTerrasseAsagaya/images")

# HEICファイルを検索して変換
for heic_file in images_dir.glob("*.HEIC"):
    jpg_file = heic_file.with_suffix(".jpg")
    
    print(f"Converting {heic_file.name} to {jpg_file.name}...")
    
    # 画像を開いてJPGとして保存
    img = Image.open(heic_file)
    
    # RGBモードに変換（HEICはRGBAの場合がある）
    if img.mode in ('RGBA', 'LA', 'P'):
        img = img.convert('RGB')
    
    # JPGとして保存（品質85%）
    img.save(jpg_file, "JPEG", quality=85, optimize=True)
    print(f"  Saved: {jpg_file.name}")

print("\nConversion completed!")
