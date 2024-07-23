def write_result(file_path, results):

    try:
        with open(file_path, 'w') as result_file:
            for result in results:
                result_file.write(result + '\n')
    except Exception as e:
        raise RuntimeError(f"An error occurred while writing to the file: {e}")