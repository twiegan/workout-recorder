import psycopg2


def send_to_db(day, time, focus):
    print(day, time, focus)
    inputs = [day, time, focus]
    conn = psycopg2.connect("host=localhost port=5432 dbname=workout-data user=thomaswiegand password=password")
    cur = conn.cursor()
    s = """INSERT INTO workout(day, time, focus) VALUES (%s, %s, %s)"""
    try:
        cur.execute(s, inputs)
        conn.commit()
    except psycopg2.Error as e:
        error_message = "Database error: " + e + "/n SQL: " + s
        print(error_message)
        return False
    cur.close()
    conn.close()
    return True
