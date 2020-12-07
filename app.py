from flask import Flask, render_template, redirect, request, jsonify
from flask_awscognito import AWSCognitoAuthentication
from flask_bootstrap import Bootstrap

app = Flask(__name__)

#us-east-1_Nv4RJ2l6M

app.config['AWS_DEFAULT_REGION'] = 'us-east-1'
app.config['AWS_COGNITO_DOMAIN'] = 'diabetically.auth.us-east-1.amazoncognito.com'
app.config['AWS_COGNITO_USER_POOL_ID'] = 'us-east-1_Nv4RJ2l6M'
app.config['AWS_COGNITO_USER_POOL_CLIENT_ID'] = 'YYY'
app.config['AWS_COGNITO_USER_POOL_CLIENT_SECRET'] = 'ZZZZ'
app.config['AWS_COGNITO_REDIRECT_URL'] = 'https://9336823629244578a28349294cad43a4.vfs.cloud9.us-east-1.amazonaws.com/'

Bootstrap(app)
aws_auth = AWSCognitoAuthentication(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
    
@app.route('/')
def index():
    return render_template('index.html')


#@app.route('/')
#@aws_auth.authentication_required
#def index():
#    claims = aws_auth.claims
#    return jsonify({'claims': claims})
#   # return render_template('index.html')
   
#@app.route('/aws_cognito_redirect')
#def aws_cognito_redirect():
#    access_token = aws_auth.get_access_token(request.args)
#    return jsonify({'access_token': access_token})
    
#@app.route('/sign_in')
#def sign_in():
#    return redirect(aws_auth.get_sign_in_url())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)