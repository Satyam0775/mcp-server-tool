from flask import Flask, request, jsonify
import os

# Step 1: Create the Flask app
app = Flask(__name__)

# Step 2: Define a route (like an endpoint)
@app.route('/search', methods=['POST'])
def search_keyword():
    # Step 3: Get the input from user (JSON)
    data = request.get_json()
    keyword = data.get("keyword")
    file_path = data.get("file_path")

    # Step 4: Basic validation
    if not keyword or not file_path:
        return jsonify({"error": "Please provide both keyword and file_path"}), 400

    # Step 5: Check if file exists
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    # Step 6: Search keyword line by line
    matches = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_no, line in enumerate(f, start=1):
            if keyword.lower() in line.lower():
                matches.append({"line_number": line_no, "text": line.strip()})

    # Step 7: Return the result as JSON
    return jsonify({
        "keyword": keyword,
        "matches": matches
    })

# Step 8: Run the server
if __name__ == '__main__':
    app.run(debug=True)
