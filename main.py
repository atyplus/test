from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Products route
@app.route("/products")
def products():
    return render_template("products.html")

# Contact route
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        # Handle form submission (e.g., save to a database or send email)
        return redirect("/")
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)