import os, shutil

# PATH = r"\\192.168.31.99\photo\宝宝"
PATH = r"\\192.168.31.99\photo\jingmiao"


def main():
    for root, dirs, files in os.walk(PATH):
        print('root:')
        print(root)  # 当前目录路径
        print('dirs:')
        print(dirs)  # 当前路径下所有子目录
        print('files:')
        print(files)  # 当前路径下所有非目录子文件
        print('========================')
    print('succcess')


def testOs():
    dir_path = os.path.join(PATH, 'testCreateDir')
    fd = os.path.exists(dir_path)
    if not fd:
        os.makedirs(dir_path)

    file_path = os.path.join(dir_path, 'testCreateFile.txt')
    fd = os.path.exists(file_path)
    # 如果不存在
    if not fd:
        with open(file_path, mode='wt') as f:
            f.write("a\nb\nc\nd\ne\nf\ng\n")
            f.close
            print(file_path + '创建成功')

    copy_file_path = os.path.join(dir_path, 'testCreateFile_copy.txt')
    fd = os.path.exists(copy_file_path)
    # 如果不存在
    if not fd:
        shutil.copy(file_path, copy_file_path)

    shutil.move(file_path, PATH)
    new_dir_path = os.path.join(PATH, 'testCopyDir')
    shutil.copy(dir_path, new_dir_path)

    old_file_path = os.path.join(PATH, 'testCreateFile.txt')
    new_file_path = os.path.join(PATH, 'testCreateFile_rename.txt')
    shutil.rename(old_file_path, new_file_path)


if __name__ == '__main__':
    # main()
    testOs()
    pass
