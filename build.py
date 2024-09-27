# 使用 PyInstaller 将 Python 程序生成可直接运行的exe程序
import site
import PyInstaller.__main__
import os


def build_exe():
    # 获取 site-packages 目录列表
    site_packages_paths = site.getsitepackages()

    # 查找包含 maa/bin 的路径
    maa_bin_path = None
    for path in site_packages_paths:
        potential_path = os.path.join(path, 'maa', 'bin')
        if os.path.exists(potential_path):
            maa_bin_path = potential_path
            break
    if maa_bin_path is None:
        raise FileNotFoundError("未找到包含 maa/bin 的路径")
    
    # 构建 --add-data 参数
    add_data_param = f'{maa_bin_path}{os.pathsep}maa/bin'

    # 查找包含 MaaAgentBinary 的路径
    maa_bin_path2 = None
    for path in site_packages_paths:
        potential_path = os.path.join(path, 'MaaAgentBinary')
        if os.path.exists(potential_path):
            maa_bin_path2 = potential_path
            break

    if maa_bin_path2 is None:
        raise FileNotFoundError("未找到包含 MaaAgentBinary 的路径")

    # 构建 --add-data 参数
    add_data_param2 = f'{maa_bin_path2}{os.pathsep}MaaAgentBinary'

    # 获取当前文件目录
    path = os.path.dirname(__file__)

    # 设置必需 DLL 文件的路径(不清楚缺dll的原因，总之把pyinstaller警告缺失的dll加进去就能用了)
    dll_path = None
    potential_path = os.path.join(path, "assets", "python", "dll")
    if os.path.exists(potential_path):
        dll_path = potential_path
    if dll_path is None:
        raise FileNotFoundError("未找到包含 dll 的路径")

    # 构建 --add-binary 参数.--add-binary="源地址;目标地址"
    add_binary_param = f"{dll_path}{os.pathsep}./"
    
    '''
    pyinstall打包后, 运行单独的exe会解压到一个临时文件夹中。之后再调用python运行python脚本。关闭程序时, 会删除临时文件夹。 
    默认情况下, 这个临时文件夹的路径位于: 
    '''
    # C:\Users\User\AppData\Local\Temp, 这个临时文件夹名称为_MEIxxxxxx, 其中XXXX为一个随机数。 
    '''注意：正常情况下, 这个临时文件夹会被删除, 但是如果exe被意外强制关闭, 将无法被删除, c盘就会被占用。
    要更改这个文件夹的路径, 可以通过--runtime-tmpdir设置, 或者在spec文件中runtime_tmpdir中设置(要和exe同一个文件夹下, 设置为'.').
    '''

    tmpdir="."
    # 运行 PyInstaller
    PyInstaller.__main__.run(
        [
            "assets/python/pi_cli.py",
            "--onefile",
            "--name=MATOT",
            f"--add-binary={add_binary_param}",
            f"--add-data={add_data_param}",
            f"--add-data={add_data_param2}",
            "--i=assets/python/matot.ico",
            "--clean",
            f"--runtime-tmpdir={tmpdir}"
        ]
    )
    

    # 删除依赖文件,只保留打包好的应用到install文件夹
    import shutil

    source_path = "./dist/MATOT.exe"
    destination_path = "./install"
    # 打包好的应用移动到install文件夹
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved successfully from {source_path} to {destination_path}")
    except FileNotFoundError:
        print("The source or destination path does not exist")
    except PermissionError:
        print("You do not have permission to move the file")
    except Exception as e:
        print("Error occurred while moving the file:", e)

    # 删除依赖文件
    def remove_file(file_path):
        try:
            os.remove(file_path)  # 或者使用 os.unlink(file_path)
            print("File " + file_path + " removed successfully")
        except FileNotFoundError:
            print("File does not exist")
        except PermissionError:
            print("You do not have permission to delete this file")
        except Exception as e:
            print("Error occurred:", e)

    def remove_folder(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(
                "Folder " + folder_path + " and all its contents removed successfully"
            )
        except Exception as e:
            print("Error occurred while deleting folder:", e)

    remove_folder("build")
    remove_folder("dist")
    remove_file("MATOT.spec")


if __name__ == "__main__":
    build_exe()
