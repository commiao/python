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


# 支持移动并修改文件名 如果文件名重复则 文件名_1.后缀名
def rename_file(file_path, new_file_path):
    fd = os.path.exists(file_path)
    if not fd:
        print('修改文件名：原文件%s不存在,结束任务' % file_path)
        return

    fd = os.path.exists(new_file_path)
    if fd:
        # 如果存在，则在文件名后加"_1"，方便区分
        new_file_name = os.path.basename(new_file_path)
        file_name_splitext = os.path.splitext(new_file_name)
        new_file_name = file_name_splitext[0] + '_1' + file_name_splitext[1]
        new_file_dir = os.path.dirname(new_file_path)
        new_file_path = os.path.join(new_file_dir, new_file_name)
    print('修改文件名：原文件:%s,-->新文件:%s' % (file_path,new_file_path))
    os.rename(file_path, new_file_path)


SHARE_USER = 'commiao'
SHARE_PASSWORD = 'han880924'
SHARE_FILE_HOST = r'\\192.168.31.99'


def int_permission_cmd():
    permission_cmd = f'net use {SHARE_FILE_HOST} {SHARE_USER} /user:{SHARE_PASSWORD}'
    print("初始化共享文件夹permission_cmd:%s" % permission_cmd)
    permission_result = os.popen(permission_cmd)
    print(permission_result.read())


if __name__ == '__main__':
    path = r'F:\bbb.txt'
    path_2 = r'F:\新建文件夹\test'
    # check_create_dir(path_2)
    # move_file(path, path_2)
    path_3 = r'\\192.168.31.99\photo\jingmiao\test'
    # int_permission_cmd()
    # move_file(path, path_3)
    path_4 = r'F:\新建文件夹\test\aaa.txt'
    rename_file(path_4, path)
