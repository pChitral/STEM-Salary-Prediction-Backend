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


db_path = 'jobs_database.db'


def db_connection():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    return conn, c


def close_db_connection(conn):
    conn.commit()
    conn.close()

# Race CRUD


class Item(BaseModel):
    race_id: int
    race_name: str


@app.post("/race/create")
async def create_race(item: Item):
    conn, c = db_connection()
    c.execute("INSERT INTO Race (race_id, race_name) VALUES (?, ?)",
              (item.race_id, item.race_name))
    conn.commit()
    conn.close()
    return {"item": item}


@app.get("/races/")
async def read_races():
    conn, c = db_connection()
    c.execute("SELECT * FROM Race")
    items = []
    for row in c.fetchall():
        item = {"race_id": row[0],  "race_name": row[1]}
        items.append(item)
    close_db_connection(conn)
    return {"items": items}


@app.put("/race/update/{item_id}")
async def update_race(item_id: int, item: Item):
    conn, c = db_connection()
    c.execute("UPDATE Race SET race_name = ? WHERE race_id = ?",
              (item.race_id, item.race_name))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": item}


@app.delete("/race/delete/{item_id}")
async def delete_race(item_id: int):
    conn, c = db_connection()
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
    conn, c = db_connection()
    c.execute("INSERT INTO Education (edu_id, edu_name) VALUES (?, ?)",
              (item.edu_id, item.edu_name))
    conn.commit()
    conn.close()
    return {"item": item}


@app.get("/educations/")
async def read_educations():
    conn, c = db_connection()
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
    conn, c = db_connection()
    c.execute("UPDATE Education SET edu_name = ? WHERE edu_id = ?",
              (item.edu_name, item_id))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": item}


@app.delete("/education/delete/{item_id}")
async def delete_education(item_id: int):
    conn, c = db_connection()
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
    conn, c = db_connection()
    c.execute("INSERT INTO City (city_id, city_name) VALUES (?, ?)",
              (city_item.city_id, city_item.city_name))
    conn.commit()
    conn.close()
    return {"item": city_item}


@app.get("/cities/")
async def read_cities():
    conn, c = db_connection()
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
    conn, c = db_connection()
    c.execute("UPDATE City SET city_name = ? WHERE city_id = ?",
              (city_item.city_name, item_id))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": city_item}


@app.delete("/city/delete/{item_id}")
async def delete_city(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM City WHERE city_id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"item_id": item_id}

# COMPANY CRUD

# Define the Item schema


class CompanyItem(BaseModel):
    company_id: int
    company_name: str


# Create a new company
@app.post("/company/create")
async def create_company(item: CompanyItem):
    conn, c = db_connection()
    c.execute("INSERT INTO Company (company_id, company_name) VALUES (?, ?)",
              (item.company_id, item.company_name))
    conn.commit()
    conn.close()
    return {"item": item}


# Read all companies
@app.get("/companies/")
async def read_companies():
    conn, c = db_connection()
    c.execute("SELECT * FROM Company")
    items = []
    for row in c.fetchall():
        item = {"company_id": row[0], "company_name": row[1]}
        items.append(item)
    conn.commit()
    conn.close()
    return {"items": items}


# Update a company by company_id
@app.put("/company/update/{company_id}")
async def update_company(company_id: int, item: CompanyItem):
    conn, c = db_connection()
    c.execute("UPDATE Company SET company_name = ? WHERE company_id = ?",
              (item.company_name, company_id))
    conn.commit()
    conn.close()
    return {"company_id": company_id, "item": item}


