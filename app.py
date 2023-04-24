from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from oortwrapper import OortWrapper
from flask_dropzone import Dropzone

app = Flask(__name__)
app.config.update(
    DROPZONE_ALLOWED_FILE_TYPE='default',
    DROPZONE_MAX_FILE_SIZE=10,
    DROPZONE_MAX_FILES=30,
    DROPZONE_REDIRECT_VIEW='results',
)

dropzone = Dropzone(app)
oort = OortWrapper()

@app.route('/')
def index():
    buckets = oort.list_buckets()
    return render_template('index.html', buckets=buckets)

@app.route('/bucket/<bucket_name>')
def view_bucket(bucket_name):
    objects = oort.list_objects(bucket_name)
    return render_template('bucket.html', bucket_name=bucket_name, objects=objects)

@app.route('/create_bucket', methods=['POST'])
def create_bucket():
    bucket_name = request.form.get('bucket_name')
    if bucket_name:
        oort.create_bucket(bucket_name)
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    selected_bucket = request.form.get('bucket')
    for key in request.files:
        file = request.files.get(key)
        if selected_bucket and file:
            file_name = file.filename
            file_data = file.read()
            oort.put_object(selected_bucket, file_name, file_data)
    return redirect(url_for('view_bucket', bucket_name=selected_bucket))

@app.route('/download/<bucket_name>/<path:file_name>')
def download(bucket_name, file_name):
    obj = oort.get_object(bucket_name, file_name)
    return send_from_directory(obj['Body'], file_name, as_attachment=True)

@app.route('/delete_bucket/<bucket_name>')
def delete_bucket(bucket_name):
    oort.delete_bucket(bucket_name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8888)
