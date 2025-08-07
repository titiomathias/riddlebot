from database.db import get_connect
from database.utils import time_controllers

def insertRiddle(riddle_id:int, user_id: int, status: bool):
    try:
        created_at = time_controllers.generate_timestamp()

        with get_connect() as con:
            cur = con.cursor()

            cur.execute(
                "INSERT INTO subs(riddle_id, user_id, status, created_at) VALUES (?, ?, ?, ?)",
                (riddle_id, user_id, status, created_at)
            )

            con.commit()

        return True
    except Exception as e:
        print("Ocorreu um erro ao tentar inserir a inscrição: ", e)
        return False
    

def delRiddle(user_id:int):
    try:
        with get_connect() as con:
            cur = con.cursor()

            cur.execute(
                f"DELETE FROM subs WHERE user_id = ?",
                (user_id,)
            )

            con.commit()
        return True
    except Exception as e:
        print("Ocorreu um erro ao deletar a inscrição: ", e)
        return False


def getRiddle(user_id:int):
    try:
        with get_connect() as con:
            cur = con.cursor()

            cur.execute(
                f"SELECT * FROM users WHERE user_id = ? or id = ?",
                (user_id, user_id)
            )
            sub_data = cur.fetchone()

            return sub_data
    except Exception as e:
        print("Ocorreu um erro ao tentar coletar dados da inscrição: ", e)
