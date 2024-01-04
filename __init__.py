import subprocess
import os

def clone_anytext():
    anytext_git_url = "https://github.com/tyxsspa/AnyText.git"
    anytext_dir_name = "AnyText"

    # 检查AnyText目录是否已经存在
    if not os.path.isdir(anytext_dir_name):
        print("Cloning AnyText repository...")
        subprocess.run(["git", "clone", anytext_git_url, anytext_dir_name], check=True)
    else:
        print("AnyText repository already exists.")

try:
    clone_anytext()
except Exception as e:
    print(f"Error cloning AnyText repository: {e}")


from .AnyTextNodeTest import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
