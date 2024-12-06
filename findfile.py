import os

def search_files(directory):
    result_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if "uh-oh" not in file:
                result_files.append(os.path.join(root, file))
    return result_files

# Example usage
directory_path = "D:\Steam\steamapps\common\Enigma of Fear\Labyrinthus"
files = search_files(directory_path)
for file in files:
    print(file)