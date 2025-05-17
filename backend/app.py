from flask import Flask, jsonify
import psycopg2 # type: ignore
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from backend API"})

@app.route('/api/db')
def db_test():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'db'),
            dbname=os.getenv('POSTGRES_DB', 'mydb'),
            user=os.getenv('POSTGRES_USER', 'useradmin'),
            password=os.getenv('POSTGRES_PASSWORD', 'mypass'),
        )
        cur = conn.cursor()
        cur.execute('SELECT 1;')
        result = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"db_connection": "success", "result": result})
    except Exception as e:
        return jsonify({"db_connection": "failed", "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)