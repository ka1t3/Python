# def count_vowels(text):
#     vowels = "aeiou"
#     count = 0
    
#     for char in text.lower():
#         if char in vowels:
#             count += 1
    
#     return count

# # Test de la fonction
# input_string = input("Entrez une chaîne de caractères : ")
# result = count_vowels(input_string)
# print(f"Nombre de voyelles : {result}")

# # # _______________________________________


'''
Test 2 :
Problème : Additionner les valeurs d'un dictionnaire
Ce problème est fréquemment utilisé dans les entretiens techniques pour évaluer votre compréhension des structures de données en Python.

Énoncé : Écrivez une fonction qui prend en paramètre un dictionnaire dont les valeurs sont des nombres (entiers ou flottants) et retourne la somme de toutes ces valeurs.

Par exemple :

Pour {"a": 1, "b": 2, "c": 3}, la fonction doit retourner 6

Pour {"x": 10.5, "y": 20, "z": 3.7}, la fonction doit retourner 34.2

Pour un dictionnaire vide {}, la fonction doit retourner 0'''


# def sum_dict_values(input_dict):
#     if not input_dict:  # Handle empty dictionary case
#         return 0
        
#     total = 0
#     for value in input_dict.values():
#         total += value
        
#     return total

# # Test cases
# print(sum_dict_values({"a": 1, "b": 2, "c": 3}))  # Should print 6
# print(sum_dict_values({"x": 10.5, "y": 20, "z": 3.7}))  # Should print 34.2
# print(sum_dict_values({}))  # Should print 0


#  Alternative version 
#  def sum_dict_values(input_dict):
#     return sum(input_dict.values())

# # # ____________________________________________________
# # # ____________________________________________________

# # def move_zeros(nums):
# #     """
# #     Move all zeros in the array to the end while preserving the order of other elements
    
# #     Args:
# #         nums: List of integers
        
# #     Returns:
# #         List with zeros moved to the end
# #     """
# #     non_zeros = [num for num in nums if num != 0]
# #     zeros = [0] * (len(nums) - len(non_zeros))
# #     return non_zeros + zeros

# Test cases
# print(move_zeros([0, 1, 0, 3, 12]))  # Should output [1, 3, 12, 0, 0]
# print(move_zeros([0]))  # Should output [0]
# print(move_zeros([1, 2, 3]))  # Should output [1, 2, 3]

# # ____________________________________________________
# # ____________________________________________________

# # Problem Statement: Write a function that reverses a string.

# def reverse_string(s):
#     """
#     Reverse a string
    
#     Args:
#         s: Input string
        
#     Returns:
#         Reversed string
#     """
#     return s[::-1]

# # Test cases
# print(reverse_string("hello"))  # Should output "olleh"
# print(reverse_string("Python"))  # Should output "nohtyP"
# print(reverse_string(""))  # Should output ""

# # ____________________________________________________
# # ____________________________________________________

# # Problem Statement: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one number that is missing from the array.

# def missing_number(nums):
#     """
#     Find the missing number in a sequence
    
#     Args:
#         nums: List of integers from 0 to n with one number missing
        
#     Returns:
#         The missing number
#     """
#     nums.sort()
    # for i,v in enumerate(nums):
    #     if (i != v):
    #         return v-1
    #     if v == len(nums)-1:
    #         return v+1
#     pass

# # Test cases
# print(missing_number([3, 0, 1]))  # Should output 2
# print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Should output 8
# print(missing_number([0]))  # Should output 1

# def missing_number(nums):
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum



# # # ____________________________________________________
# # # ____________________________________________________

# even =[]
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     if number % 2 == 0:
#         even.append(number) 
# print(even)

# # # ____________________________________________________
# # # ____________________________________________________

# numse = [1,1,1,3,3,4,3,2,4,2]

# def contains_duplicates(nums):
#     if len(set(nums)) == len(nums):
#         return False
#     else:
#         return True
    
# print(contains_duplicates(numse))


# # # ____________________________________________________
# # # ____________________________________________________


# pp = [[1,1],[3,4],[-1,0]]

# def minTimeToVisitAllPoints(points):
#     time = 0
#     for i in range(1, len(points)):
#         x1, y1 = points[i-1]
#         x2, y2 = points[i]
#         time += max(abs(x2-x1), abs(y2-y1))
#     return time

# print(minTimeToVisitAllPoints(pp))

# # # ____________________________________________________
# # # ____________________________________________________

# matrix =[[1,2,3], [4,5,6], [7,8,9]]
# for i in range(1, len(matrix)):
# output = [1, 2, 3, 6, 9, 8, 7, 4, 5]

# res = 0
# res = matrix[0]
# res.append(matrix[1][-1])
# x = matrix[0][-1] + matrix[0][-1]
# res.append(x)
# print(res)

# # # ____________________________________________________
# # # ____________________________________________________

'''For example: given stream ['apple, facebook, google', 'banana, facebook', 'facebook, google, tesla', 'intuit, google, facebook'], if the keyword is ['apple'] the output should ['facebook', 'google'] because only 'apple, facebook, google' has apple. Similarly if the keyword is ['facebook', 'google'], the output should ['apple', 'tesla', 'intuit']. The output can be in any order and can be put into a single list/array.'''

# def find_related_words(data, keywords):
#     result = []
    
#     # Go through each string in the data
#     for string in data:
#         # Split the string by comma and remove spaces
#         words = [word.strip() for word in string.split(',')]
        
#         # Check if ALL keywords are in this string
#         all_keywords_found = True
#         for keyword in keywords:
#             if keyword not in words:
#                 all_keywords_found = False
#                 break
        
#         # If all keywords are found, add other words to result
#         if all_keywords_found:
#             for word in words:
#                 if word not in keywords and word not in result:
#                     result.append(word)
    
