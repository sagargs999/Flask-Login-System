from flask import Flask, request, redirect, url_for, session, Response
app = Flask(__name__)
app.secret_key = "supersecret"
@app.route("/", methods =["GET", "POST"])
def login():
    if request.method =="POST":
        user = request.form.get("Username")
        password = request.form.get("Password")
        if user == "admin" and password == "123":
            session["user"] = user
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials, Try again", mimetype = "text/plain")
    return '''
<h2>Login Page</h2>
<form method = "POST">
username:<input type = "text" name = "Username"><br>
password:<input type = "password" name = "Password"><br>
<input type = "submit" value = "Login">
</form>
'''
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session['user']}!</h2>
        <a href="{url_for('logout')}">Logout</a>
        '''
    return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)