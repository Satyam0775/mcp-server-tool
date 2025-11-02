# MCP Server Tool

This is a simple MCP (Model Context Protocol) server built using Flask.
It searches for a given keyword in a text file and returns all lines that contain that keyword.

## How to Run
1. Install Flask  
pip install flask

2. Run the server  
python server.py

cpp
Copy code
3. Test the endpoint (using Postman or curl):  
POST http://127.0.0.1:5000/search

css

**Body (JSON):**
```json
{
  "keyword": "Satyam",
  "file_path": "sample.txt"
}
Output Example:

json
Copy code
{
  "keyword": "Satyam",
  "matches": [
    {
      "line_number": 3,
      "text": "This assignment belongs to Satyam Kumar."
    }
  ]
}


---

### 🪜 Steps to Create It in VS Code

1. **Open VS Code** → Click **File → Open Folder** → select a location (like Desktop).  
2. **Create Folder:**  
   - Name it `MCP_Server`  
3. **Inside it:**  
   - Right-click → **New File** → `server.py`  
   - Right-click → **New File** → `sample.txt`  
   - (optional) Right-click → **New File** → `README.md`
4. **Copy and paste** the above content into each file.  
5. **Open Terminal in VS Code** → type:
pip install flask



6. Then run:
python server.py
Copy code
7. You’ll see:
Running on http://127.0.0.1:5000
