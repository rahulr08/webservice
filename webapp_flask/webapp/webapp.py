from flask import Flask
from flask import request
import itertools

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def word_list_anagram(word):
  try:
    perms = [''.join(perm) for perm in itertools.permutations(word)]
  except Exception, a:
    print ("Exception follows as ->"+a)
  finally:
    return  perms


@app.route('/anagram/')
def word_list():
  word = request.args.get('word')
  return (", ".join((word_list_anagram(word))))

@app.route('/monitor')
def monitor():
  return "UP"

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
