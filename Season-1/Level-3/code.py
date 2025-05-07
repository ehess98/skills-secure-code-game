# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def source():
    user_input = request.args.get("input", "")  # Prevent KeyError
    taxpayer = TaxPayer('foo', 'bar')
    taxpayer.get_tax_form_attachment(user_input)
    taxpayer.get_prof_picture(user_input)

class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # Returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        if not path:
            return None  # Return None safely

        # Validate path to prevent traversal attacks
        base_dir = os.path.abspath(os.path.dirname(__file__))
        prof_picture_path = os.path.abspath(os.path.join(base_dir, path))

        if not prof_picture_path.startswith(base_dir):  # Ensures file is within allowed dir
            return None

        if not os.path.exists(prof_picture_path):  # Check if the file exists
            return None
        
        with open(prof_picture_path, 'rb') as pic:
            picture = bytearray(pic.read())

        return prof_picture_path

    # Returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        if not path:
            raise Exception("Error: Tax form is required for all users")

        # Validate path
        base_dir = os.path.abspath(os.path.dirname(__file__))
        tax_form_path = os.path.abspath(os.path.join(base_dir, path))

        if not tax_form_path.startswith(base_dir):  # Prevents traversal attacks
            raise Exception("Invalid file path")

        if not os.path.exists(tax_form_path):  # Check if the file exists before opening
            raise Exception("File does not exist")

        with open(tax_form_path, 'rb') as form:
            tax_data = bytearray(form.read())

        return tax_form_path