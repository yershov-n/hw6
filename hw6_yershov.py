# Создать `view` функцию выводящую длительность треков сгрупированную по жанрам.
#
# Решить данную задачу средствами Python.

from flask import Flask
from db import execute_query
from formater import list_rec2html_br, records2dct, milliseconds_conv
from utils import duration_in_millisec


app = Flask(__name__)


@app.route('/tracks')
def get_duration():
    sql = 'select "GenreId", "Milliseconds" from tracks'
    sql_genres = 'select * from genres'

    records = execute_query(sql)
    records_genres = execute_query(sql_genres)

    duration = duration_in_millisec(records)
    genres_dct = records2dct(records_genres)

    res_lst = []
    for _ in duration:
        res_lst += [f'{genres_dct[_]}: {milliseconds_conv(duration[_])}']

    return list_rec2html_br(res_lst)


app.run(debug=True)
