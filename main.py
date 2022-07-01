from flask import *
app = Flask(__name__)

from data_factory import DataUtilFactory

dataUtilFactory = DataUtilFactory()
dataUtil = dataUtilFactory.create()

@app.route('/')
def cari():
    query = request.args.get('query')
    data = dataUtil.getGame(query)
    return render_template('cari.html', data=data, query=query, datacount=len(data))

@app.route('/gambar_game/<filename>')
def gambar_game(filename):
	return send_file('./static/assets/images/'+filename, attachment_filename=filename)

app.run(debug = True, threaded=True)
