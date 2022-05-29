"""
第一步
目标：
    1、获取ios文件 数据矩阵
    2、获取win文件 数据矩阵
    3、通过 日期文件夹名称、文件名称 merger ios、win数据矩阵
"""
import os, pandas as pd


def aa(dir_path):
    print("开始执行")
    file_name_list = []
    file_path_list = []
    spli_file_list = []
    dir_name_list = []
    file_list = os.listdir(dir_path)
    dir_name = os.path.basename(dir_path)
    for file in file_list:
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            spli_file = os.path.splitext(file)
            spli_file_list.append(spli_file)
            file_name_list.append(file)
            dir_name_list.append(dir_name)
            file_path_list.append(file_path)
        else:
            print("警告：=================日期文件夹下出现了二级目录：%s" % file_path)

    df = pd.DataFrame({"file_path":file_path_list, "spli_file":spli_file_list, "file_name": file_name_list, "dir_name": dir_name_list })
    print("执行结束")
    return df


df = aa(r"\\192.168.31.99\photo\宝宝\hanminmin\202003\ios")

df

