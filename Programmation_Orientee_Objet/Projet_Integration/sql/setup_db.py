from classes.user_repository import User
import sqlite3

SELECT_USERS = """SELECT * FROM USERS;"""
SELECT_ROLE = """SELECT UG.NAME FROM USER_GROUPS UG JOIN USER_IN_GROUP UIG ON UG.ID = UIG.GROUP_ID WHERE UIG.MATRICULE = ?"""


def create_db(db_file):
    try:
        db = sqlite3.connect(db_file)
        cursor = db.cursor()

        with open("sql/database.sql") as db_script:
            script = db_script.readlines()

            for query in script:
                query = query.rstrip("\n")

                if query[0].lower() == 'c':
                    try:
                        cursor.execute(query)
                        db.commit()

                    except Exception:
                        query = query.split(" ")
                        print(f"Table '{query[2]}' already created.")

                elif query[0].lower() == 'i':
                    try:
                        cursor.execute(query)
                        db.commit()

                    except Exception:
                        query = query.split(" ")
                        print(f"Data for table '{query[2]}' already inserted.")

                else:
                    continue

        db.close()

    except FileNotFoundError:
        print("DataBase creation from file: 'database.sql' failed.")


def script_to_get_users(self, cursor):
    cursor.execute(SELECT_USERS)
    for user in cursor.fetchall():
        self.users.append(User(user[0], user[1], user[2]))
    return self.users


def get_role_of_user(users, cursor):
    for user in users:
        cursor.execute(SELECT_ROLE, (user.login,))
        roles = cursor.fetchall()
        if len(roles) > 1:
            for role in roles:
                user.role += role[0] + ", "
            user.role = user.role.rstrip(", ")
        else:
            user.role += roles[0][0]
