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
    close_db_connection(conn)
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
    close_db_connection(conn)
    return {"item_id": item_id, "item": item}


@app.delete("/race/delete/{item_id}")
async def delete_race(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Race WHERE race_id = ?", (item_id,))
    close_db_connection(conn)
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
    close_db_connection(conn)
    return {"item": item}


@app.get("/educations/")
async def read_educations():
    conn, c = db_connection()
    c.execute("SELECT * FROM Education")
    items = []
    for row in c.fetchall():
        item = {"edu_id": row[0],  "edu_name": row[1]}
        items.append(item)
    close_db_connection(conn)
    return {"items": items}


@app.put("/education/update/{item_id}")
async def update_education(item_id: int, item: EducationItem):
    conn, c = db_connection()
    c.execute("UPDATE Education SET edu_name = ? WHERE edu_id = ?",
              (item.edu_name, item_id))
    close_db_connection(conn)
    return {"item_id": item_id, "item": item}


@app.delete("/education/delete/{item_id}")
async def delete_education(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Education WHERE edu_id = ?", (item_id,))
    close_db_connection(conn)
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
    close_db_connection(conn)
    return {"item": city_item}


@app.get("/cities/")
async def read_cities():
    conn, c = db_connection()
    c.execute("SELECT * FROM City")
    items = []
    for row in c.fetchall():
        item = {"city_id": row[0],  "city_name": row[1]}
        items.append(item)
    close_db_connection(conn)
    return {"items": items}


@app.put("/city/update/{item_id}")
async def update_city(item_id: int, city_item: CityItem):
    conn, c = db_connection()
    c.execute("UPDATE City SET city_name = ? WHERE city_id = ?",
              (city_item.city_name, item_id))
    close_db_connection(conn)
    return {"item_id": item_id, "item": city_item}


@app.delete("/city/delete/{item_id}")
async def delete_city(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM City WHERE city_id = ?", (item_id,))
    close_db_connection(conn)
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
    close_db_connection(conn)
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
    close_db_connection(conn)
    return {"items": items}


# Update a company by company_id
@app.put("/company/update/{company_id}")
async def update_company(company_id: int, item: CompanyItem):
    conn, c = db_connection()
    c.execute("UPDATE Company SET company_name = ? WHERE company_id = ?",
              (item.company_name, company_id))
    close_db_connection(conn)
    return {"company_id": company_id, "item": item}


# Delete a company by company_id
@app.delete("/company/delete/{company_id}")
async def delete_company(company_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Company WHERE company_id = ?", (company_id,))
    close_db_connection(conn)
    return {"company_id": company_id}


# Tag CRUD

class Tag(BaseModel):
    tag_str: int
    tag_name: str


@app.post("/tag/create")
async def create_tag(item: Tag):
    conn, c = db_connection()
    c.execute("INSERT INTO Tag (tag_str, tag_name) VALUES (?, ?)",
              (item.tag_str_str, item.tag_str_name))
    close_db_connection(conn)
    return {"item": item}


@app.get("/tags/")
async def read_tags():
    conn, c = db_connection()
    c.execute("SELECT * FROM Tag")
    items = []
    for row in c.fetchall():
        item = {"tag_str": row[0],  "tag_name": row[1]}
        items.append(item)
    close_db_connection(conn)
    return {"items": items}


@app.put("/tag/update/{item_id}")
async def update_tag(item_id: int, item: Tag):
    conn, c = db_connection()
    c.execute("UPDATE Tag SET tag_name = ? WHERE tag_str = ?",
              (item.tag_str_name, item_id))
    close_db_connection(conn)
    return {"item_id": item_id, "item": item}


@app.delete("/tag/delete/{item_id}")
async def delete_tag(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Tag WHERE tag_str = ?", (item_id,))
    close_db_connection(conn)
    return {"item_id": item_id}

# TITLE CRUD


class Title(BaseModel):
    title_str: int
    title_name: str


@app.post("/title/create")
async def create_title(item: Title):
    conn, c = db_connection()
    c.execute("INSERT INTO Title (title_str, title_name) VALUES (?, ?)",
              (item.title_str_str, item.title_str_name))
    close_db_connection(conn)
    return {"item": item}


@app.get("/titles/")
async def read_titles():
    conn, c = db_connection()
    c.execute("SELECT * FROM Title")
    items = []
    for row in c.fetchall():
        item = {"title_str": row[0],  "title_name": row[1]}
        items.append(item)
    close_db_connection(conn)
    return {"items": items}


@app.put("/title/update/{item_id}")
async def update_title(item_id: int, item: Title):
    conn, c = db_connection()
    c.execute("UPDATE Title SET title_name = ? WHERE title_str = ?",
              (item.title_str_name, item_id))
    close_db_connection(conn)
    return {"item_id": item_id, "item": item}


@app.delete("/title/delete/{item_id}")
async def delete_title(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Title WHERE title_str = ?", (item_id,))
    close_db_connection(conn)
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
    close_db_connection(conn)
    return {"item": item}


@app.get("/states/")
async def read_states():
    conn, c = db_connection()
    c.execute("SELECT * FROM State")
    items = []
    for row in c.fetchall():
        item = {"state_id": row[0],  "state_name": row[1]}
        items.append(item)
    close_db_connection(conn)
    return {"items": items}


@app.put("/state/update/{item_id}")
async def update_state(item_id: int, item: State):
    conn, c = db_connection()
    c.execute("UPDATE State SET state_name = ? WHERE state_id = ?",
              (item.state_name, item_id))
    close_db_connection(conn)
    return {"item_id": item_id, "item": item}


@app.delete("/state/delete/{item_id}")
async def delete_state(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM State WHERE state_id = ?", (item_id,))
    close_db_connection(conn)
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
    close_db_connection(conn)
    return {"item": item}


@app.get("/countries/")
async def read_countries():
    conn, c = db_connection()
    c.execute("SELECT * FROM Country")
    items = []
    for row in c.fetchall():
        item = {"country_id": row[0], "country_name": row[1]}
        items.append(item)
    close_db_connection(conn)
    return {"items": items}


@app.put("/country/update/{item_id}")
async def update_country(item_id: int, item: Country):
    conn, c = db_connection()
    c.execute("UPDATE Country SET country_name = ? WHERE country_id = ?",
              (item.country_name, item_id))
    close_db_connection(conn)
    return {"item_id": item_id, "item": item}


@app.delete("/country/delete/{item_id}")
async def delete_country(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Country WHERE country_id = ?", (item_id,))
    close_db_connection(conn)
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
    close_db_connection(conn)
    return {"item": item}


@app.get("/genders/")
async def read_genders():
    conn, c = db_connection()
    c.execute("SELECT * FROM Gender")
    items = []
    for row in c.fetchall():
        item = {"gender_id": row[0], "gender_type": row[1]}
        items.append(item)
    close_db_connection(conn)
    return {"items": items}


@app.put("/gender/update/{item_id}")
async def update_gender(item_id: int, item: Gender):
    conn, c = db_connection()
    c.execute("UPDATE Gender SET gender_type = ? WHERE gender_id = ?",
              (item.gender_type, item_id))
    close_db_connection(conn)
    return {"item_id": item_id, "item": item}


@app.delete("/gender/delete/{item_id}")
async def delete_gender(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Gender WHERE gender_id = ?", (item_id,))
    close_db_connection(conn)
    return {"item_id": item_id}

# EMPLOYEE CRUD


class Employee(BaseModel):
    emp_id: int
    timestamp: str
    company_id: int
    level_id: int
    title_str: str
    total_yearly_compensation: int
    location_str: str
    years_of_experience: int
    years_at_company: int
    tag_str: str
    base_salary: float
    stock_grant_value: float
    bonus: float
    gender: str
    race: str
    education: str


@app.post("/employee/create")
async def create_employee(item: Employee):
    conn, c = db_connection()
    gender_id = gender_lookup[item.gender.lower()]
    race_id = race_lookup[item.race.lower()]
    edu_id = edu_lookup[item.education.lower()]
    
    # Call Location Database
    location_str = location_lookup[item.location_str.lower()]
    title_str = title_lookup[item.title_str.lower()]
    tag_str = tag_lookup[item.tag_str.lower()]
    c.execute("INSERT INTO Employee (emp_id, timestamp, company_id, level_id, title_str, total_yearly_compensation, location_str, years_of_experience, years_at_company, tag_str, base_salary, stock_grant_value, bonus, gender_id, race_id, edu_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (item.emp_id,
               item.timestamp,
               item.company_id,
               item.level_id,
               title_str,
               item.total_yearly_compensation,
               location_str,
               item.years_of_experience,
               item.years_at_company,
               tag_str,
               item.base_salary,
               item.stock_grant_value,
               item.bonus,
               gender_id,
               race_id,
               edu_id))
    close_db_connection(conn)
    return {"item": item}


@app.get("/employees/")
async def read_employees():
    conn, c = db_connection()
    c.execute("SELECT * FROM Employee LIMIT 5")
    items = []
    for row in c.fetchall():
        item = {"emp_id": row[0], "timestamp": row[1], "company_id": row[2], "level_id": row[3], "title_str": row[4], "total_yearly_compensation": row[5], "location_str": row[6], "years_of_experience": row[7],
                "years_at_company": row[8], "tag_str": row[9], "base_salary": row[10], "stock_grant_value": row[11], "bonus": row[12], "gender_id": row[13], "race_id": row[14], "edu_id": row[15]}
        items.append(item)
    close_db_connection(conn)
    return {"items": items}


@app.put("/employee/update/{item_id}")
async def update_employee(item_id: int, item: Employee):
    conn, c = db_connection()
    c.execute("UPDATE Employee SET timestamp = ?, company_id = ?, level_id = ?, title_str = ?, total_yearly_compensation = ?, location_str = ?, years_of_experience = ?, years_at_company = ?, tag_str = ?, base_salary = ?, stock_grant_value = ?, bonus = ?, gender_id = ?, race_id = ?, edu_id = ? WHERE emp_id = ?",
              (item.timestamp, item.company_id, item.level_id, item.title_str_str, item.total_yearly_compensation, item.location_str_str, item.years_of_experience, item.years_at_company, item.tag_str_str, item.base_salary, item.stock_grant_value, item.bonus, item.gender_id, item.race_id, item.edu_id, item_id))
    close_db_connection(conn)
    return {"item_id": item_id, "item": item}


@app.delete("/employee/delete/{item_id}")
async def delete_employee(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Employee WHERE emp_id = ?", (item_id,))
    close_db_connection(conn)
    return {"item_id": item_id}

# LOCATION CRUD

class Location(BaseModel):
    location_id: int
    city_id: int
    state_id: int
    country_id: int


@app.post("/location/create")
async def create_location(item: Location):
    conn, c = db_connection()
    c.execute("INSERT INTO Location (location_id, city_id, state_id, country_id) VALUES (?, ?, ?, ?)",
              (item.location_id, item.city_id, item.state_id, item.country_id))
    close_db_connection(conn)
    return {"item": item}


@app.get("/locations/")
async def read_locations():
    conn, c = db_connection()
    c.execute("SELECT * FROM Location")
    items = []
    for row in c.fetchall():
        item = {"location_id": row[0], "city_id": row[1],
                "state_id": row[2], "country_id": row[3]}
        items.append(item)
    close_db_connection(conn)
    return {"items": items}


@app.put("/location/update/{item_id}")
async def update_location(item_id: int, item: Location):
    conn, c = db_connection()
    c.execute("UPDATE Location SET city_id = ?, state_id = ?, country_id = ? WHERE location_id = ?",
              (item.city_id, item.state_id, item.country_id, item_id))
    close_db_connection(conn)
    return {"item_id": item_id, "item": item}


@app.delete("/location/delete/{item_id}")
async def delete_location(item_id: int):
    conn, c = db_connection()
    c.execute("DELETE FROM Location WHERE location_id = ?", (item_id,))
    close_db_connection(conn)
    return {"item_id": item_id}
