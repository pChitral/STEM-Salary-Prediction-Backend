from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Race CRUD

class Item(BaseModel):
    race_id: int
    race_name: str


@app.post("/race/create")
async def create_race(item: Item):
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Race (race_id, race_name) VALUES (?, ?)",
              (item.race_id, item.race_name))
    conn.commit()
    conn.close()
    return {"item": item}


@app.get("/races/")
async def read_races():
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Race")
    items = []
    for row in c.fetchall():
        item = {"race_id": row[0],  "race_name": row[1]}
        items.append(item)
    conn.commit()
    conn.close()
    return {"items": items}


@app.put("/race/update/{item_id}")
async def update_race(item_id: int, item: Item):
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("UPDATE Race SET race_name = ? WHERE race_id = ?",
              (item.race_id, item.race_name))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": item}


@app.delete("/race/delete/{item_id}")
async def delete_race(item_id: int):
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("DELETE FROM Race WHERE race_id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"item_id": item_id}
