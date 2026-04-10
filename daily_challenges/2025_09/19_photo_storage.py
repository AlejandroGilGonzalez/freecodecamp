# 19/09/2026 Daily Challenge

# Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB),
# return the number of photos the hard drive can store using the following constraints:

# 1 gigabyte equals 1000 megabytes.
# Return the number of whole photos the drive can store.

def number_of_photos(photo_size_mb:int, drive_size_gb:int) -> int:

    # Get the number of mb the drive can store:

    size = drive_size_gb * 1000

    # Get the total number of photos dividing total storage per mb:

    result = size // photo_size_mb

    return result

number_of_photos(4, 256)