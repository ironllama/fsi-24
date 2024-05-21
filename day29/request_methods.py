from flask import Flask, request

app = Flask(__name__)

general_css = """
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            flex-direction: column;
            gap: 2rem;
        }
    </style>
"""

square_css = """
    <style>
        div.square {
            width: 10rem;
            height: 10rem;
            border-radius: 10px;
            background-color: cornflowerblue;
        }
    </style>
"""

def drawSquare(color, size):
    return f"<div class='square' style='background-color:{color}; width:{size}rem; height:{size}rem;'></div>"

@app.get("/squareGet")
def one():
    new_color = request.args.get('color')
    square_size = request.args.get('size')

    return general_css + square_css + drawSquare(new_color, square_size)

@app.post("/squarePost")
def two():
    new_color = request.form.get('color')
    square_size = request.form.get('size')

    return general_css + square_css + drawSquare(new_color, square_size)

@app.route("/squareBoth", methods=['GET', 'POST'])
def three():
    if request.method == 'GET':
        new_color = request.args.get('color')
        square_size = request.args.get('size')
    else:
        new_color = request.form.get('color')
        square_size = request.form.get('size')

    return general_css + square_css + drawSquare(new_color, square_size)

@app.post("/squareJson")
def four():
    new_color = request.json.get('color')
    square_size = request.json.get('size')

    return general_css + square_css + drawSquare(new_color, square_size)

@app.get("/getSquareColor")
def getSquareColor():
    return general_css + """
    <style>
        form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
    </style>

    <fieldset>
        <legend>GET Request</legend>
        <form method="get" action="/squareGet">
            <div>
                <label>
                    Enter a valid CSS color:
                    <input name="color">
                </label>
            </div>
            <div>
                <label>
                    Enter a size:
                    <input type="number" name="size">
                </label>
            </div>
            <button>Send</button>
        </form>
    </fieldset>

    <fieldset>
        <legend>POST Request</legend>
        <form method="post" action="/squarePost">
            <div>
                <label>
                    Enter a valid CSS color:
                    <input name="color">
                </label>
            </div>
            <div>
                <label>
                    Enter a size:
                    <input type="number" name="size">
                </label>
            </div>
            <button>Send</button>
        </form>
    </fieldset>

    <fieldset>
        <legend>POST/JSON Request</legend>
        <form id="jsonForm">
            <div>
                <label>
                    Enter a valid CSS color:
                    <input name="color">
                </label>
            </div>
            <div>
                <label>
                    Enter a size:
                    <input type="number" name="size">
                </label>
            </div>
            <button>Send</button>
        </form>
        <div id="stuff" style="display: flex; justify-content: center;"></div>
    </fieldset>


    <script>
        document.querySelector("#jsonForm").addEventListener("submit", evt => {
            evt.preventDefault();

            // Turn into FormData so we can get data out of the form easily.
            // You could have also put an id on each input and used
            // document.querySelector or document.getElementById to get the
            // input values. (eg. document.getElementById('colorInput').value)
            const fd = new FormData(evt.target);
            const color = fd.get("color");
            const size = fd.get("size");

            // Fetch with a POST request.
            // NOTE: JSON requests require the Content-type header to be set
            // appropriately as application/json
            const fetchOptions = {
                method: "post",
                headers: {
                    "Content-type": "application/json",
                },
                // body: JSON.stringify({ color: color, size: size })
                body: JSON.stringify({ color, size })  // Same as above.
            }

            fetch("/squareJson", fetchOptions)
                .then(res => res.text())
                .then(res => {
                    // The '/squareJson' endpoint returns HTML. This is not
                    // typical, but to make the most of it, we're going
                    // to replace a portion of the UI with the new HTML.
                    document.querySelector('#stuff').innerHTML = res;
                });
        })
    </script>
"""
