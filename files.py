
from flask import Flask, request, send_file
import os
import zipfile
import datetime


app = Flask(__name__)


@app.route("/outputs", methods=["GET"])
def files():
    ts = int(datetime.datetime.now().timestamp())
    fn = "outputs-" + str(ts) + ".zip"
    zf = zipfile.ZipFile(fn, "w")
    for dirname, subdirs, files in os.walk("outputs"):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()

    return send_file(fn, as_attachment=True)


@app.route("/removeDup", methods=["GET"])
def files():
    ts = int(datetime.datetime.now().timestamp())
    fn = "removeDup-" + str(ts) + ".zip"
    zf = zipfile.ZipFile(fn, "w")
    for dirname, subdirs, files in os.walk("removeDup"):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()

    return send_file(fn, as_attachment=True)


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8585)
