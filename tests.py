from functions.get_files_info import get_files_info

result_1 = get_files_info("calculator", ".")
print(result_1)

result_2 = get_files_info("calculator", "pkg")
print(result_2)

result_3 = get_files_info("calculator", "/bin")
print(result_3)