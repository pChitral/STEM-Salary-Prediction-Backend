import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import GenderList from "./GenderList";
import CountryList from "./CountryList";

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<GenderList />} />
        <Route path="/countries" element={<CountryList />} />
      </Routes>
    </Router>
  );
}

export default App;
