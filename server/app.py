from flask import Flask
from routes.analyze import analyze_code, analyze_file  # Import your routes

app = Flask(__name__)

# Register the routes
app.add_url_rule('/analyze', view_func=analyze_code, methods=['POST'])
app.add_url_rule('/analyze-file', view_func=analyze_file, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
