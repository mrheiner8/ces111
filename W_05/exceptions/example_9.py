"""
PermissionError
Nearly all computer operating systems, such as Microsoft Windows, Mac OS X, and Linux, allow multiple people to use a single computer. Because people need to store private data in files on a computer, the operating systems implement file access permission rules. These rules help to prevent unauthorized access to files.

If we write a call to the open function that attempts to open a file and the person executing our program doesn`t have permission to access the file, the computer will raise a PermissionError. Example 9 contains code where such an error might occur.
"""
# Example 9
def main():
  try:
    with open("contacts.csv", "rt") as contacts_file:
        for row in contacts_file:
            print(row)
  except PermissionError as perm_err:
    print(perm_err)
if __name__ == "__main__":
  main()
"""
> python permission_error.py
[Errno 13] Permission denied: 'contacts.csv'
"""