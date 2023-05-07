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


# Education CRUD

class EducationItem(BaseModel):
    edu_id: int
    edu_name: str


@app.post("/education/create")
async def create_education(item: EducationItem):
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Education (edu_id, edu_name) VALUES (?, ?)",
              (item.edu_id, item.edu_name))
    conn.commit()
    conn.close()
    return {"item": item}


@app.get("/educations/")
async def read_educations():
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Education")
    items = []
    for row in c.fetchall():
        item = {"edu_id": row[0],  "edu_name": row[1]}
        items.append(item)
    conn.commit()
    conn.close()
    return {"items": items}


@app.put("/education/update/{item_id}")
async def update_education(item_id: int, item: EducationItem):
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("UPDATE Education SET edu_name = ? WHERE edu_id = ?",
              (item.edu_name, item_id))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": item}


@app.delete("/education/delete/{item_id}")
async def delete_education(item_id: int):
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("DELETE FROM Education WHERE edu_id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"item_id": item_id}

# City CRUD

class CityItem(BaseModel):
    city_id: int
    city_name: str


@app.post("/city/create")
async def create_city(city_item: CityItem):
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO City (city_id, city_name) VALUES (?, ?)",
              (city_item.city_id, city_item.city_name))
    conn.commit()
    conn.close()
    return {"item": city_item}


@app.get("/cities/")
async def read_cities():
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM City")
    items = []
    for row in c.fetchall():
        item = {"city_id": row[0],  "city_name": row[1]}
        items.append(item)
    conn.commit()
    conn.close()
    return {"items": items}


@app.put("/city/update/{item_id}")
async def update_city(item_id: int, city_item: CityItem):
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("UPDATE City SET city_name = ? WHERE city_id = ?",
              (city_item.city_name, item_id))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": city_item}


@app.delete("/city/delete/{item_id}")
async def delete_city(item_id: int):
    conn = sqlite3.connect('jobs_database.db')
    c = conn.cursor()
    c.execute("DELETE FROM City WHERE city_id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"item_id": item_id}
