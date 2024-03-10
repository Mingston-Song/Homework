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
    query = "SELECT id, fname, lname FROM students"
    cur = con.cursor()
    cur.execute(query)
    students_list = cur.fetchall()
    query = "SELECT name FROM works"
    cur = con.cursor()
    cur.execute(query)
    works_list = cur.fetchall()
    con.close()
    print(assignments_list)
    print(students_list)
    print(works_list)
    returned_list = []
    for assignment in assignments_list:
        temp_list = ["", "", "", 0]
        temp_list[0] = students_list[assignment[0] - 1][1] + " " + students_list[assignment[0] - 1][2]
        temp_list[1] = works_list[assignment[1] - 1][0]
        temp_list[2] = assignment[2]
        temp_list[3] = assignment[3]
        returned_list.append(temp_list)
    print(returned_list)
    return render_template('main.html', assignments=returned_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)