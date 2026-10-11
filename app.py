# NowPageGen - Minimal /now page generator
# Author: Mourad.Soltani
# Signature: Mourad.Soltani

from flask import Flask, render_template, request, jsonify, make_response
import html

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "ok", "service": "nowpage-gen", "author": "Mourad.Soltani"}), 200

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form
    name = html.escape(data.get('name', 'Anonymous'))
    working_on = html.escape(data.get('working_on', ''))
    reading = html.escape(data.get('reading', ''))
    exploring = html.escape(data.get('exploring', ''))
    note = html.escape(data.get('note', ''))

    html_content = render_template(
        'now_page.html',
        name=name,
        working_on=working_on,
        reading=reading,
        exploring=exploring,
        note=note
    )
    return html_content

@app.route('/download', methods=['POST'])
def download():
    data = request.form
    name = html.escape(data.get('name', 'Anonymous'))
    working_on = html.escape(data.get('working_on', ''))
    reading = html.escape(data.get('reading', ''))
    exploring = html.escape(data.get('exploring', ''))
    note = html.escape(data.get('note', ''))

    html_content = render_template(
        'now_page.html',
        name=name,
        working_on=working_on,
        reading=reading,
        exploring=exploring,
        note=note
    )
    response = make_response(html_content)
    response.headers['Content-Disposition'] = 'attachment; filename=now.html'
    response.headers['Content-Type'] = 'text/html'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
