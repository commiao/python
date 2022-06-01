import os
import shutil


def check_create_dir(dir_path):
    print('检查创建文件夹:' + dir_path)
    fd = os.path.exists(dir_path)
    if not fd:
        print('创建目录：%s' % dir_path)
        os.makedirs(dir_path)
    else:
        print('目录已存在：%s' % dir_path)


def move_file(file_path, dir_path):
    # 校验目标目录是否存在，不存在则新建
    check_create_dir(dir_path)
    # 校验目标目录下是否已存在该文件
    file_name = os.path.basename(file_path)
    fd = os.path.exists(os.path.join(dir_path, file_name))
    if not fd:
        print('移动文件：%s' % file_path)
        shutil.move(file_path, dir_path)
    else:
        print('文件已存在：%s' % file_path)


SHARE_USER = 'commiao'
SHARE_PASSWORD = 'han880924'
SHARE_FILE_HOST = r'\\192.168.31.99'


def int_permission_cmd():
    permission_cmd = f'net use {SHARE_FILE_HOST} {SHARE_USER} /user:{SHARE_PASSWORD}'
    print("初始化共享文件夹permission_cmd:%s" % permission_cmd)
    permission_result = os.popen(permission_cmd)
    print(permission_result.read())


if __name__ == '__main__':
    path = r'F:\aaa.txt'
    path_2 = r'F:\新建文件夹\test'
    check_create_dir(path_2)
    move_file(path, path_2)
    path_3 = r'\\192.168.31.99\photo\jingmiao\test'
    # int_permission_cmd()
    move_file(path, path_3)
