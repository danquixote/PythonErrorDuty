#!/usr/bin/env python
from flask import Flask, request, redirect
from connect_to_pd import PDIncident as pdi


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@pdi('6243b99729d742bd981db183dfae0fa9')
def bar():
    return str(1000/0)


if __name__ == "__main__":
    app.run(debug=False)