#     return result

# or 
# def find_related_words(stream, keywords):
#     keyword_set = set(keywords)
#     output_tags = set()
#         # Process the stream of tags
#     for line in stream:
#         tags = line.split(', ')
#         tag_set = set(tags)
#         # Check if all keywords are present in the current set of tags
#         if keyword_set.issubset(tag_set):
#             # Add all tags from this line to the output set, except the keyword tags
#             output_tags.update(tag_set - keyword_set)

#     # Convert set to list before returning
#     return list(output_tags)

# Test data
# data = [
#     'apple, facebook, google', 
#     'banana, facebook', 
#     'facebook, google, tesla', 
#     'intuit, google, facebook'
# ]

# # Test case 1: keyword = ['apple']
# result1 = find_related_words(data, ['apple'])
# print(f"Keywords ['apple']: {result1}")
# # Output: ['facebook', 'google']

# # Test case 2: keywords = ['facebook', 'google']
# result2 = find_related_words(data, ['facebook', 'google'])
# print(f"Keywords ['facebook', 'google']: {result2}")
# # Output: ['apple', 'tesla', 'intuit']


# # # ____________________________________________________
# # # ____________________________________________________

'''
You are given the list of logs of HTTP requests in the given format:
[IP, HTTP Verb, status, response time, size, request time]
Write the code to answer the various queries. For example, list all HTTP requests for the last 2 months or show all requests with 200 status, etc.
'''

# logs = [
#     ["192.168.1.1", "GET", 200, 150, 1024, "2025-03-15 10:30:00"],
#     ["10.0.0.5", "POST", 404, 200, 512, "2025-05-20 14:22:30"],
#     ["192.168.1.1", "GET", 500, 1500, 2048, "2025-05-22 09:15:45"],
#     # ... more logs
# ]

# from datetime import datetime, timedelta

# # Sample logs data - each log is a list with 6 elements:
# # [IP, HTTP Verb, status, response time, size, request time]
# logs = [
#     ["192.168.1.1", "GET", 200, 150, 1024, "2025-03-15 10:30:00"],
#     ["10.0.0.5", "POST", 404, 200, 512, "2025-05-20 14:22:30"],
#     ["192.168.1.1", "GET", 500, 1500, 2048, "2025-05-22 09:15:45"],
#     ["172.16.0.1", "GET", 200, 100, 2048, "2025-04-01 12:00:00"],
# ]

# def filter_logs_for_last_2_months_or_status_200(logs, current_date):
#     """
#     Filter logs to show:
#     1. All requests from the last 2 months OR
#     2. All requests with status 200
#     """
    
#     # Step 1: Calculate what date was 2 months ago
#     # We use 60 days as an approximation for 2 months
#     two_months_ago = current_date - timedelta(days=60)
    
#     # Step 2: Create an empty list to store our filtered results
#     filtered_logs = []
    
#     # Step 3: Go through each log entry one by one
#     for log in logs:
#         # Step 4: Extract each piece of information from the log
#         # This is called "unpacking" - we take the list and assign each element to a variable
#         ip, verb, status, response_time, size, request_time_str = log
        
#         # Step 5: Convert the time string into a datetime object so we can compare dates
#         # The string "2025-03-15 10:30:00" becomes a datetime object
#         request_time = datetime.strptime(request_time_str, "%Y-%m-%d %H:%M:%S")
        
#         # Step 6: Check if this request happened in the last 2 months
#         # We compare the request time with our "two_months_ago" date
#         is_recent = request_time >= two_months_ago
        
#         # Step 7: Check if this request has status code 200 (success)
#         is_status_200 = (status == 200)
        
#         # Step 8: If EITHER condition is true, we want to keep this log
#         # The "or" means we keep logs that are either recent OR have status 200 (or both)
#         if is_recent or is_status_200:
#             filtered_logs.append(log)  # Add this log to our results
    
#     # Step 9: Return all the logs that matched our criteria
#     return filtered_logs

# # Example usage:
# current_date = datetime(2025, 5, 26, 9, 33, 0)  # Today's date
# filtered_results = filter_logs_for_last_2_months_or_status_200(logs, current_date)

# # Print each filtered log
# print("Filtered logs (last 2 months OR status 200):")
# for log in filtered_results:
#     print(log)


# # # ____________________________________________________
# # # ____________________________________________________

'''Given an array of latencies, numBuckets, buketWidth
We want to know the number of latencies belongs to each bucket. Create numBuckets number of bucket of length bucketWidth starting 0.
Any latencies higher than the last bucket goes into the last bucket.
Return an array ans of size numBuckets where ans[i] is the number of latencies in ith bucket.'''

# latencies = [5, 15, 25, 35, 8, 12, 22]
# numBuckets = 3
# bucketWidth = 10

# def latency_buckets(latencies, numBuckets, bucketWidth):

#     # Step 1: Create a list of zeros to count items in each bucket
#     # If numBuckets = 3, this creates [0, 0, 0]
#     bucket_counts = [0] * numBuckets

#     # Step 2: Go through each latency value one by one
#     for latency in latencies:
        
#         # Step 3: Calculate which bucket this latency belongs to
#         # We divide the latency by bucket width to find the bucket index
#         # For example: latency=15, bucketWidth=10 → 15//10 = 1 (bucket 1)
#         bucket_index = latency // bucketWidth
        
#         # Step 4: Handle the special case where latency is too high
#         # If the calculated bucket_index is beyond our last bucket,
#         # put it in the last bucket instead
#         if bucket_index >= numBuckets:
#             bucket_index = numBuckets - 1  # Last bucket index
        
#         # Step 5: Increment the count for this bucket
#         # Add 1 to the count of items in this bucket
#         bucket_counts[bucket_index] += 1

