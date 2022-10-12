import sqlite3


def load_db(path='source/score.db'):
    connect = sqlite3.connect(path);
    cursor = connect.cursor();

    try :
        cursor.execute("SELECT * FROM SCORE_TABLE");
    except:
        cursor.execute('CREATE TABLE SCORE_TABLE (name text, accuracy integer, time float)');
        cursor.execute("SELECT * FROM SCORE_TABLE");

    return connect ,cursor


def save_score2db(data,cursor,connect):
    cursor.execute("INSERT INTO SCORE_TABLE VALUES(?,?,?)", data);
    connect.commit()
    return cursor


def is_samename(user_name, name_list):
    if user_name in name_list:
        return True
    return False

