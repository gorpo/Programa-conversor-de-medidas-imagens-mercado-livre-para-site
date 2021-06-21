#!/usr/bin/python
import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",passwd="",db="test")
cursor = conn.cursor()

def chat_exists(chat_id):  # se o chat existir ele nao cadastra de novo o mesmo chat
  cursor.execute(f"""SELECT * FROM chats WHERE chat_id = {chat_id} """)
  if cursor.fetchone():
    print('retorna true')
    return True
  else:
    print('retorna false')
    return False

if not chat_exists(-214748364801):
            cursor.execute(f"""INSERT INTO chats (chat_id, welcome_enabled,  chat_lang) VALUES ({123123123},{True},{123})""")
            conn.commit()

            cursor.execute(f"""UPDATE chats SET cached_admins = {1111111111} WHERE chat_id = {-2147483648}""")
            conn.commit()