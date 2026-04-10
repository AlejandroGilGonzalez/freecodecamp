# 21/09/2025 Daily Challenge

# Given a video size, a unit for the video size, a hard drive capacity,and a unit for the hard drive,
# return the number of videos the hard drive can store using the following constraints:

"""
- The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
- If not given one of the video units above, return "Invalid video unit".
- The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
- If not given one of the hard drive units above, return "Invalid drive unit".
- Return the number of whole videos the drive can fit.

Use the following conversions:

Unit	Equivalent
1 B	    1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
1 TB	1000 GB


"""

def number_of_videos(video_size:int, video_unit:str, drive_size:int, drive_unit:str) -> int or str:

    # Convert the video_size to bytes:

    if video_unit == "B":
        bytes_video_size = video_size
    elif "KB" in video_unit:
        bytes_video_size = video_size * 1000
    elif "MB" in video_unit:
        bytes_video_size = video_size * 1000000
    elif "GB" in video_unit:
        bytes_video_size = video_size * 1000000000
    
    # If video unit is not part of the previous ones, return invalid video unit:
    
    else:
        return "Invalid video unit"

    # Convert the drive size to bytes:

    if "GB" in drive_unit:
        bytes_drive_size = drive_size * 1000000000
    elif "TB" in drive_unit:
        bytes_drive_size = drive_size * 1000000000000
    
    # If drive unit is not part of the previous ones, return Invalid drive unit:

    else:
        return "Invalid drive unit"
    
    # Return the maximum amount of videos that can fit in drive:

    result = bytes_drive_size // bytes_video_size

    return result

number_of_videos(500, "MB", 100, "GB")