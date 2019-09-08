from flask              import Flask, request, render_template
from layer_business     import create_user, get_all_users, get_user_or_none


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World !"


@app.route('/register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'GET':
        return render_template('register.html')
    
    # POST
    # form data
    name = request.form.get('name') or ""
    username = request.form.get('username') or ""
    email = request.form.get('email') or ""
    password = request.form.get('password') or ""

    # create user
    is_created = create_user(name=name, username=username, 
                             email=email, password=password)

    if is_created:
        return "Successfull !"
    
    return "Error ! Please try again..."

@app.route('/users', methods=['GET'])
def get_users():

    all_users = get_all_users()

    return render_template('users.html', all_users=all_users)


@app.route('/users/<username>', methods=['GET'])
def get_user_by_username(username):

    user = get_user_or_none(username)

    if user:
        return render_template('single_user.html', user=user)
    
    return "Not found :(", 404


if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)
