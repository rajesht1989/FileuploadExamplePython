from flask import Flask, request
import pandas as pd
import time
app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    # Get the file from the request.
    file = request.files["file"]

    # Save the file to the filesystem.
    with open("uploads/" + file.filename, "wb") as f:
        f.write(file.read())


    df = pd.read_csv("uploads/" + file.filename)
    # df.drop("STATISTIC", axis=1, inplace=True)
    # df.insert(0, "name", "Vishnu")
    time.sleep(5)
    return df.to_json()

if __name__ == "__main__":
    app.run(port=5001, debug=True)