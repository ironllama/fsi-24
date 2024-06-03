from flask import Flask, request
import sqlalchemy
from sqlalchemy import text

app = Flask(__name__)

db = sqlalchemy.create_engine(
	"mariadb+mariadbconnector://root:@localhost:3306/fsi-24",
	echo=True
	)

@app.get("/phones")
def phones():
  returnStr = ""
  field = request.args.get("field", "id")
  # all_fields = fields.split(",")
  
  with db.begin() as conn:
    # response = conn.execute(text("SELECT * FROM phones"))
    # for phone in response:
    #   returnStr += f"""
    #     <p>
    #       <strong>Phone</strong>: { phone.model } <br />
    #       The owner of this phone is: { phone.owner }, and sells the phone at the price of { phone.price } dollars! <br />
    #       This phone brand is { phone.brand } and weight { phone.weight }g at maximum.<br />
    #       { phone.owner } had given this comment { phone.model}: <em>{ phone.comment }</em>
    #     </p>
    #     """
    response = conn.execute(text(f"SELECT {field} FROM phones LIMIT 0, 10"))
    # SELECT [brand] FROM phones LIMIT 0, 10
    # SELECT [1; DROP TABLE phones; SELECT 1] FROM phones LIMIT 0, 10
    for phone in response:
      returnStr += f"{phone[0]}<br>"
    # return response.all()
    # return [{ "model": item.phone_model, "price": item.price } for item in response]
    # return str(response)
  
  return returnStr
