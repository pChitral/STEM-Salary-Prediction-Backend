import React, { useState, useEffect } from "react";
import axios from "axios";
import { Button, Input, List, TextInput, useMantineTheme } from "@mantine/core";

function CityList() {
  const [genders, setCities] = useState([]);
  const [newCityName, setNewCityName] = useState("");
  const [deleteCityId, setDeleteCityId] = useState("");
  const [updateCityNames, setUpdateCityNames] = useState({});
  const theme = useMantineTheme();

  useEffect(() => {
    async function fetchCities() {
      const response = await axios.get("http://http://3.95.169.32:8000/genders");
      setCities(response.data.items);
    }
    fetchCities();
  }, []);

  async function handleCreateCity() {
    const newCity = {
      gender_id: 123,
      gender_type: newCityName,
    };
    const response = await axios.post(
      "http://localhost:8000/gender/create",
      newCity
    );
    setCities([...genders, response.data]);
    setNewCityName("");
  }

  async function handleUpdateCity(gender) {
    const updatedCity = {
      gender_id: gender.gender_id,
      gender_type: updateCityNames[gender.gender_id],
    };
    await axios.put(
      `http://localhost:8000/gender/update/${gender.gender_id}`,
      updatedCity
    );
    const updatedCities = genders.map((c) =>
      c.gender_id === gender.gender_id ? updatedCity : c
    );
    setCities(updatedCities);
    setUpdateCityNames({
      ...updateCityNames,
      [gender.gender_id]: updatedCity.gender_type,
    });
  }

  async function handleDeleteCity() {
    await axios.delete(`http://localhost:8000/gender/delete/${deleteCityId}`);
    const updatedCities = genders.filter((c) => c.gender_id !== deleteCityId);
    setCities(updatedCities);
    setDeleteCityId("");
  }

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: theme.spacing.xl }}>
      <h1>Gender List</h1>
      <List>
        {genders.map((gender) => (
          <List
            key={gender.gender_id}
            style={{ display: "flex", alignItems: "center" }}
          >
            <div style={{ marginRight: theme.spacing.xs }}>
              {gender.gender_id} - {gender.gender_type}
            </div>
            <TextInput
              placeholder="Update name"
              value={updateCityNames[gender.gender_id] || ""}
              onChange={(e) =>
                setUpdateCityNames({
                  ...updateCityNames,
                  [gender.gender_id]: e.target.value,
                })
              }
              style={{ marginRight: theme.spacing.xs }}
            />
            <Button
              variant="outline"
              color="blue"
              onClick={() => handleUpdateCity(gender)}
            >
              Update
            </Button>
            <Button
              variant="outline"
              color="red"
              onClick={() => setDeleteCityId(gender.gender_id)}
            >
              Delete
            </Button>
          </List>
        ))}
      </List>
      <div style={{ marginTop: theme.spacing.xl }}>
        <h2>Create Gender</h2>
        <Input
          placeholder="Gender Type"
          value={newCityName}
          onChange={(e) => setNewCityName(e.target.value)}
          style={{ marginRight: theme.spacing.xs }}
        />
        <Button onClick={handleCreateCity} color="blue">
          Create
        </Button>
      </div>
      <div style={{ marginTop: theme.spacing.xl }}>
        <h2>Delete Gender</h2>
        <Input
          placeholder="Gender ID"
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
