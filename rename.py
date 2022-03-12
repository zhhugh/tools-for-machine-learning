import os


def rename_v1(path):
    """
    文件批量重命名，可能会出现文件覆盖的问题
    :param path: file path
    :return: None
    """
    num = 26
    for file in os.listdir(path):
        os.rename(os.path.join(path, file), os.path.join(path, str(num).zfill(5) + ".jpg"))
        num += 1


def renameFiles(folder_path, startNumber, suffix):
    """
    批量重命名文件:
    忽略文件夹，且不会出现文件覆盖的问题
    """
    filenames = os.listdir(folder_path)
    changeList = []  # 记录哪些文件被修改了
    newNameList = []  # 预期生成的新文件名列表
    length = 0

    # 计算文件夹下文件数量
    for filename in filenames:
        if os.path.isdir(os.path.join(folder_path, filename)) or filename == '.DS_Store':  # join合并路径名，会帮你自动考虑“/”
            continue
        length += 1
    # 计算预期的新文件夹列表
    for i in range(length):
        tmp = str(i + int(startNumber)).zfill(6) + "." + suffix
        newNameList.append(tmp)

    print("正在批量处理\n...")
    count, num = 0, 0

    # 核心代码
    for filename in filenames:
        # 如果是子文件夹，则不执行
        if os.path.isdir(os.path.join(folder_path, filename)) or filename in ['.DS_Store', 'classes.txt']:
            continue
        oldName = os.path.join(folder_path, filename)
        # 如果filename已经在新文件名列表中，则不需要重命名
        if filename in newNameList:
            continue

        # 找到合适的newName，防止覆盖原有的同名文件
        while True:
            tmp = str(count + int(startNumber)).zfill(6) + "." + suffix
            newName = os.path.join(folder_path, tmp)
            if tmp in filenames:
                count += 1
            else:
                break

        changeList.append("文件" + filename + "被修改为" + tmp)
        os.rename(oldName, newName)
        count += 1
        num += 1

    print("任务完成，共修改了" + str(num) + "个文件\n")


image_path = r'./tmp/all'

renameFiles(image_path, startNumber=1, suffix='jpg')
