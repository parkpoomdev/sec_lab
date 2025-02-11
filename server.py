from flask import Flask, request, render_template_string
import logging
import threading

app = Flask(__name__)

# Configure logging to track form submissions
logging.basicConfig(filename='flask_submission.log', level=logging.INFO, format='%(asctime)s - %(message)s')

HTML_FORM = """
   <!DOCTYPE html>
   <html>
   <head>
       <title>Form Submission</title>
   </head>
   <body>
       <h2>Submit Your Details</h2>
       <form method="post">
           Name: <input type="text" name="name" required><br><br>
           Email: <input type="email" name="email" required><br><br>
           <input type="submit" value="Submit">
       </form>
       
       {% if name and email %}
       <h3>Submitted Data:</h3>
       <p><strong>Name:</strong> {{ name }}</p>
       <p><strong>Email:</strong> {{ email }}</p>
       {% endif %}
   </body>
   </html>
   """

@app.route('/', methods=['GET', 'POST'])
def index():
    name = email = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Log the submitted data
        app.logger.info(f"Form Submitted: Name={name}, Email={email}")

    return render_template_string(HTML_FORM, name=name, email=email)

def run_http():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

def run_https():
    app.run(host='0.0.0.0', port=5001, ssl_context=('cert.pem', 'key.pem'), debug=False, use_reloader=False)

if __name__ == '__main__':
    threading.Thread(target=run_http, daemon=True).start()
    run_https()