#     # Step 6: Return the final counts for all buckets
#     return bucket_counts

    # Example usage with detailed trace:
    # latencies = [5, 15, 25, 35, 8, 12, 22]
    # numBuckets = 3
    # bucketWidth = 10

# Let's trace through each latency:
# Bucket ranges: [0-9], [10-19], [20+]
# 
# latency=5:  5//10 = 0 → bucket 0
# latency=15: 15//10 = 1 → bucket 1  
# latency=25: 25//10 = 2 → bucket 2
# latency=35: 35//10 = 3, but 3 >= 3, so → bucket 2 (last bucket)
# latency=8:  8//10 = 0 → bucket 0
# latency=12: 12//10 = 1 → bucket 1
# latency=22: 22//10 = 2 → bucket 2
#
# Final counts: bucket 0 = 2, bucket 1 = 2, bucket 2 = 3

# result = latency_buckets(latencies, numBuckets, bucketWidth)
# print(result)  # Output: [2, 2, 3]

# Explanation of the result:
# Bucket 0 (0-9):   [5, 8] = 2 items
# Bucket 1 (10-19): [15, 12] = 2 items  
# Bucket 2 (20+):   [25, 35, 22] = 3 items


# # # ____________________________________________________
# # # ____________________________________________________

'''Given root directory find the total sizes for the files in the sub-directories.'''
'''
root/
├── subdir1/
│   ├── file1.txt (100 bytes)
│   └── file2.txt (200 bytes)
├── subdir2/
│   ├── file3.txt (150 bytes)
│   └── nested/
│       └── file4.txt (50 bytes)
└── file5.txt (300 bytes - this is in root, not a subdirectory)
'''

# import os

# def get_subdirectory_sizes(root_path):    
#     # Step 1: Create a dictionary to store the results
#     # Key = subdirectory name, Value = total size in bytes
#     subdirectory_sizes = {}
    
#     # Step 2: Check if the root path exists and is a directory
#     if not os.path.exists(root_path) or not os.path.isdir(root_path):
#         print(f"Error: {root_path} is not a valid directory")
#         return subdirectory_sizes
    
#     # Step 3: Get all items in the root directory
#     try:
#         with os.scandir(root_path) as entries:
#             for entry in entries:
#                 # Step 4: Only process directories (skip files in root)
#                 if entry.is_dir():
#                     # Step 5: Calculate the total size for this subdirectory
#                     total_size = calculate_directory_size(entry.path)
#                     # Step 6: Store the result using the directory name as key
#                     subdirectory_sizes[entry.name] = total_size
                    
#     except PermissionError:
#         print(f"Permission denied accessing {root_path}")
#     except Exception as e:
#         print(f"Error scanning directory: {e}")
    
#     return subdirectory_sizes

# def calculate_directory_size(directory_path):
   
#     total_size = 0
    
#     try:
#         # Step 1: Use os.scandir to efficiently iterate through directory contents
#         with os.scandir(directory_path) as entries:
#             for entry in entries:
                
#                 # Step 2: If it's a file, add its size to the total
#                 if entry.is_file():
#                     # entry.stat().st_size gives us the file size in bytes
#                     total_size += entry.stat().st_size
                
#                 # Step 3: If it's a directory, recursively calculate its size
#                 elif entry.is_dir():
#                     # Recursive call: calculate size of this subdirectory
#                     # and add it to our total
#                     total_size += calculate_directory_size(entry.path)
                    
#     except PermissionError:
#         print(f"Permission denied accessing {directory_path}")
#     except Exception as e:
#         print(f"Error calculating size for {directory_path}: {e}")
    
#     return total_size

# def format_size(size_bytes):
#     """
#     Convert bytes to human-readable format (KB, MB, GB)
#     This is a helper function to make the output more readable
#     """
    
#     if size_bytes == 0:
#         return "0 B"
    
#     # Define size units
#     units = ['B', 'KB', 'MB', 'GB', 'TB']
#     unit_index = 0
#     size = float(size_bytes)
    
#     # Keep dividing by 1024 until we get a reasonable number
#     while size >= 1024.0 and unit_index < len(units) - 1:
#         size /= 1024.0
#         unit_index += 1
    
#     # Format to 2 decimal places
#     return f"{size:.2f} {units[unit_index]}"

# # Example usage:
# def main():
#     # Replace this with your actual directory path
#     root_directory = "."  # Current directory
    
#     print(f"Calculating subdirectory sizes for: {os.path.abspath(root_directory)}")
#     print("-" * 50)
    
#     # Get the sizes
#     sizes = get_subdirectory_sizes(root_directory)
    
#     # Display results
#     if sizes:
#         for subdir, size in sizes.items():
#             print(f"{subdir}: {format_size(size)} ({size:,} bytes)")
#     else:
#         print("No subdirectories found or unable to access directory")

# # Alternative simpler version if you just want basic functionality:
# def simple_subdirectory_sizes(root_path):
#     """
#     Simplified version - less error handling but easier to understand
#     """
#     subdirectory_sizes = {}
    
#     # Get all entries in root directory
#     for entry in os.scandir(root_path):
#         if entry.is_dir():  # Only process directories
#             total_size = 0
            
#             # Walk through all files in this subdirectory recursively
#             for dirpath, dirnames, filenames in os.walk(entry.path):
#                 for filename in filenames:
#                     filepath = os.path.join(dirpath, filename)
#                     try:
#                         total_size += os.path.getsize(filepath)
#                     except (OSError, FileNotFoundError):
#                         # Skip files we can't access
#                         continue
            
#             subdirectory_sizes[entry.name] = total_size
    
#     return subdirectory_sizes

# if __name__ == "__main__":
#     main()

# # # ____________________________________________________
# # # ____________________________________________________


