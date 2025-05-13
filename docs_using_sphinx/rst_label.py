import os

def add_labels_to_rst_files(rst_dir):
    for root, dirs, files in os.walk(rst_dir):
        for file in files:
            if file.endswith('.rst'):
                file_path = os.path.join(root, file)
                module_name = file.replace('.rst', '')
                label = f'.. _module_{module_name}:\n\n'
                with open(file_path, 'r+') as f:
                    content = f.read()
                    if content.find(label) != -1:
                        f.seek(0, 0)
                        f.write(label + content)

if __name__ == "__main__":
    rst_directory = './reference'  # 替换为实际的 .rst 文件目录
    add_labels_to_rst_files(rst_directory)