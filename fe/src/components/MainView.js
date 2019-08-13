import React, { useState, useEffect } from 'react';
import '../style/MainView.css';
import SearchResult from './SearchResult'




function MainView(props) {
  const [recipes, setRecipes] = useState([]);
  
  useEffect(()=>{
    setRecipes(props.recipes)
  },[props])

  if (recipes.length) {
    return (
      <div className="MainView">
        <ul>
          {recipes.map(recipe => (
            <SearchResult name={recipe.name} />
          ))}
        </ul>
      </div>
    );
  } else {
    return (
      <div className="MainView">
        <ul>
          No recipes matched you search! :(
        </ul>
      </div>
    );
  }
  
};

export default MainView;