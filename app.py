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
    query = "SELECT students.fname, students.lname, works.name, assignments.due_date, assignments.completed FROM assignments INNER JOIN students ON assignments.student_id=students.id INNER JOIN works ON assignments.work_id=works.id"
    cur = con.cursor()
    cur.execute(query)
    assignments_list = cur.fetchall()
    con.close()
    print(assignments_list)
    return render_template('main.html', assignments=assignments_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)