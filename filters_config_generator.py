import os
import importlib.util
import inspect

def load_module(filepath):
    spec = importlib.util.spec_from_file_location("module", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def get_filter_info(filepath):
    module = load_module(filepath)
    filter_data_func = getattr(module, "get_filter_data", None)
    if filter_data_func and inspect.isfunction(filter_data_func):
        return filter_data_func()
    else:
        return None


def generate_py_code(directory):
    py_code = "from filters import *\n\nFILTERS = {}\n\n"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "__init__.py": 
                filepath = os.path.join(root, file)
                folder_name = os.path.basename(os.path.dirname(filepath))
                module_name = os.path.splitext(os.path.basename(filepath))[0]
                py_code += f"from filters.{folder_name} import {module_name}\n"

    py_code += "\nFILTERS = {\n"

    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if dir_name != "__pycache__":  
                py_code += f'    "{dir_name}": {{\n'
                for file in os.listdir(os.path.join(directory, dir_name)):
                    if file.endswith(".py") and file != "__init__.py": 
                        module_name = os.path.splitext(file)[0]
                        py_code += f'        "{module_name}": {{\n'
                        py_code += f'            "apply": {module_name}.apply_effect,\n'
                        filter_info = get_filter_info(os.path.join(directory, dir_name, file))
                        if filter_info:
                            py_code += '            "parameters": {\n'
                            for param, value in filter_info["parameters"].items():
                                py_code += f'                "{param}": {value},\n'
                            py_code += '            }\n'
                        py_code += '        },\n'
                py_code += '    },\n'

    py_code += "}\n"
        
    return py_code

directory_path = "filters"
generated_py_code = generate_py_code(directory_path)

with open("effects_settings.py", "w") as py_file:
    py_file.write(generated_py_code)

print("Archivo 'effects_settings.py' creado con éxito.")
