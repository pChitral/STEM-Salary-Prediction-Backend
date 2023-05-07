import { useEffect, useState } from "react";
import axios from "axios";

function GenderList() {
  const [genders, setGenders] = useState([]);

  useEffect(() => {
    async function fetchGenders() {
      const response = await axios.get("http://localhost:8000/genders/");
      setGenders(response.data.items);
    }

    fetchGenders();
  }, []);

  return (
    <div>
      <h1>Gender List</h1>
      <ul>
        {genders.map((gender) => (
          <li key={gender.gender_id}>
            {gender.gender_id} - {gender.gender_type}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default GenderList;