'''Given a path string, parse it and calculate the total_size.'''

# import os

# def calculate_total_size_from_path(path_string):
#     """
#     Parse a path string containing file information and calculate total size
    
#     Args:
#         path_string: String containing file paths and sizes
        
#     Returns:
#         Total size in bytes
#     """
    
#     # Step 1: Initialize total size to 0
#     total_size = 0
    
#     # Step 2: Handle empty or None input
#     if not path_string:
#         return total_size
    
#     # Step 3: Split the path string by commas to get individual file entries
#     # Example: "file1.txt:1024,file2.txt:2048" becomes ["file1.txt:1024", "file2.txt:2048"]
#     file_entries = path_string.split(',')
    
#     # Step 4: Process each file entry
#     for entry in file_entries:
#         # Step 5: Remove any extra whitespace from the entry
#         entry = entry.strip()
        
#         # Step 6: Skip empty entries
#         if not entry:
#             continue
        
#         # Step 7: Split each entry by colon to separate path and size
#         # Example: "file1.txt:1024" becomes ["file1.txt", "1024"]
#         if ':' in entry:
#             parts = entry.split(':')
            
#             # Step 8: Get the size part (last element after splitting by colon)
#             size_str = parts[-1].strip()  # Take the last part in case path has colons
            
#             # Step 9: Convert size string to integer and add to total
#             try:
#                 file_size = int(size_str)
#                 total_size += file_size
#             except ValueError:
#                 # Step 10: If conversion fails, print error and skip this entry
#                 print(f"Warning: Could not parse size from '{entry}'")
#                 continue
#         else:
#             # Step 11: If no colon found, this entry doesn't have size info
#             print(f"Warning: No size information found in '{entry}'")
    
#     return total_size

# # Alternative version that handles different formats
# def calculate_total_size_flexible(path_string):
#     """
#     More flexible version that can handle different formats
#     Supports formats like:
#     - "file1.txt:1024,file2.txt:2048"
#     - "file1.txt(1024)|file2.txt(2048)"
#     - "/path/to/file1.txt:1024,/path/to/file2.txt:2048"
#     """
    
#     total_size = 0
    
#     if not path_string:
#         return total_size
    
#     # Step 1: Handle different separators (comma, pipe, semicolon)
#     # Replace common separators with comma for consistent processing
#     normalized_string = path_string.replace('|', ',').replace(';', ',')
    
#     # Step 2: Split by comma
#     file_entries = normalized_string.split(',')
    
#     for entry in file_entries:
#         entry = entry.strip()
#         if not entry:
#             continue
        
#         # Step 3: Try different formats to extract size
#         size = extract_size_from_entry(entry)
#         if size is not None:
#             total_size += size
    
#     return total_size

# def extract_size_from_entry(entry):
#     """
#     Helper function to extract size from different entry formats
#     """
    
#     # Format 1: "filename:size" or "/path/to/filename:size"
#     if ':' in entry:
#         parts = entry.split(':')
#         size_str = parts[-1].strip()
#         try:
#             return int(size_str)
#         except ValueError:
#             pass
    
#     # Format 2: "filename(size)" or "/path/to/filename(size)"
#     if '(' in entry and ')' in entry:
#         # Find content between last ( and )
#         start = entry.rfind('(')
#         end = entry.rfind(')')
#         if start < end:
#             size_str = entry[start+1:end].strip()
#             try:
#                 return int(size_str)
#             except ValueError:
#                 pass
    
#     # Format 3: "filename size" (space separated)
#     parts = entry.split()
#     if len(parts) >= 2:
#         size_str = parts[-1].strip()
#         try:
#             return int(size_str)
#         except ValueError:
#             pass
    
#     print(f"Warning: Could not extract size from '{entry}'")
#     return None

# # Example usage and testing:
# def main():
#     # Test different formats
    
#     # Format 1: colon separated
#     path_str1 = "/home/user/file1.txt:1024,/home/user/docs/file2.txt:2048,/home/user/images/photo.jpg:5120"
#     total1 = calculate_total_size_from_path(path_str1)
#     print(f"Format 1 total: {total1} bytes")  # Should output: 8192 bytes
    
#     # Format 2: parentheses
#     path_str2 = "file1.txt(1024)|file2.txt(2048)|photo.jpg(5120)"
#     total2 = calculate_total_size_flexible(path_str2)
#     print(f"Format 2 total: {total2} bytes")  # Should output: 8192 bytes
    
#     # Format 3: space separated
#     path_str3 = "file1.txt 1024,file2.txt 2048,photo.jpg 5120"
#     total3 = calculate_total_size_flexible(path_str3)
#     print(f"Format 3 total: {total3} bytes")  # Should output: 8192 bytes
    
#     # Test with actual file paths (if they exist)
#     test_actual_paths()

# def test_actual_paths():
#     """
#     Test with actual file paths to get real file sizes
#     """
#     # Get current directory files and their sizes
#     current_dir = "."  # Current directory
    
#     try:
#         # Get all files in current directory
#         files_with_sizes = []
        
#         for filename in os.listdir(current_dir):
#             filepath = os.path.join(current_dir, filename)
            
#             # Only process files (not directories)
#             if os.path.isfile(filepath):
#                 try:
#                     file_size = os.path.getsize(filepath)
#                     files_with_sizes.append(f"{filename}:{file_size}")
#                 except OSError:
#                     continue
        
#         # Create path string from actual files
#         if files_with_sizes:
#             path_string = ",".join(files_with_sizes)
#             print(f"\nActual files path string: {path_string}")
            
#             total = calculate_total_size_from_path(path_string)
#             print(f"Total size of files in current directory: {total} bytes")
#         else:
#             print("No files found in current directory")
            
#     except Exception as e:
#         print(f"Error accessing files: {e}")

