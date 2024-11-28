def sort_text(file_path):

    # Step 1: Read the file
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Step 2: Parse lines to extract ratings and sort them
    sorted_lines = sorted(
        lines, 
        key=lambda line: float(line.split("Rating:")[1].strip()), 
        reverse=True
    )

    # Step 3: Write the sorted lines back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(sorted_lines)

    print("File sorted by ratings in descending order.")
