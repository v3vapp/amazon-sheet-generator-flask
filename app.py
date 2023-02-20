from flask import Flask, request, render_template, request, jsonify, make_response, send_file
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
            try:
                sheet = AmazonCheckSheet(file1, file2)

                filename = sheet.generate()

                response = make_response(jsonify({"filename": f"./static/{filename}"}))

            except Exception as e:

                response = make_response(jsonify({"error":f"Wrong files has uploaded... error -> {e}"}))
            
        return response

    return render_template("index.html")


# -----------------------------------------------------------------------------------------------

@app.route('/download')
def download():
    path = 'static/AmazonCheckSheet.csv'
    return send_file(path, as_attachment=True)

# -----------------------------------------------------------------------------------------------

@app.route('/clear')
def download():
    
    path = 'static/AmazonCheckSheet.csv'

    return send_file(path, as_attachment=True)

#--------------------------------------------------------------------------
if __name__ == "__main__":

    app.run()