# if __name__ == "__main__":
#     main()




'''
Given a API for file system
Delete(path) -> bool: deletes the file or empty directory, returns false if deletion was not successful.
isDirectory(path) -> bool: checks whether filepath is directory or not.
GetAllFiles(path) -> List<string>: gets the absolute paths of all files in a directory, including other sub-directories.
implement rm -rf.
'''

# def rm_rf(path):
#     """
#     Implement rm -rf functionality using the provided file system API
#     This recursively deletes files and directories, similar to Unix 'rm -rf' command
    
#     Args:
#         path: The path to delete (file or directory)
        
#     Returns:
#         bool: True if deletion was successful, False otherwise
#     """
    
#     # Step 1: Check if the path is a directory
#     if isDirectory(path):
#         # Step 2: If it's a directory, we need to delete all contents first
#         try:
#             # Step 3: Get all files and subdirectories in this directory
#             all_files = GetAllFiles(path)
            
#             # Step 4: Delete each file/subdirectory recursively
#             for file_path in all_files:
#                 # Step 5: Recursively call rm_rf on each item
#                 # This handles both files and subdirectories
#                 if not rm_rf(file_path):
#                     # If any deletion fails, return False
#                     return False
            
#             # Step 6: After all contents are deleted, delete the empty directory
#             return Delete(path)
            
#         except Exception as e:
#             # Step 7: If we can't access the directory contents, return False
#             print(f"Error accessing directory {path}: {e}")
#             return False
    
#     else:
#         # Step 8: If it's a file, simply delete it
#         return Delete(path)

# # Alternative implementation with better error handling and logging
# def rm_rf_verbose(path, verbose=False):
#     """
#     Enhanced version with verbose output and better error handling
    
#     Args:
#         path: The path to delete
#         verbose: If True, prints what's being deleted
        
#     Returns:
#         bool: True if deletion was successful, False otherwise
#     """
    
#     if verbose:
#         print(f"Attempting to delete: {path}")
    
#     # Check if it's a directory
#     if isDirectory(path):
#         if verbose:
#             print(f"Directory detected: {path}")
        
#         try:
#             # Get all contents of the directory
#             all_files = GetAllFiles(path)
            
#             if verbose and all_files:
#                 print(f"Found {len(all_files)} items in directory")
            
#             # Delete all contents recursively
#             for file_path in all_files:
#                 if not rm_rf_verbose(file_path, verbose):
#                     if verbose:
#                         print(f"Failed to delete: {file_path}")
#                     return False
            
#             # Delete the now-empty directory
#             success = Delete(path)
#             if verbose:
#                 if success:
#                     print(f"Successfully deleted directory: {path}")
#                 else:
#                     print(f"Failed to delete directory: {path}")
#             return success
            
#         except Exception as e:
#             if verbose:
#                 print(f"Error processing directory {path}: {e}")
#             return False
    
#     else:
#         # It's a file, delete it directly
#         success = Delete(path)
#         if verbose:
#             if success:
#                 print(f"Successfully deleted file: {path}")
#             else:
#                 print(f"Failed to delete file: {path}")
#         return success

# # Iterative implementation (avoids recursion for very deep directory structures)
# def rm_rf_iterative(path):
#     """
#     Iterative implementation to avoid stack overflow with very deep directories
#     Uses a stack to simulate recursion
#     """
    
#     # Step 1: Create a stack to keep track of paths to process
#     stack = [path]
#     # Step 2: Keep track of directories we need to delete after their contents
#     dirs_to_delete = []
    
#     # Step 3: Process all items in the stack
#     while stack:
#         current_path = stack.pop()
        
#         if isDirectory(current_path):
#             # Step 4: Add directory to deletion list (we'll delete it last)
#             dirs_to_delete.append(current_path)
            
#             try:
#                 # Step 5: Get all contents and add them to the stack
#                 all_files = GetAllFiles(current_path)
#                 # Add in reverse order so we process them in correct order
#                 for file_path in reversed(all_files):
#                     stack.append(file_path)
                    
#             except Exception as e:
#                 print(f"Error accessing directory {current_path}: {e}")
#                 return False
#         else:
#             # Step 6: It's a file, delete it immediately
#             if not Delete(current_path):
#                 return False
    
#     # Step 7: Delete directories in reverse order (deepest first)
#     for directory in reversed(dirs_to_delete):
#         if not Delete(directory):
#             return False
    
#     return True

# # Example usage and testing
# def test_rm_rf():
#     """
#     Test function to demonstrate usage
#     """
    
#     # Test case 1: Delete a single file
#     print("Test 1: Deleting a single file")
#     result1 = rm_rf("/path/to/single_file.txt")
#     print(f"Result: {result1}")
    
#     # Test case 2: Delete a directory with contents
#     print("\nTest 2: Deleting a directory")
#     result2 = rm_rf_verbose("/path/to/directory", verbose=True)
#     print(f"Result: {result2}")
    
#     # Test case 3: Delete using iterative approach
#     print("\nTest 3: Deleting using iterative approach")
#     result3 = rm_rf_iterative("/path/to/another_directory")
#     print(f"Result: {result3}")

# # Wrapper function that matches the exact rm -rf behavior
# def rm_rf_command(paths):
#     """
#     Wrapper to handle multiple paths like the actual rm -rf command
    
#     Args:
#         paths: List of paths to delete
        
#     Returns:
#         bool: True if all deletions were successful
#     """
    
#     all_successful = True
    
#     for path in paths:
#         if not rm_rf(path):
#             print(f"rm: cannot remove '{path}': Operation failed")
#             all_successful = False
    
#     return all_successful

# if __name__ == "__main__":
#     # Example usage
#     test_rm_rf()


# __________________________________________________________________________
# __________________________________________________________________________



