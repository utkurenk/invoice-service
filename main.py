from flask import Flask, jsonify, request
from flask_restful import Api
import sqlite3
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)
cors = CORS(app)
api = Api(app)
DATABASE = "Chinook_Sqlite.sqlite"


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except sqlite3.error as e:
        logger.exception("Database error has occured.", e)
    return conn


@app.route("/api/invoices", methods=["GET"])
def invoices_get():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        logger.info("Get request received.")
        cursor = conn.execute("SELECT * FROM Invoice")
        invoices = [
            dict(invoice_id=row[0], customer_id=row[1], date=row[2], address=row[3], city=row[4], state=row[5],
                 country=row[6], postal_code=row[7], total=row[8]) for row in cursor.fetchall()
        ]
        if invoices is not None:
            return jsonify(invoices)


@app.route("/api/invoices/<int:invoice_id>", methods=["GET"])
def single_invoice(invoice_id):
    conn = db_connection()
    cursor = conn.cursor()
    invoice = None

    if request.method == "GET":
        cursor.execute("SELECT * FROM Invoice WHERE InvoiceId=?", (invoice_id,))
        invoice = [
            dict(invoice_id=row[0], customer_id=row[1], date=row[2], address=row[3], city=row[4], state=row[5],
                 country=row[6], postal_code=row[7], total=row[8]) for row in cursor.fetchall()
                ]
        if invoice is not None:
            return jsonify(invoice), 200
        else:
            return "Something wrong.", 404


@app.route("/api/invoices/add", methods=["POST"])
def invoice_add():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        customer_id = request.form['CustomerId']
        invoice_date = request.form["InvoiceDate"]
        billing_address = request.form["BillingAddress"]
        billing_city = request.form["BillingCity"]
        billing_state = request.form["BillingState"]
        billing_country = request.form["BillingCountry"]
        billing_postalcode = request.form["BillingPostalCode"]
        total = request.form["Total"]
        sql = """INSERT INTO Invoice (CustomerId, InvoiceDate, BillingAddress, BillingCity, BillingCountry,
                BillingState, BillingPostalCode, Total) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor = conn.execute(sql, (customer_id, invoice_date, billing_address, billing_city, billing_state,
                                    billing_country, billing_postalcode, total))
        conn.commit()
        return f"Invoice with the InvoiceId: {cursor.lastrowid} created successfully"


@app.route("/api/invoices/update/<int:invoice_id>", methods=["PUT"])
def update_invoice(invoice_id):
    if request.method == "PUT":
        conn = db_connection()
        cursor = conn.cursor()
        sql = """UPDATE Invoice
                SET CustomerId=?,
                    InvoiceDate=?,
                    BillingAddress=?,
                    BillingCity=?,
                    BillingCountry=?,
                    BillingState=?,
                    BillingPostalCode=?,
                    Total=?
                WHERE InvoiceId=? """
        customer_id = request.form["CustomerId"]
        invoice_date = request.form["InvoiceDate"]
        billing_address = request.form["BillingAddress"]
        billing_city = request.form["BillingCity"]
        billing_state = request.form["BillingState"]
        billing_country = request.form["BillingCountry"]
        billing_postalcode = request.form["BillingPostalCode"]
        total = request.form["Total"]
        updated_invoice = {
            "InvoiceId": invoice_id,
            "CustomerId": customer_id,
            "BillingAddress": billing_address,
            "BillingCity": billing_city,
            "BillingState": billing_state,
            "BillingCountry": billing_country,
            "BillingPostalCode": billing_postalcode,
            "Total": total,
            "InvoiceDate": invoice_date,
        }
        conn.execute(sql, (customer_id, invoice_date, billing_address, billing_city, billing_country,
                           billing_state, billing_postalcode, total, invoice_id))
        conn.commit()
        return "Success"


@app.route("/api/invoices/delete/<int:invoice_id>", methods=["DELETE"])
def del_invoice(invoice_id):
    conn = db_connection()
    sql = """ DELETE FROM Invoice WHERE InvoiceId=? """
    conn.execute(sql, (invoice_id,))
    conn.commit()
    return "The invoice with id: {} has been deleted.".format(invoice_id), 200


if __name__ == "__main__":
    logger.info("Application is starting up @ Port:5000")
    app.run(debug=True, host='0.0.0.0')
