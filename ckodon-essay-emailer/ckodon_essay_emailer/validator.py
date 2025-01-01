"""Extract email addresses from documents for validation."""
from os import listdir, rename
import docx2txt
import re


for filename in listdir("../data/essays/"):
    # define path to each activities document
    doc_path = "../data/essays/" + filename

    try:
        # extract all text from word document at path
        search_string = docx2txt.process(doc_path)

        # search for email in text
        pattern = "[A-Za-z0-9.+\-_]+@[A-Za-z0-9.+\-_]+\.[A-Za-z]{2,}"  # regular expression for email
        matches = re.search(pattern, search_string)
        email_address = matches.group(0)
        print(email_address, doc_path)

    except Exception as exception:
        rename(doc_path, f"../data/exceptions/{filename}")
        print(f"Moved file {filename}")