# Delete a company by company_id
@app.delete("/company/delete/{company_id}")
async def delete_company(company_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Company WHERE company_id = ?", (company_id,))
    conn.commit()
    conn.close()
    return {"company_id": company_id}


# Tag CRUD

class Tag(BaseModel):
    tag_id: int
    tag_name: str


@app.post("/tag/create")
async def create_tag(item: Tag):
    conn, c = db_connection()
    c.execute("INSERT INTO Tag (tag_id, tag_name) VALUES (?, ?)",
              (item.tag_id, item.tag_name))
    conn.commit()
    conn.close()
    return {"item": item}


@app.get("/tags/")
async def read_tags():
    conn, c = db_connection()
    c.execute("SELECT * FROM Tag")
    items = []
    for row in c.fetchall():
        item = {"tag_id": row[0],  "tag_name": row[1]}
        items.append(item)
    conn.commit()
    conn.close()
    return {"items": items}


@app.put("/tag/update/{item_id}")
async def update_tag(item_id: int, item: Tag):
    conn, c = db_connection()
    c.execute("UPDATE Tag SET tag_name = ? WHERE tag_id = ?",
              (item.tag_name, item_id))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": item}


@app.delete("/tag/delete/{item_id}")
async def delete_tag(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Tag WHERE tag_id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"item_id": item_id}

# TITLE CRUD


class Title(BaseModel):
    title_id: int
    title_name: str


@app.post("/title/create")
async def create_title(item: Title):
    conn, c = db_connection()
    c.execute("INSERT INTO Title (title_id, title_name) VALUES (?, ?)",
              (item.title_id, item.title_name))
    conn.commit()
    conn.close()
    return {"item": item}


@app.get("/titles/")
async def read_titles():
    conn, c = db_connection()
    c.execute("SELECT * FROM Title")
    items = []
    for row in c.fetchall():
        item = {"title_id": row[0],  "title_name": row[1]}
        items.append(item)
    conn.commit()
    conn.close()
    return {"items": items}


@app.put("/title/update/{item_id}")
async def update_title(item_id: int, item: Title):
    conn, c = db_connection()
    c.execute("UPDATE Title SET title_name = ? WHERE title_id = ?",
              (item.title_name, item_id))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": item}


@app.delete("/title/delete/{item_id}")
async def delete_title(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Title WHERE title_id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"item_id": item_id}

# STATE CRUD


class State(BaseModel):
    state_id: int
    state_name: str


@app.post("/state/create")
async def create_state(item: State):
    conn, c = db_connection()
    c.execute("INSERT INTO State (state_id, state_name) VALUES (?, ?)",
              (item.state_id, item.state_name))
    conn.commit()
    conn.close()
    return {"item": item}


@app.get("/states/")
async def read_states():
    conn, c = db_connection()
    c.execute("SELECT * FROM State")
    items = []
    for row in c.fetchall():
        item = {"state_id": row[0],  "state_name": row[1]}
        items.append(item)
    conn.commit()
    conn.close()
    return {"items": items}


@app.put("/state/update/{item_id}")
async def update_state(item_id: int, item: State):
    conn, c = db_connection()
    c.execute("UPDATE State SET state_name = ? WHERE state_id = ?",
              (item.state_name, item_id))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": item}


@app.delete("/state/delete/{item_id}")
async def delete_state(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM State WHERE state_id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"item_id": item_id}

# COUNTRY CRUD


class Country(BaseModel):
    country_id: int
    country_name: str


@app.post("/country/create")
async def create_country(item: Country):
    conn, c = db_connection()
    c.execute("INSERT INTO Country (country_id, country_name) VALUES (?, ?)",
              (item.country_id, item.country_name))
    conn.commit()
    conn.close()
    return {"item": item}


@app.get("/countries/")
async def read_countries():
    conn, c = db_connection()
    c.execute("SELECT * FROM Country")
    items = []
    for row in c.fetchall():
        item = {"country_id": row[0], "country_name": row[1]}
        items.append(item)
    conn.commit()
    conn.close()
    return {"items": items}


@app.put("/country/update/{item_id}")
async def update_country(item_id: int, item: Country):
    conn, c = db_connection()
    c.execute("UPDATE Country SET country_name = ? WHERE country_id = ?",
              (item.country_name, item_id))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": item}


@app.delete("/country/delete/{item_id}")
async def delete_country(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Country WHERE country_id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"item_id": item_id}

# GENDER CRUD


class Gender(BaseModel):
    gender_id: int
    gender_type: str


@app.post("/gender/create")
async def create_gender(item: Gender):
    conn, c = db_connection()
    c.execute("INSERT INTO Gender (gender_id, gender_type) VALUES (?, ?)",
              (item.gender_id, item.gender_type))
    conn.commit()
    conn.close()
    return {"item": item}


@app.get("/genders/")
async def read_genders():
    conn, c = db_connection()
    c.execute("SELECT * FROM Gender")
    items = []
    for row in c.fetchall():
        item = {"gender_id": row[0], "gender_type": row[1]}
        items.append(item)
    conn.commit()
    conn.close()
    return {"items": items}


@app.put("/gender/update/{item_id}")
async def update_gender(item_id: int, item: Gender):
    conn, c = db_connection()
    c.execute("UPDATE Gender SET gender_type = ? WHERE gender_id = ?",
              (item.gender_type, item_id))
    conn.commit()
    conn.close()
    return {"item_id": item_id, "item": item}


@app.delete("/gender/delete/{item_id}")
async def delete_gender(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Gender WHERE gender_id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"item_id": item_id}
