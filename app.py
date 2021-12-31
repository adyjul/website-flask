from os import PathLike
from flask import Flask, render_template, request, url_for, redirect,jsonify
from flask_mysqldb import MySQL
app=Flask(__name__,template_folder='template')

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'TubesWeb'
mysql = MySQL(app)

def query(query):
    cur1 = mysql.connection.cursor()
    cur1.execute(query)
    rs = cur1.fetchall()
    cur1.close()
    return rs


def tablePg():
    return "SELECT * FROM pengumuman"


def tablebr():
    return "SELECT * FROM berita"

a = lambda x,y : x.append(y[0]) 


# frontend

@app.route('/home')
def home():
    data1 = query(tablePg())
    data2 = query(tablebr())

    return render_template('home.html', data1=data1, data2=data2)


# end frontend


# berita

@app.route('/berita')
def admin():
    data1 = query(tablebr())
    return render_template('tambah_berita.html', data=data1)


@app.route('/berita/show/<string:id_data>')
def showId(id_data):
    def inner_showId():
        id = id_data        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM berita WHERE id=%s", (id))
        rv = cur.fetchall()
        fields_list = cur.description  # sql key name
        cur.close()

        column_list = []    
        for i in fields_list:
            a(column_list,i)   
            
        jsonData_list = []
        for row in rv:
            data_dict = {}
            for i in range(len(column_list)):
                data_dict[column_list[i]] = row[i]

            jsonData_list.append(data_dict)

        return jsonify({
            'status': True,
            'data': jsonData_list
        })
    return inner_showId()


@app.route('/berita/simpan', methods=["POST"])
def simpan():
    judul = request.form['judul']
    isi = request.form['isi']
    cur = mysql.connection.cursor()
    sql = "INSERT INTO berita (judul, isi) VALUES (%s, %s)"
    val = (judul, isi)
    cur.execute(sql, val)

    mysql.connection.commit()
    return redirect(url_for('admin'))


@app.route('/berita/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM berita WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('admin'))


@app.route('/berita/update', methods=["POST"])
def update():
    id_data = request.form['id']
    judul = request.form['judul']
    isi = request.form['isi']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE berita SET judul=%s,isi=%s WHERE id=%s", (judul, isi, id_data,))
    mysql.connection.commit()
    return redirect(url_for('admin'))


# end berita

# pengumuman

@app.route('/pengumuman')
def adminP():
    data1 = query(tablePg())
    return render_template('tambah_pengumuman.html', data=data1)


@app.route('/pengumuman/show/<string:id_data>')
def showIdP(id_data):

    def inner_showID() :
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM pengumuman WHERE id=%s", (id_data))
        rv = cur.fetchall()
        fields_list = cur.description  # sql key name
        cur.close()        

        column_list = []    
        for i in fields_list:
            a(column_list,i)        
        print("print final colume_list", column_list)

        jsonData_list = []
        for row in rv:
            data_dict = {}
            for i in range(len(column_list)):
                data_dict[column_list[i]] = row[i]

            jsonData_list.append(data_dict)

        return jsonify({
            'status': True,
            'data': jsonData_list
        })

    return inner_showID()


@app.route('/pengumuman/simpan', methods=["POST"])
def simpanP():
    judul = request.form['judul']
    isi = request.form['isi']
    lokasi = request.form['lokasi']
    cur = mysql.connection.cursor()
    sql = "INSERT INTO pengumuman (judul, isi, lokasi) VALUES (%s, %s, %s)"
    val = (judul, isi, lokasi)
    cur.execute(sql, val)

    mysql.connection.commit()
    return redirect(url_for('adminP'))


@app.route('/pengumuman/hapus/<string:id_data>', methods=["GET"])
def hapusP(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM pengumuman WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('adminP'))


@app.route('/pengumuman/update', methods=["POST"])
def updateP():
    id_data = request.form['id']
    judul = request.form['judul']
    isi = request.form['isi']
    lokasi = request.form['lokasi']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE pengumuman SET judul=%s,isi=%s,lokasi=%s WHERE id=%s", (judul, isi, lokasi, id_data))
    mysql.connection.commit()    
    return redirect(url_for('adminP'))

# end pengumuman


if __name__=="__main__":
    app.run(host='127.0.0.9',port=4455,debug=True) 