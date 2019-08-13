import React, { useState, useEffect } from 'react';
import './style/App.css';
import Navbar from './components/Navbar'
import * as api from "./utils/recipesAPI"
import MainView from './components/MainView'

function App() {
  const [recipes, setRecipes] = useState([]);
  
  useEffect(()=>{
    api.getRecipes(recipes =>
    setRecipes(recipes["results"]),
    error => console.log(error)
    )
  },[])

  function handleClickForSearch(query) {
    api.getFilteredRecipes(query, recipes => 
      setRecipes(recipes["results"]),
      error => console.log(error)
  )}

  return (
    <div className="App">
      <Navbar handleSearch={handleClickForSearch}/>
      <MainView recipes={recipes} />
    </div>
  );
};

export default App;
