import React from 'react';
import '../style/MainView.css';
import SearchResult from './SearchResult'





function MainView(props) {
  
  console.log(props)

  return (
    <div className="MainView">
      <ul>
        {props.recipes.map(recipe => (
        <SearchResult name={recipe.name} />
        ))}
      </ul>
    </div>
  );
};

export default MainView;