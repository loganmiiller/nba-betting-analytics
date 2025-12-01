from db import get_connection
from extract import fetch_teams
import psycopg2

def insert_teams(teams):
    conn = get_connection()
    cur = conn.cursor()

    try:
        for team in teams:
            cur.execute("""
                        INSERT INTO teams (id, conference, division, city, name, full_name, abbreviation)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (id) DO NOTHING;
                        """,
                        (team['id'], team['conference'], team['division'], team['city'],
                        team['name'], team['full_name'], team['abbreviation'])
                        )
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    teams = fetch_teams()
    insert_teams(teams)