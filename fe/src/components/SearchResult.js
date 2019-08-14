import React, { useEffect } from 'react';
import '../style/SearchResult.css';

function SearchResult(props) {
  
  return (
    <div className="SearchResult">
      <img className="img" src={"media/" + props.recipe.img} alt={props.recipe.name}></img>
      <h3 class="title">{props.recipe.name}</h3>
      {/* improving the display of recipes */}
    </div>
  );
};

export default SearchResult;