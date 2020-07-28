from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'test'
@app.route('/home/<string:name>' , methods=['POST','GET'])
def home(name):
    return '<h1> hello {}, you are on the home page!'</h1>' .format(username)
    
@app.route('/json')
def json():
    return jsonify({'key' : 'value', 'listkey' : [1,2,3]})

@app.route('/query')
def query():
    username = request.args.get('username')
    password = request.args.get('password')
    return <h1> Hi {} . you are from {}. you are on the query page </h1> .format(username,password)
    
@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process" >
                <input type="text" name="username" pattern="[a-z]{1-15}">
                <input type="text" name= "password">
                <input type="submit" value="submit">
               </form>'''
               
@app.route('/login' , methods=['POST'])
def process():
    if(request.form['username'] == 'vaibhav') && (request.form['password']== 'abcd12')
        return jsonify({'status' : '200' , 'msg' : 'success'})
    else if(request.form['username'] == 'vaibhav') && (request.form['password']== 'abcd')
        return jsonify({'status' : '201' , 'msg' : 'failure:password should be of length 6'})
    else if(request.form['username'] == 'vaibhav') && (request.form['password']== 'abcdef')
        return jsonify({'status' : '202' , 'msg' : 'Failure:password to have 1 character and 1 number'})
    else if(request.form['username'] == '1234') && (request.form['password']== 'abcd12')
        return jsonify({'status' : '203' , 'msg' : 'Failure: only character allowed in username'})
    else    
        return 0
    if __name__ == '__main__':
    app.run(debug=True)