import React from 'react';
import '../style/UserMenu.css'

function UserMenu() {
  return (
    <div className="UserMenu">
      <div className="usermenu-butn">Hi username!</div>
      <div className="usermenu-box collapsed">
        <ul>
          <li>my profile</li>
          <li>my cookbook</li>
        </ul>
      </div>
    </div>
  );
};

export default UserMenu;