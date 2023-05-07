import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import GenderList from "./GenderList";
import CountryList from "./CountryList";
import CityList from "./CityList";

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/genders" element={<GenderList />} />
        <Route path="/countries" element={<CountryList />} />
        <Route path="/cities" element={<CityList />} />
      </Routes>
    </Router>
  );
}

export default App;
