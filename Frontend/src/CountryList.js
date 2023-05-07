import React, { useState, useEffect } from "react";
import axios from "axios";

import { Button, Input, List, TextInput, useMantineTheme } from "@mantine/core";

function CountryList() {
  const [countries, setCountries] = useState([]);
  const [newCountryName, setNewCountryName] = useState("");
  const [deleteCountryId, setDeleteCountryId] = useState("");
  const [updateCountryNames, setUpdateCountryNames] = useState({});
  const theme = useMantineTheme();

  useEffect(() => {
    async function fetchCountries() {
      const response = await axios.get("http://localhost:8000/countries");
      setCountries(response.data.items);
    }

    fetchCountries();
  }, []);

  async function handleCreateCountry() {
    const newCountry = {
      country_id: 88,
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
    setUpdateCountryNames({
      ...updateCountryNames,
      [country.country_id]: updatedCountry.country_name,
    });
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
    <div style={{ maxWidth: 600, margin: "auto", padding: theme.spacing.xl }}>
      <h1>Country List</h1>
      <List>
        {countries.map((country) => (
          <List
            key={country.country_id}
            style={{ display: "flex", alignItems: "center" }}
          >
            <div style={{ marginRight: theme.spacing.xs }}>
              {country.country_id} - {country.country_name}
            </div>
            <TextInput
              placeholder="Update name"
              value={updateCountryNames[country.country_id] || ""}
              onChange={(e) =>
                setUpdateCountryNames({
                  ...updateCountryNames,
                  [country.country_id]: e.target.value,
                })
              }
              style={{ marginRight: theme.spacing.xs }}
            />
            <Button
              variant="outline"
              color="blue"
              onClick={() => handleUpdateCountry(country)}
            >
              Update
            </Button>
            <Button
              variant="outline"
              color="red"
              onClick={() => setDeleteCountryId(country.country_id)}
            >
              Delete
            </Button>
          </List>
        ))}
      </List>
      <div style={{ marginTop: theme.spacing.xl }}>
        <h2>Create Country</h2>
        <Input
          placeholder="Country name"
          value={newCountryName}
          onChange={(e) => setNewCountryName(e.target.value)}
          style={{ marginRight: theme.spacing.xs }}
        />
        <Button onClick={handleCreateCountry} color="blue">
          Create
        </Button>
      </div>
      <div style={{ marginTop: theme.spacing.xl }}>
        <h2>Delete Country</h2>
        <Input
          placeholder="Country ID"
          value={deleteCountryId}
          onChange={(e) => setDeleteCountryId(parseInt(e.target.value))}
          style={{ marginRight: theme.spacing.xs }}
        />
        <Button onClick={handleDeleteCountry} color="red">
          Delete
        </Button>
      </div>
    </div>
  );
}

export default CountryList;