# f = File('/tmp/my/file.txt')
# f.write(b"hello world")
 
# Write a wrapper class for the file object which allows us to buffer the writes in-memory. The wrapper class, BufferedFile is initialized with a File class object and a buffer size. It has two methods: write and flush. The data should be flushed to disk when the buffer is full, or on demand with a method called flush. All bytes must be stored in the buffer first before being written to disk. The buffer cannot use more memory than the max bytes allowed.
 
# Example usage:
 
# f = File('/tmp/my/file.txt')
# buf_size = 1000
 
# b = BufferedFile(f, buf_size)
# b.write(b"hello world")
# b.flush()

# class BufferedFile:
#     def __init__(self, file_object, buffer_size):
#         # Step 1: Store the original file object
#         self.file = file_object
        
#         # Step 2: Store the maximum buffer size
#         self.max_buffer_size = buffer_size
        
#         # Step 3: Initialize empty buffer to store data temporarily
#         # Using bytes() creates an empty bytes object
#         self.buffer = b""
        
#         # Step 4: Track current buffer size for efficiency
#         self.current_buffer_size = 0
    
#     def write(self, data):
#         # Step 1: Add new data to the existing buffer
#         self.buffer += data
        
#         # Step 2: Update the current buffer size
#         self.current_buffer_size += len(data)
        
#         # Step 3: Check if buffer exceeds maximum size
#         if self.current_buffer_size >= self.max_buffer_size:
#             # Step 4: Automatically flush when buffer is full
#             self.flush()
    
#     def flush(self):
#         # Step 1: Only flush if there's data in the buffer
#         if self.buffer:
#             # Step 2: Write all buffered data to the actual file
#             self.file.write(self.buffer)
            
#             # Step 3: Clear the buffer after successful write
#             self.buffer = b""
            
#             # Step 4: Reset buffer size counter
#             self.current_buffer_size = 0
    
#     def close(self):
#         """
#         Flush any remaining data and close the file
#         Optional method for proper cleanup
#         """
#         # Step 1: Flush any remaining buffered data
#         self.flush()
        
#         # Step 2: Close the underlying file if it has a close method
#         if hasattr(self.file, 'close'):
#             self.file.close()



# __________________________________________________________________________
# __________________________________________________________________________


'''Write a program that prints the first letter of each string on one line, then the second letter of each string on the next line, and so on. For example, if

strings = ["abc", "def", "ghi"]
then your program should print

adg
beh
cfi
'''

'''My solution '''

# strings = ["abc", "def", "ghi"]

# num = len(strings[0])
# for i in range(num):
#     # i = 0
#     new = []
#     for string in strings:
#         #string = abc
#         new.append(string[i])
#     print ("".join(new))

# '''Their solution'''

# for i in range(len(strings[0])):
#     line = ""
#     for string in strings:
#         line += string[i]
#     print(line)


'''
For example, if
strings = ["abcqwe", "def", "ghiq"]
your program should print :
adg
beh
cfi
q q
w
e
'''

# strings = ["abcqwe", "def", "ghiq"]

# max_lengh = max(len(s) for s in strings)

# for i in range(max_lengh):
#     line = []
#     for string in strings:
#         line.append(string[i] if i < len(string) else " ")
#     print ("".join(line))
        

# __________________________________________________________________________
# __________________________________________________________________________

   
# def surround(x, y):
#     a = y + x + y
#     return a
    
# def alert(string, level):
#     string = surround(string, " ")
#     for i in range(level):
#         string = surround(string, "!")
#     return string
 

# assert_equal(alert("Warning", 2), "!! Warning !!")
# assert_equal(alert("DANGER", 4), "!!!! DANGER !!!!")


# __________________________________________________________________________
# __________________________________________________________________________


def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")

# ''' My solution '''

# import snoop


# @snoop(depth=1)
# def diagonal_winner(board):
#     line1 = []
#     for index_line in board:
#         for line in index_line:
#             if line:
#                     line1.append(line)
#     return line1[0] == line1 [4] == line1[8] or line1[2] == line1 [4] == line1[6]  


# def diagonal_winner(board):
#      middle = board[1][1]
#      return (
#           (middle == board[0][0] and middle == board[2][2]) or
#           (middle == board[0][2] and middle == board[2][0])
#      )
            
            

# def all_equal(board):
#     return row[0] == row[1] == row[2]

# assert_equal(
#     diagonal_winner(
#         [
#             ['X', 'O', 'X'],
#             ['X', 'X', 'O'],
#             ['O', 'O', 'X']
#         ]
#     ),
#     True
# )

# assert_equal(
#     diagonal_winner(
#         [
#             ['X', 'X', 'O'],
#             ['X', 'O', 'O'],
#             ['O', 'X', 'X']
#         ]
#     ),
#     True
# )

# assert_equal(
#     diagonal_winner(
#         [
#             ['O', 'X', 'O'],
#             ['X', 'X', 'X'],
#             ['O', 'O', 'X']
#         ]
#     ),
#     False
# )

# __________________________________________________________________________

# __________________________________________________________________________

# def invalid_image(filename):
#     return not (filename.endswith(".png") or filename.endswith(".jpg"))

# assert_equal(invalid_image("dog.png"), False)
# assert_equal(invalid_image("cat.jpg"), False)
# assert_equal(invalid_image("invoice.pdf"), True)


# __________________________________________________________________________
'''Tic - Tac - Toe'''
# __________________________________________________________________________

import snoop

# def row_winner(board): 
    # for line in board:
    #     if not " " in line:
    #         making_line = [line[0] * len(board[0])]
    #         new = [char for char in making_line[0]]
    #         print (new)
    #         if line == new:
    #             return True
    # return False  

