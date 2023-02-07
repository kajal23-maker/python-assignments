from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


@app.route('/')
def view():
    connection = sqlite3.connect("student.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    return render_template("index.html", rows=rows)


@app.route('/add')
def add():
    return render_template("add.html")


@app.route('/save', methods=["POST"])
def save():
    msg = "msg"
    name = request.form["name"]
    email = request.form["email"]
    contact = request.form["contact"]
    dept = request.form["dept"]
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO students(student_name, student_email, student_phoneno, student_dept ) values(?,?,"
                       "?,?)", (name, email, contact, dept))
        connection.commit()
        msg = "Student added successfully!"
    except:
        connection.rollback()
        msg = "Cannot add student (unknown error occurred)"
    finally:
        connection.close()
        return redirect(url_for("view"))


@app.route('/delete', methods=["POST"])
def delete():
    st_id = request.form["todelete"]
    print(st_id)
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    msg = "msg"
    try:
        cursor.execute("DELETE FROM students WHERE student_id = ?", (st_id, ))
        msg = "Record successfully deleted!"
        connection.commit()
    except:
        msg = "Can not delete! Unexpected error occurred"
    finally:
        connection.close()
        return redirect(url_for("view"))


@app.route('/update', methods=["POST"])
def update():
    stu_id = request.form["toupdate"]
    # print(stu_id)
    return render_template('update.html', id=stu_id)


@app.route('/updaterecord', methods=["POST"])
def updaterecord():
    st_id = request.form["update"]
    new_name = request.form["name"]
    new_email = request.form["email"]
    new_phone = request.form["contact"]
    new_dept = request.form["dept"]
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    msg = ""
    try:
        cursor.execute("UPDATE students SET student_name = ?, student_email = ?, student_phoneno = ?, student_dept = "
                       "? WHERE student_id = ?", (new_name, new_email, new_phone, new_dept, st_id))
        connection.commit()
    except:
        return render_template("update.html")
    finally:
        connection.close()
        return redirect(url_for("view"))


if __name__ == "__main__":
    app.run(debug=True)
