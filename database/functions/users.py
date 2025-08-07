from database.db import get_connect

def insertUser(user_id: int, email: str = None, phone: str = None, balance: float = 0.0):
    try:
        with get_connect() as con:
            cur = con.cursor()

            cur.execute(
                "INSERT INTO users(user_id, email, phone, balance) VALUES (?, ?, ?, ?)",
                (user_id, email, phone, balance)
            )

            con.commit()

        return True
    except Exception as e:
        print("Ocorreu um erro ao tentar inserir o usuário: ", e)
        return False
    

def delUser(user_id:int):
    try:
        with get_connect() as con:
            cur = con.cursor()

            cur.execute(
                f"DELETE FROM users WHERE user_id = ?",
                (user_id,)
            )

            con.commit()
        return True
    except Exception as e:
        print("Ocorreu um erro ao deletar o usuário: ", e)
        return False


def getUser(user_id:int):
    try:
        with get_connect() as con:
            cur = con.cursor()

            cur.execute(
                f"SELECT * FROM users WHERE user_id = ?",
                (user_id,)
            )
            user_data = cur.fetchone()

            return user_data
    except Exception as e:
        print("Ocorreu um erro ao tentar coletar dados dos usuários: ", e)