# @snoop
# def column_winner(board):
#     k = 0
#     for _ in range(len(board[0])):
#         new_column = []
#         for j in range(len(board)):
#             new_column.append(board[j][k])
#         if not " " in new_column:
#             verify = [new_column[0] * len(new_column)]
#             new_verify = [char for char in verify[0]]
#             if new_verify == new_column:
#                 return True
#         print(new_column)
#         k += 1
#     return False 

# @snoop
# def diagonal_winner(board):
#     k = 0
#     j =  0
#     m = -1
#     diag = []
#     diag2 = []
#     while k < len(board):
#             diag.append(board[j][k])
#             diag2.append(board[j][m])
#             k += 1
#             j += 1
#             m -= 1
#     if not " " in diag:
#         verify = [diag[0] * len(diag)]
#         new_verify = [char for char in verify[0]]
#         if new_verify == diag:
#             return True
#     if not " " in diag2:
#         verify = [diag2[0] * len(diag2)]
#         new_verify = [char for char in verify[0]]
#         if new_verify == diag2:
#             return True

#     print(diag, diag2)
        
#     return False 

# assert_equal(
#     diagonal_winner(
#         [
#             ['O', 'X', 'O', 'X'],
#             [' ', 'O', 'X', ' '],
#             ['X', 'X', ' ', 'X'],
#             ['X', ' ', 'O', 'O']
#         ]
#     ),
#     True
# )
# assert_equal(
#     diagonal_winner(
#         [
#             ['X', 'X', ' '],
#             ['X', ' ', 'O'],
#             [' ', 'O', 'O']
#         ]
#     ),
#     False
# )

# assert_equal(
#     row_winner(
#         [
#             ['A', 'A', 'B', 'A'],
#             [' ', ' ', ' ', ' '],
#             ['A', ' ', ' ', 'A'],
#             ['B', ' ', 'B', 'A']
#         ]
#     ),
#     False
# )
# assert_equal(
#     row_winner(
#         [
#             ['X', ' ', 'X'],
#             ['O', 'X', 'X'],
#             ['O', 'O', 'O']
#         ]
#     ),
#     True
# )

# assert_equal(
#     column_winner(
#         [
#             ['X', 'O', ' '],
#             ['X', 'O', ' '],
#             ['0', 'X', ' ']
#         ]
#     ),
#     False
# )
# assert_equal(
#     column_winner(
#         [
#             ['X', 'O', ' ', 'X'],
#             [' ', 'O', 'X', 'O'],
#             ['O', 'O', 'X', 'X'],
#             ['O', 'O', 'X', ' ']
#         ]
#     ),
#     True
# )



# '''Their version'''

# def winner(board):
#     if row_winner(board) or column_winner(board) or diagonal_winner(board):
#         return True
#     else:
#         return False 

# def winning_line(strings):
#     piece = strings[0]
#     if piece == ' ':
#         return False
#     for entry in strings:
#         if piece != entry:
#             return False
#     return True

# def row_winner(board):
#     for row in board:
#         if winning_line(row):
#             return True
#     return False

# def column_winner(board):
#     for col in range(len(board[0])):
#         column = []
#         for row in board:
#             column.append(row[col])
#         if winning_line(column):
#             return True
#     return False

# def diagonal_winner(board):
#     diagonal1 = []
#     diagonal2 = []
#     for i in range(len(board)):
#         diagonal1.append(board[i][i])
#         diagonal2.append(board[i][-i-1])
#     return winning_line(diagonal1) or winning_line(diagonal2)

# assert_equal(
#     winner(
#         [
#             ['X', 'X', 'X', ' '],
#             ['X', 'X', ' ', ' '],
#             ['X', ' ', 'O', 'X'],
#             [' ', ' ', 'O', 'X']
#         ]
#     ),
#     False
# )
# assert_equal(
#     winner(
#         [
#             ['X', ' ', 'X'],
#             ['O', 'X', 'O'],
#             ['O', 'O', 'O']
#         ]
#     ),
#     True
# )
# assert_equal(
#     winner(
#         [
#             ['X', ' '],
#             ['X', 'O']
#         ]
#     ),
#     True
# )



# def format_board(board):
#     joined_rows = []
#     for row in board:
#         joined_rows.append("".join(row))
#     return "\n".join(joined_rows)

# def format_board(board):
#     new = []
#     for line in board:
#         r = "|".join(line)
#         new.append(r)
#     the_line = ["-" for i in range(len(line))]
#     new_line = "+".join(the_line)
#     print (new_line)
#     new2 = ("\n"+ new_line + "\n").join(new)
#     print (new2)
#     return new2

# assert_equal(
#     format_board([
#         ['X', 'O', 'X'],
#         ['O', ' ', ' '],
#         [' ', 'X', 'O']
#     ]),
#     'X|O|X\n-+-+-\nO| | \n-+-+-\n |X|O'
# )



# def format_board(board):
#     lengh =" "
#     for i in range(len(board)):
#         lengh += str(i+1)
#     print(lengh)
#     new = []
#     for line in board:
#         new.append("".join(line))
#     k = 0
#     for line2 in new:
#         another_new = str(k+1) + line2
#         new[k] = another_new
#         k += 1
#     new2 = "\n".join(new)
#     final = lengh + "\n" + new2
#     print(final)

''' or '''
# @snoop
# def format_board(board):
#     lengh =" "
#     for i in range(len(board)):
#         lengh += str(i+1)
#     joined_rows = [lengh]
#     for i in range(len(board)):
#         joined_row = str(i+1) + "".join(board[i])
#         joined_rows.append(joined_row)
#     return print("\n".join(joined_rows))



# assert_equal(
#     format_board([
#         ['X', 'O', 'X'],
#         ['O', ' ', ' '],
#         [' ', 'X', 'O']
#     ]),
#     ' 123\n1XOX\n2O  \n3 XO'
# )


