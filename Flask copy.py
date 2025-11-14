from flask import Flask, render_template_string, request, redirect
import mysql.connector

app = Flask(__name__)

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "students"
    )

def get_students():
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM information")
    return mycursor.fetchall()

@app.route('/')
def home():
    students = get_students()

    html = '''
    <html>
    <body>
        <h1>Students Data</h1>
        <a href="/add">Sign In</a>
        <table border="1" cellpadding = "5" cellspacing = "0">
            <tr>
                <th>Id</th>
                <th>First_Name</th>
                <th>Middle_Name</th>
                <th>Sur_Name</th>
                <th>Section</th>
                <th>Address</th>
                <th>Year</th>
                <th>Age</th>
                <th>Sex</th>
                <th>Motto</th>
                <th>Actions</th>
            </tr>
            {% for row in students %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
                <td>{{ row[3] }}</td>
                <td>{{ row[4] }}</td>
                <td>{{ row[5] }}</td>
                <td>{{ row[6] }}</td>
                <td>{{ row[7] }}</td>
                <td>{{ row[8] }}</td>
                <td>{{ row[9] }}</td>
                <td>
                    <a href="/update/{{ row[0] }}">Update</a>
                     <a href="/delete/{{ row[0] }}" onclick="return confirm('Are you sure you want to delete this student?');">Delete</a>
                </td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    '''
    return render_template_string(html, students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        firstname = request.form['firstname']
        midname = request.form['midname']
        surname = request.form['surname']
        sect = request.form['sect']
        addr = request.form['addr']
        year = request.form['year']
        age = request.form['age']
        sex = request.form['sex']
        motto = request.form['motto']

        mydb =connect_db()
        mycursor = mydb.cursor()
        sql = "INSERT INTO information (First_Name, Middle_Name, Sur_name, Section, Address, Year, Age, Sex, Motto) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (firstname, midname, surname, sect, addr, year, age, sex, motto)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')

    html = '''
    <html>
        <body>
            <h1>Sign In</h1>
            <form method="POST">
                <label for="firstname">FirstName:</label>
                <input type="text" id="firstname" name="firstname" required>
                <label for="midname">MiddleName:</label>
                <input type="text" id="midname" name="midname" required>
                <label for="surname">Surname:</label>
                <input type="text" id="surname" name="surname" required>
                <label for="sect">Section:</label>
                <input type="text" id="sect" name="sect" required>
                <label for="addr">Address:</label>
                <input type="text" id="addr" name="addr" required>
                <label for="year">Year:</label>
                <input type="text" id="year" name="year" required>
                <label for="age">Age:</label>
                <input type="number" id="age" name="age" min="1" max="90" required>
                <label for="sex">Sex:</label>
                <input type="text" id="sex" name="sex" required>
                <label for="motto">Motto:</label>
                <input type="text" id="motto" name="motto" required>
                <button type="submit">Add</button>
                <a href="/">Cancel</a>
            </form>
        </body>
    </html>
    '''
    return render_template_string(html)

@app.route( '/update/<int:id>', methods=['GET', 'POST'])
def update_students(id):
    mydb = connect_db()
    mycursor = mydb.cursor()

    if request.method == 'POST':
        firstname = request.form['firstname']
        midname = request.form['midname']
        surname = request.form['surname']
        sect = request.form['sect']
        addr = request.form['addr']
        year = request.form['year']
        age = request.form['age']
        sex = request.form['sex']
        motto = request.form['motto']

        sql = "UPDATE information SET First_Name = %s, Middle_Name = %s, Sur_name = %s, Section = %s, Address = %s, Year = %s, Age = %s, Sex = %s, Motto = %s WHERE Id = %s"
        val = (firstname, midname, surname, sect, addr, year, age, sex, motto, id)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')

    mycursor.execute("SELECT * FROM information WHERE id = %s", (id,))
    student = mycursor.fetchone()

    html = '''
    <html>
        <body>
            <h1>Update Student</h1>
            <form method="POST">
                <label for="firstname">FirstName:</label>
                <input type="text" id="firstname" name="firstname" value="{{ student[1] }}" required>
                <label for="midname">MiddleName:</label>
                <input type="text" id="midname" name="midname" value="{{ student[2] }}" required>
                <label for="surname">Surname:</label>
                <input type="text" id="surname" name="surname" value="{{ student[3] }}" required>
                <label for="sect">Section:</label>
                <input type="text" id="sect" name="sect" value="{{ student[4] }}" required>
                <label for="addr">Address:</label>
                <input type="text" id="addr" name="addr" value="{{ student[5] }}" required>
                <label for="year">Year:</label>
                <input type="text" id="year" name="year" value="{{ student[6] }}" required>
                <label for="age">Age:</label>
                <input type="number" id="age" name="age" min="1" max="90" value="{{ student[7] }}" required>
                <label for="sex">Sex:</label>
                <input type="text" id="sex" name="sex" value="{{ student[8] }}" required>
                <label for="motto">Motto:</label>
                <input type="text" id="motto" name="motto" value="{{ student[9] }}" required>
                <button type="submit">Add</button>
                <a href="/">Cancel</a>
            </form>
        </body>
    </html>
    '''
    return render_template_string(html, student=student)

@app.route('/delete/<int:id>')
def delete_students(id):
    mydb = connect_db()
    mycursor = mydb.cursor()
    sql = "DELETE FROM information WHERE Id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
