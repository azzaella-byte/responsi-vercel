import mysql.connector
from mysql.connector import Error

from config import Config


def get_connection():
    """
    Membuat koneksi ke database MySQL.
    """

    try:
        connection = mysql.connector.connect(
            host="sn90ww.h.filess.io",
            port="3306",
            user="db_akademik_represent",
            password="1706563509498dc41f31f7478ed988a0ef176b6d",
            database="db_akademik_represent"
        )

        return connection

    except Error as e:
        print(f"Gagal terhubung ke database: {e}")
        return None