'''
iterate dict : 
for k,v in d.item() --> (k,v)
    d.keys()
    d.values()

sort dict by value:
print(sorted(x.items(),key = lambda y:y[1]))


'''

# def format_board(board):
#     first_row = ' '
#     for i in range(len(board)):
#         first_row += str(i + 1)
#     joined_rows = [first_row]
#     for i in range(len(board)):
#         joined_row = str(i + 1) + ''.join(board[i])
#         joined_rows.append(joined_row)
#     return "\n".join(joined_rows)

# def play_game():
#     board = [
#         [' ', ' ', ' '],
#         [' ', ' ', ' '],
#         [' ', ' ', ' '],
#     ]
#     print(format_board(board))
#     print('\nX to play:\n')
#     play_move(board, 'X')
#     print(format_board(board))
#     print('\nO to play:\n')
#     play_move(board, 'O')
#     print(format_board(board))

# def play_move(board, player):
#     number_row = input("Row :")
#     number_column = input("Column :")
#     board[int(number_row) -1][int(number_column) -1] = player

# play_game()

# --------------------------------------------------


# --------------------------------------------------

# # @snoop
# def make_board(size):
#     board = []
#     for _ in range(size):
#         row = []
#         for _ in range(size):
#             row.append(' ')
#         board.append(row)
#     return board

# # @snoop
# def test():
#     board = make_board(3)
#     print(board)
#     assert_equal(board, [
#         [' ', ' ', ' '],
#         [' ', ' ', ' '],
#         [' ', ' ', ' '],
#     ])
#     board[0][0] = 'X'
#     assert_equal(board, [
#         ['X', ' ', ' '],
#         [' ', ' ', ' '],
#         [' ', ' ', ' '],
#     ])


# test()

# --------------------------------------------------


# --------------------------------------------------


'''Here each element of cube is a separate list, a copy of board. And within each of those copies, each element is also a separate list, a copy of row. But the shallow copies of board all have the same first element as each other (the first copy of row), the same second element, and so on. Changing make_board won't fix anything here, the solution is to either:

Call make_board repeatedly to make a new board each time, or
Use the deepcopy function instead of board.copy(). deepcopy makes copies at every level of nested objects.'''
# def make_board(size):
#     row = []
#     for _ in range(size):
#         row.append(' ')
#     board = []
#     for _ in range(size):
#         board.append(row.copy())
#     return board

# def make_cube(size):
#     cube = []
#     board = make_board(size)
#     for _ in range(size):
#         cube.append(board.copy())
#     return cube

# def test():
#     cube = make_cube(2)
#     print(cube)
#     cube[0][0][0] = 'X'
#     print(cube)
#     print(cube[0] is cube[1])
#     print(cube[0][0] is cube[0][1])
#     print(cube[0][0] is cube[1][0])

# test()

# --------------------------------------------------


# -------------------------------------------------

# '''The full game'''

# def winning_line(strings):
#     strings = set(strings)
#     return len(strings) == 1 and ' ' not in strings

# def row_winner(board):
#     return any(winning_line(row) for row in board)

# def column_winner(board):
#     return row_winner(zip(*board))

# def main_diagonal_winner(board):
#     return winning_line(row[i] for i, row in enumerate(board))

# def diagonal_winner(board):
#     return main_diagonal_winner(board) or main_diagonal_winner(reversed(board))

# def winner(board):
#     return row_winner(board) or column_winner(board) or diagonal_winner(board)

# def format_board(board):
#     size = len(board)
#     line = f'\n  {"+".join("-" * size)}\n'
#     rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
#     return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'

# def play_move(board, player):
#     print(f'{player} to play:')
#     row = int(input()) - 1
#     col = int(input()) - 1
#     board[row][col] = player
#     print(format_board(board))

# def make_board(size):
#     return [[' '] * size for _ in range(size)]

# def print_winner(player):
#     print(f'{player} wins!')

# def print_draw():
#     print("It's a draw!")

# @snoop
# def play_game(board_size, player1, player2):
#     board = make_board(board_size)
#     print(format_board(board))
#     num = board_size * board_size
#     k = 0
#     while k < num:
#         play_move(board, player1)
#         k += 1
#         if row_winner(board) or diagonal_winner(board) or column_winner(board):
#             return print_winner(player1)
#         if k == num:
#             return print_draw()
#         play_move(board, player2)
#         if row_winner(board) or diagonal_winner(board) or column_winner(board):
#             return print_winner(player2)
#         k += 1
#     return print_draw()

        

# play_game(3, 'X', 'O')

'''
xx0
00x
xx0

'''

# '''Their solution'''
# def play_game(board_size, player1, player2):
#     board = make_board(board_size)
#     print(format_board(board))

#     player = player1
#     for _ in range (board_size * board_size):
#         if winner(board):
#             print_winner(player)
#             return
#         if player == player1:
#             player = player2
#         else:
#             player = player1
#     print_draw()


# --------------------------------------------------


# -------------------------------------------------

# @snoop
# def substitute(string, d):
#     result = ''
#     for char in string:
#         char = d[char]
#         result += char
#     return result

# original = 'AGTAGCGTCCTTAGTTACAGGATGGCTTAT'
# expected = 'TCATCGCAGGAATCAATGTCCTACCGAATA'
# assert_equal(substitute(original, {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}), expected)

# --------------------------------------------------


# -------------------------------------------------

@snoop
def print_words(words):
    for word in words:
        translations = words[word]

        print(f"English: {word}")
        for language in translations:
            print(f"{language}: {translations[language]}")
        print(f"---")

print_words({
    'apple': {
        'French': 'pomme',
        'German': 'apfel',
    },
    'box': {
        'French': 'boite',
        'German': 'kasten',
    },
})














