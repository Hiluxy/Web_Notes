#package: requests, jsonify

@app.route('/test', methods=['GET'])
def test_get():
title_receive = request.args.get('키')
print(title_receive)
return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['키']
    print(title_receive)
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
