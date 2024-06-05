import sqlalchemy
from sqlalchemy import text

db = sqlalchemy.create_engine(
	"mariadb+mariadbconnector://root:@localhost:3306/fsi-24",
	# echo=True
	)

with db.begin() as conn:
    results = conn.execute(
        text("SELECT model, LENGTH(comment) AS comment FROM phones")
    )
    print("|--------------------+-----|")
    for row in results:
        print("|" + row.model.ljust(20, ' ') + "|" + str(row.comment).ljust(5, " ") + "|")
        print("|--------------------+-----|")
    print()

    results = conn.execute(
        text("SELECT AVG(weight) as avg_weight FROM phones WHERE owner='Brad'")
    )
    print(results.one().avg_weight)
    print()
