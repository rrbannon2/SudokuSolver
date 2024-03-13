from flask import Flask, request, jsonify, render_template
import clingoSudokuSolver as solver

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/solve', methods = ["POST"])
def load_puzzle():
    solution = solver.run_python(request.get_json())
    # print(solution)
    return jsonify(solution)
    

if __name__ == '__main__':
    app.run(debug=True) 