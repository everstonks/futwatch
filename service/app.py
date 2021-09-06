from flask import Flask, render_template
import subprocess

subprocess.call(" python3 htmlgenerator.py", shell=True)

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')
if __name__ == '__main__':
  app.run()
