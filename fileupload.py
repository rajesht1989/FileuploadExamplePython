from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    # Get the file from the request.
    file = request.files["file"]

    # Save the file to the filesystem.
    with open("uploads/" + file.filename, "wb") as f:
        f.write(file.read())

    return "File uploaded successfully!"

if __name__ == "__main__":
    app.run(port=5001, debug=True)