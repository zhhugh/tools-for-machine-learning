import os


def delete_images(image_path):
    '''
    删除指定图片和标签
    :param image_path: 要删除的图片路径
    :return:
    '''
    data_path, label_path = find_txt_relate_to_image(image_path)
    if os.path.exists(image_path) and os.path.exists(label_path):
        os.remove(image_path)
        os.remove(label_path)
    else:
        print("the file does't exit")
    renameFiles(os.path.join(data_path, 'images'), 0, 'jpg')


def find_txt_relate_to_image(image_path):
    data_path = os.path.dirname(os.path.dirname(image_path))
    label_name = os.path.split(image_path)[1].split('.')[0] + '.txt'
    label_path = os.path.join(data_path, 'labels', label_name)
    return data_path, label_path


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
        _, label_path = find_txt_relate_to_image(oldName)
        # 如果filename已经在新文件名列表中，则不需要重命名
        if filename in newNameList:
            continue

        # 找到合适的newName，防止覆盖原有的同名文件
        while True:
            tmp = str(count + int(startNumber)).zfill(6) + "." + suffix
            newName = os.path.join(folder_path, tmp)
            _, new_label_path = find_txt_relate_to_image(newName)
            if tmp in filenames:
                count += 1
            else:
                break

        changeList.append("文件" + filename + "被修改为" + tmp)
        os.rename(oldName, newName)
        os.rename(label_path, new_label_path)
        print(label_path)
        print(new_label_path)
        count += 1
        num += 1

    print("任务完成，共修改了" + str(num) + "个文件\n")


image_path = r'C:\Users\zhouhan\Desktop\tmp\打标签\images'
# delete_images(image_path)

renameFiles(image_path, startNumber=299, suffix='jpg')