import { useState, useEffect } from "react";
import axios from "axios";

function CountryList() {
  const [countries, setCountries] = useState([]);
  const [newCountryName, setNewCountryName] = useState("");
  const [deleteCountryId, setDeleteCountryId] = useState("");
  const [updateCountryNames, setUpdateCountryNames] = useState({});

  useEffect(() => {
    async function fetchCountries() {
      const response = await axios.get("http://localhost:8000/countries");
      setCountries(response.data.items);
    }

    fetchCountries();
  }, []);

  async function handleCreateCountry() {
    const newCountry = {
      country_name: newCountryName,
    };
    const response = await axios.post(
      "http://localhost:8000/country/create",
      newCountry
    );
    setCountries([...countries, response.data]);
    setNewCountryName("");
  }

  async function handleUpdateCountry(country) {
    const updatedCountry = {
      country_id: country.country_id,
      country_name: updateCountryNames[country.country_id],
    };
    await axios.put(
      `http://localhost:8000/country/update/${country.country_id}`,
      updatedCountry
    );
    const updatedCountries = countries.map((c) =>
      c.country_id === country.country_id ? updatedCountry : c
    );
    setCountries(updatedCountries);
  }

  async function handleDeleteCountry() {
    await axios.delete(
      `http://localhost:8000/country/delete/${deleteCountryId}`
    );
    const updatedCountries = countries.filter(
      (c) => c.country_id !== deleteCountryId
    );
    setCountries(updatedCountries);
    setDeleteCountryId("");
  }

  return (
    <div>
      <h1>Country List</h1>
      <ul>
        {countries.map((country) => (
          <li key={country.country_id}>
            {country.country_id} - {country.country_name}
            <input
              type="text"
              value={updateCountryNames[country.country_id] || ""}
              onChange={(e) =>
                setUpdateCountryNames({
                  ...updateCountryNames,
                  [country.country_id]: e.target.value,
                })
              }
            />
            <button onClick={() => handleUpdateCountry(country)}>Update</button>
            <button onClick={() => setDeleteCountryId(country.country_id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
      <div>
        <h2>Create Country</h2>
        <input
          type="text"
          placeholder="Country name"
          value={newCountryName}
          onChange={(e) => setNewCountryName(e.target.value)}
        />
        <button onClick={handleCreateCountry}>Create</button>
      </div>
      <div>
        <h2>Delete Country</h2>
        <input
          type="text"
          placeholder="Country ID"
          value={deleteCountryId}
          onChange={(e) => setDeleteCountryId(parseInt(e.target.value))}
        />
        <button onClick={handleDeleteCountry}>Delete</button>
      </div>
    </div>
  );
}

export default CountryList;
