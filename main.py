from ui import get_folder_name, get_thick_pdf_name, banner, get_source_pdfs
from merger import check_and_build as join_pdfs

VERSION = "0.2"

banner(VERSION)
folder = get_folder_name()
pdfs_to_join = get_source_pdfs(folder)
dest_file = get_thick_pdf_name(folder)
join_pdfs(pdfs_to_join, dest_file)