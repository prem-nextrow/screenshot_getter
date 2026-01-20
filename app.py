from flask import Flask, request, jsonify, render_template, send_from_directory
from crawler.crawler_service import run_crawler
import os

app = Flask(__name__)

@app.route('/cdn/<path:filepath>')
def serve_static_assets(filepath):
    return send_from_directory('output', filepath)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/crawl", methods=["POST"])
def crawl():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400
        
    result = run_crawler(url)
    
    base_cdn = request.host_url + "cdn"
    
    return jsonify({
        "status": "done",
        "pdf_list": [
            {"name": p["name"], "url": f"{base_cdn}/{p['src']}"} 
            for p in result['pdfs']
        ],
        "media_files": [
            {"type": m["type"], "url": f"{base_cdn}/{m['src']}"} 
            for m in result['media']
        ]
    })

if __name__ == "__main__":
    app.run(port=3030, debug=True)