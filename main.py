from fastapi import FastAPI, Query
from sqlalchemy import create_engine, Text

app = FastAPI()

def connect_db(username='root', password='root', host='postgres', port='5432', database='postgres'):
    try:
        engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
        conn = engine.connect()
        print('Conectado correctamente a la base de datos')
        return conn, engine
    except Exception as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None, None

@app.get('/')
def get_data(query: str = Query("SELECT * FROM vocabulary_umls LIMIT 5")):
    conn, engine = connect_db()

    if conn:
        result = conn.execute(Text(query))
        data = [dict(row) for row in result]
        conn.close()
        return data
    else:
        return {"error": "No se pudo conectar a la base de datos"}
