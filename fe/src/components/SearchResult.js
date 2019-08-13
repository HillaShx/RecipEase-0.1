import React from 'react';
import '../style/MainView.css';




function SearchResult(props) {
  
  return (
    <div className="SearchResult">
      <h3>{props.recipe_details.name}</h3>
      {/* improving the display of recipes */}

    </div>
  );
};

export default SearchResult;