#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for

import requests


app = Flask(__name__)


@app.route('/chucknorris', methods=['GET'])
def get_chuck_norris_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        joke = response.json()['value']
        print(joke)
        letter_count = {}
        for letter in joke:
            if letter.lower() in letter_count:
                letter_count[letter.lower()] += 1
            else:
                letter_count[letter.lower()] = 1
        return jsonify({'joke': joke, 'letter_count': letter_count})
    else:
        message = "Status Code: " + response.status_code
        return jsonify({'error_message':message})


if __name__ == '__main__':
    app.run(debug=True)

