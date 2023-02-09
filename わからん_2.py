import sys
from io import BytesIO
from PIL import Image
def data_to_img(data):
    """メモリ内の<data>からPIL Imageオブジェクトを作って返す"""
    fp=BytesIO(data)
    return Image.open(fp)
def img_to_data(img, fmt=None):
    """PIL Imageオブジェクトの<img>のイメージデータを<fmt>形式で返す"""
    fp=BytesIO()
    if not fmt:
        fmt=img.format #元の形式を維持
    img.save(fp,fmt)
    return fp.getvalue()
def convert_image(data, fmt=None):
    """イメージ<data>をPIL Imageオブジェクト経由で<fmt>形式に変換"""
    img=data_to_img(data)
    return img_to_data(img, fmt)
def get_file_data(name):
    """イメージファイル<name>からイメージデータを作って返す"""
    img=Image.open(name)
    print("img",img,img.format)
    return img_to_data(img)
if __name__=="__main__":
    for name in sys.argv[1:]:
        data=get_file_data(name)
        print("in",len(data),data[:10])
        for fmt in ("gif","png","jpeg"):
            out_data=convert_image(data, fmt)
            print("out",len(out_data),out_data[:10])