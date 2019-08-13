import $ from 'jquery';
import React from 'react';
import '../style/Navbar.css';
import logo from '../img/navbar-logo.png'
import UserMenu from './UserMenu'

function Navbar(props) {

  function handleClickForSearch() {
    let query = $("input[name='query']").val()
    props.handleSearch(query);
  }

  return (
    <div className="Navbar">
      <img id="navbar-logo" src={logo} alt="" />
      <input type="text" name="query" id="search-bar" />
      <div onClick={handleClickForSearch} className="search-butn butn">search</div>
      <UserMenu />
    </div>
  );
};

export default Navbar;