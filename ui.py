import os

def read_and_validate_filename(folder=""):
  filename_from_user = input("PDF file name to join (type '_end_' to stop asking): ")

  if filename_from_user.strip().lower()=="_end_":
      return False, "_end_"

  if not filename_from_user.lower().endswith('.pdf'):
      filename_from_user+='.pdf'

  filepath = os.path.join(folder, filename_from_user)
  #print(f"File search -> {filepath}")
  if os.path.isfile(filepath):
      return True, filepath
  else:
      return False, None


def get_source_pdfs(folder):
    pdfs_to_join = []
    while (True):
        found, current_pdf = read_and_validate_filename(folder)
        if (current_pdf=="_end_"):
            break

        if found:
            print(f"INFO: File OK\n")
            pdfs_to_join.append(current_pdf)
        else:
            print(f"ERROR: Cannot find this file\n")
    return pdfs_to_join

def get_thick_pdf_name(folder=""):
  filename_from_user = ""
  while filename_from_user=="":
    filename_from_user = input("Name for the new PDF: ")
    
  if not filename_from_user.lower().endswith('.pdf'):
      filename_from_user+='.pdf'

  filepath = os.path.join(folder, filename_from_user)
  print(f"File to be created: {filepath}")
  return filepath

def get_folder_name():
  folder_name = ""
  while folder_name=="":
    folder_name = input("Folder to work at: ")
    if not os.path.isdir(folder_name):
        print(f"{folder_name} is not valid (must already exist)")
        folder_name=""
      
  return folder_name

    

def banner(v):
    print("*****************************************************")
    print("****                PDF JOINER                   ****")
    print("*****************************************************")
    print()
    print(f"Version: {v}")
    print()