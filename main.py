from ui import get_folder_name, get_thick_pdf_name, banner, get_source_pdfs, ask_for_all_in_folder
from merger import check_and_build as join_pdfs

VERSION = "2.0.0"

banner(VERSION)

folder = get_folder_name()
confirmation, pdfs_to_join = ask_for_all_in_folder(folder)

if confirmation=="no":
  pdfs_to_join = get_source_pdfs(folder)


print(f"DEBUG {pdfs_to_join}")

dest_file = get_thick_pdf_name(folder)
join_pdfs(pdfs_to_join, dest_file)
