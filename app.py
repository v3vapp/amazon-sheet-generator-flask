from flask import Flask, request, render_template, request, jsonify, make_response
import csv
from converter import AmazonCheckSheet

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        file1 = request.files["file1"]
        file2 = request.files["file2"]

        if not file1 or not file2:
            return "No file uploaded"

        # file_contents = file.read().decode("utf-8")
        # rows = list(csv.reader(file_contents.splitlines()))
        else:

            sheet = AmazonCheckSheet(file1, file2)
            filename = sheet.generate()

            response = make_response(jsonify({"filename": f"./static/{filename}"}))
            
        return response

    return render_template("index.html")

if __name__ == "__main__":

    app.run()
