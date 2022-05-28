import os

SHARE_USER = 'commiao'
SHARE_PASSWORD = 'han880924'
SHARE_FILE_HOST = r'\\192.168.31.99'


def int_permission_cmd(share_file_host, share_user, share_password):
    permission_cmd = f'net use {share_file_host} {share_user} /user:{share_password}'
    print("初始化共享文件夹permission_cmd:%s" % permission_cmd)
    return permission_cmd


def copy_share_file(permission_cmd, share_file_path, target_file_path):
    print("开始copy共享文件%s, 目标文件%s" % (share_file_path, target_file_path))
    permission_result = os.popen(permission_cmd)
    print(permission_result.read())
    copy_cmd = f'xcopy /y {share_file_path} {target_file_path}'
    print("copy共享文件操作结束:%s" % copy_cmd)
    copy_result = os.popen(copy_cmd)
    print(copy_result.read())


def copy_share_file_commiao(share_file_path, target_file_path):
    print("开始操作NAS-commiao")
    permission_cmd = f'net use {SHARE_FILE_HOST} {SHARE_USER} /user:{SHARE_PASSWORD}'
    print("初始化共享文件夹permission_cmd:%s" % permission_cmd)
    print("开始copy共享文件%s, 目标文件%s" % (share_file_path, target_file_path))
    permission_result = os.popen(permission_cmd)
    print(permission_result.read())
    copy_cmd = f'xcopy /y {share_file_path} {target_file_path}'
    print("copy共享文件操作结束:%s" % copy_cmd)
    copy_result = os.popen(copy_cmd)
    print(copy_result.read())


if __name__ == '__main__':

    SHARE_USER = 'commiao'
    SHARE_PASSWORD = 'han880924'
    SHARE_FILE_HOST = r'\\192.168.31.99'

    permission_cmd = int_permission_cmd(SHARE_FILE_HOST, SHARE_USER, SHARE_FILE_HOST)

    share_file_path = r'\\192.168.31.99\photo\hanminmin\todo\新建文件夹7'
    target_file_path = r'F:\HEIC\新建文件夹7'
    # target_file_path='\\\\192.168.31.99\\photo\\hanminmin\\mobile'
    # copy_share_file(permission_cmd, share_file_path, target_file_path)

    # share_file_path = r'\\192.168.31.99\photo\hanminmin\todo\新建文件夹3'
    share_file_path = r'\\192.168.31.99\photo\hanminmin\heic\新建文件夹7'
    target_file_path = r'F:\HEIC\新建文件夹7'

    # share_file_path = '\\\\192.168.31.99\\photo\\hanminmin\\heic\\新建文件夹8'
    # target_file_path = 'F:\\HEIC\\新建文件夹8'
    copy_share_file_commiao(share_file_path, target_file_path)
    share_file_path = r'\\192.168.31.99\photo\hanminmin\todo\新建文件夹7'
    copy_share_file_commiao(share_file_path, target_file_path)




    # file_name = '新建文件夹7'
    # target_dir_path = rf'F:\HEIC\{file_name}'
    # copy_share_file_commiao(rf'\\192.168.31.99\photo\hanminmin\todo\{file_name}', target_dir_path)
    # copy_share_file_commiao(rf'\\192.168.31.99\photo\hanminmin\heic\{file_name}', target_dir_path)


