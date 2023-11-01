import os
import openpyxl


# Function to find files containing a specific word
def find_files_with_word(directory, search_word):
    matching_files = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if search_word in open(os.path.join(root, filename), 'r').read():
                matching_files.append(os.path.join(root, filename))
    return matching_files


# Function to create an Excel file and write the file names
def write_to_excel(file_list, output_file):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Matching Files"

    for index, file in enumerate(file_list, start=1):
        worksheet.cell(row=index, column=1, value=file)

    workbook.save(output_file)


if __name__ == "__main__":
    directory = r'C:\Users\dpierce\Desktop'
    # Replace above with the directory path you want to search in
    search_word = "p"
    # Replace above with the word you want to search for
    output_file = "matching_files.xlsx"

    matching_files = find_files_with_word(directory, search_word)

    if matching_files:
        write_to_excel(matching_files, output_file)
        print(f"Found and saved {len(matching_files)} matching files in {output_file}")
    else:
        print(f"No files containing '{search_word}' found in the directory.")
