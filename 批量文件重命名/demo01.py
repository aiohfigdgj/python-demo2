import os

def shift(folder, pre):
    files = os.listdir(folder)
    files.sort()
    for i, name in enumerate(files, 1):
        ext = os.path.splitext(name)[1]
        new_name = f'{pre}_{i}{ext}'
        os.rename(
            os.path.join(folder, name),
            os.path.join(folder, new_name)
        )
        print(f"{name} -> {new_name}")

shift('test','hhh')