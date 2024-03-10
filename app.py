from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DATABASE = "C:/Users/20392/OneDrive - Wellington College/homework_list/homework.db"


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)
    return None


@app.route('/')
def render_main():  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT student_id, work_id, due_date, completed FROM assignments"
    cur = con.cursor()
    cur.execute(query)
    assignments_list = cur.fetchall()
    print(assignments_list)
    return render_template('main.html', assignments=assignments_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
