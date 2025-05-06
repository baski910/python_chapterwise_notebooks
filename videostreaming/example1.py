import os
import re
from pathlib import Path

from flask import Flask, render_template, Response, request
from werkzeug.routing import BaseConverter

app = Flask(__name__)

FILE_TEMPLATE = '''
<a href="/{video_file}">{video_file}</a>
'''
BASE_DIR = Path('.')
CHUNK_SIZE = 2 ** 25


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def index():
    #return '<br>'.join([
    #    FILE_TEMPLATE.format(video_file=file.name).strip()
    #    for file in list(BASE_DIR.glob('*.mkv')) + list(BASE_DIR.glob('*.mp4'))
    #])
    return render_template('index.html')


@app.after_request
def after_request(response):
    response.headers.add('Accept-Ranges', 'bytes')
    return response


def get_chunk(full_path, byte1=None, byte2=None):
    if not os.path.isfile(full_path):
        raise OSError('no such file: {}'.format(full_path))

    file_size = os.stat(full_path).st_size
    start = 0
    if byte1 < file_size:
        start = byte1

    length = file_size - start
    if byte2:
        length = byte2 + 1 - byte1

    if length > CHUNK_SIZE:
        length = CHUNK_SIZE

    with open(full_path, 'rb') as f:
        f.seek(start)
        chunk = f.read(length)
    return chunk, start, length, file_size


def get_byte_interval(request):
    range_header = request.headers.get('Range', None)
    byte1, byte2 = 0, None
    if range_header:
        match = re.search(r'(\d+)-(\d*)', range_header)
        groups = match.groups()

        if groups[0]:
            byte1 = int(groups[0])
        if groups[1]:
            byte2 = int(groups[1])

    return byte1, byte2


#@app.route('/<regex(".*\.mp4"):video_file>')
@app.route('/video_feed')
def video_feed():
#def get_file_mp4(video_file):
    byte1, byte2 = get_byte_interval(request)

    chunk, start, length, file_size = get_chunk(
        "SampleVideo.mp4",
        byte1, byte2)
    resp = Response(chunk, 206, mimetype='video/mp4',
                    content_type='video/mp4', direct_passthrough=True)
    resp.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(start, start + length - 1, file_size))
    return resp


if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description='Process some integers.')

    #parser.add_argument(
    #    '-d', '--dir', type=str, default='.', help='directory with videos')

    #args = parser.parse_args()
    #BASE_DIR = Path(args.dir)
    app.run(host='0.0.0.0', threaded=True, debug=True)
