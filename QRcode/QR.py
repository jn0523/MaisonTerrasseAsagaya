import qrcode

# データ定義
url = "https://jn0523.github.io/MaisonTerrasseAsagaya/introduction.html"

# QRコード生成の設定
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# 画像の作成と保存
img = qr.make_image(fill_color="black", back_color="white")
img.save("QRcode/MaisonTerrasseAsagaya_QR.png")