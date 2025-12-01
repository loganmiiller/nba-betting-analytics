from db import get_connection
from extract import fetch_players
import psycopg2

def insert_players(players):
    conn = get_connection()
    cur = conn.cursor()

    try:
        for player in players:
            cur.execute("""
                        INSERT INTO players (id, first_name, last_name, position, height, weight, team_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (id) DO NOTHING;
                        """,
                        (player['id'], player['first_name'], player['last_name'], player['position'],
                        player['height'], player['weight'], player['team']['id'])
                        )
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    players = fetch_players()
    insert_players(players)