from PyPDF2 import PdfFileMerger

def join_pdfs(pdfs, dest_name):
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)

    output = open(dest_name, "wb")
    merger.write(output)    

def check_and_build(pdfs, dest_name):
  if len(pdfs)>1:
    print(f"Files to join: {', '.join(pdfs)}\n")
    print(f"Process starting...")
    try:
        join_pdfs(pdfs, dest_name)
        print(f"INFO: successfully merged {dest_name}")
        return True
    except Exception as e:
        print(f"ERROR: issue raised while processing files\n{e}")
        return False
  else:
    print("WARNING: Not enough files to join (more than 1 file is needed), try again.")      