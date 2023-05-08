import React, { useState, useEffect } from "react";
import axios from "axios";
import { Button, Input, List, TextInput, useMantineTheme } from "@mantine/core";

function CityList() {
  const [cities, setCities] = useState([]);
  const [newCityName, setNewCityName] = useState("");
  const [deleteCityId, setDeleteCityId] = useState("");
  const [updateCityNames, setUpdateCityNames] = useState({});
  const theme = useMantineTheme();

  useEffect(() => {
    async function fetchCities() {
      const response = await axios.get("http://http://3.95.169.32:8000/cities");
      setCities(response.data.items);
    }
    fetchCities();
  }, []);

  async function handleCreateCity() {
    const newCity = {
      city_id: 123,
      city_name: newCityName,
    };
    const response = await axios.post(
      "http://localhost:8000/city/create",
      newCity
    );
    setCities([...cities, response.data]);
    setNewCityName("");
  }

  async function handleUpdateCity(city) {
    const updatedCity = {
      city_id: city.city_id,
      city_name: updateCityNames[city.city_id],
    };
    await axios.put(
      `http://localhost:8000/city/update/${city.city_id}`,
      updatedCity
    );
    const updatedCities = cities.map((c) =>
      c.city_id === city.city_id ? updatedCity : c
    );
    setCities(updatedCities);
    setUpdateCityNames({
      ...updateCityNames,
      [city.city_id]: updatedCity.city_name,
    });
  }

  async function handleDeleteCity() {
    await axios.delete(`http://localhost:8000/city/delete/${deleteCityId}`);
    const updatedCities = cities.filter((c) => c.city_id !== deleteCityId);
    setCities(updatedCities);
    setDeleteCityId("");
  }

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: theme.spacing.xl }}>
      <h1>City List</h1>
      <List>
        {cities.map((city) => (
          <List
            key={city.city_id}
            style={{ display: "flex", alignItems: "center" }}
          >
            <div style={{ marginRight: theme.spacing.xs }}>
              {city.city_id} - {city.city_name}
            </div>
            <TextInput
              placeholder="Update name"
              value={updateCityNames[city.city_id] || ""}
              onChange={(e) =>
                setUpdateCityNames({
                  ...updateCityNames,
                  [city.city_id]: e.target.value,
                })
              }
              style={{ marginRight: theme.spacing.xs }}
            />
            <Button
              variant="outline"
              color="blue"
              onClick={() => handleUpdateCity(city)}
            >
              Update
            </Button>
            <Button
              variant="outline"
              color="red"
              onClick={() => setDeleteCityId(city.city_id)}
            >
              Delete
            </Button>
          </List>
        ))}
      </List>
      <div style={{ marginTop: theme.spacing.xl }}>
        <h2>Create City</h2>
        <Input
          placeholder="City name"
          value={newCityName}
          onChange={(e) => setNewCityName(e.target.value)}
          style={{ marginRight: theme.spacing.xs }}
        />
        <Button onClick={handleCreateCity} color="blue">
          Create
        </Button>
      </div>
      <div style={{ marginTop: theme.spacing.xl }}>
        <h2>Delete City</h2>
        <Input
          placeholder="City ID"
          value={deleteCityId}
          onChange={(e) => setDeleteCityId(parseInt(e.target.value))}
          style={{ marginRight: theme.spacing.xs }}
        />
        <Button onClick={handleDeleteCity} color="red">
          Delete
        </Button>
      </div>
    </div>
  );
}

export default CityList;
