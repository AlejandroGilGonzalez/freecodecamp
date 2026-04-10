# 20/09/2025 Daily Challenge

# Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), 
# return the number of files the hard drive can store using the following constraints:

"""
- The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
- Return the number of whole files the drive can fit.

Use the following conversions:

Unit	Equivalent
1 B	    1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB

"""

def number_of_files(file_size:int, file_unit:str, drive_size_gb:int or float) -> int:

    # Convert the file_size to bytes:

    if "KB" in file_unit:
        byte_file_size = file_size * 1000
    elif "MB" in file_unit:
        byte_file_size = file_size * 1000000
    elif "GB" in file_unit:
        byte_file_size = file_size * 1000000000
    else:
        byte_file_size = file_size
    
    # Convert drive_size_gb to bytes:

    bytes_drive_size = drive_size_gb * 1000000000

    # Divide drive size by file size in bytes:

    result = int(bytes_drive_size // byte_file_size)

    return result

number_of_files(4096, "B", 1.5)