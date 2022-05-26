# -*- coding: utf-8 -*-
from PIL import Image
import pyheif
import os
import whatimage
import traceback


# 循环读取HEIC格式照片，写入JPG
def recyle_convert(org_path, dst_path):
    # 判断是不是目录
    if os.path.isdir(org_path):
        file_list = os.listdir(org_path)
        for idx, file in enumerate(file_list):
            sub_path = os.path.join(org_path, file)
            recyle_convert(sub_path, dst_path)
    # 判断是不是文件
    elif os.path.isfile(org_path):
        with open(org_path, 'rb') as f:
            file_data = f.read()
            try:
                # 判断照片格式
                fmt = whatimage.identify_image(file_data)
                if fmt in ['heic']:
                    # 读取图片
                    heif_file = pyheif.read_heif(org_path)
                    image = Image.frombytes(mode=heif_file.mode, size=heif_file.size, data=heif_file.data)
                    # 将要存储的路径及名称
                    path, filename = os.path.split(org_path)
                    name, ext = os.path.splitext(filename)
                    file_path = os.path.join(dst_path, '%s.jpg' % name)
                    print(file_path)
                    # 缩略图（原始图片太大了，换成1080x1440）
                    image.thumbnail((1080, 1440))
                    # 保存图片（JPEG格式）
                    image.save(file_path, "JPEG")
            except Exception as e:
                print(e)
                traceback.print_exc()
    else:
        print(org_path + 'is error format!')
    pass


# 主函数入口
def main():
    # dst path
    dst_path = '/home/chen/图片/车牌'
    if os.path.exists(dst_path) is False:
        os.makedirs(dst_path)
        pass
    # org path
    org_path = '/home/chen/图片/车牌'
    # convert
    recyle_convert(org_path, dst_path)
    pass


if __name__ == '__main__':
    main()
    pass
