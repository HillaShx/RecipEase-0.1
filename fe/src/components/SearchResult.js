import React from 'react';
import '../style/MainView.css';




function SearchResult(props) {
  
  return (
    <div className="SearchResult">
      <h3>{props.name}</h3>        
    </div>
  );
};

export default SearchResult;