import os

file_path = "alg/MobileNet.h5"
print("Full path:", os.path.abspath(file_path))

new_model = load_model(file_path)
