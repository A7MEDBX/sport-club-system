/* eslint-disable react/prop-types */
import { useState } from "react";
import { FiMenu, FiUser, FiLogOut, FiSettings } from "react-icons/fi";
import logo from "../../assets/4843042_ball_game_play_sport_tennis_icon.png";
import "./admin-dashboard.css";

function DashboardNav({ adminName = "Admin", setAsideShow, asideShow }) {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    if (!isDropdownOpen) {
      document.querySelector(".profile-section").style.backgroundColor =
        "#d8d8d83d";
    } else {
      document.querySelector(".profile-section").style.backgroundColor =
        "transparent";
    }
    setIsDropdownOpen(!isDropdownOpen);
  };

  function onToggleSidebar() {
    if (asideShow) {
      setAsideShow(false);
    } else {
      setAsideShow(true);
    }
  }

  return (
    <nav className="dashboard-nav">
      <div className="nav-left">
        <button className="menu-toggle" onClick={onToggleSidebar}>
          <FiMenu size={24} />
        </button>
        <img className="logo" src={logo} alt="Logo"></img>
      </div>
      <div className="nav-right">
        <div className="profile-section" onClick={toggleDropdown}>
          <span>Hi, </span>
          <span className="admin-name">{adminName}</span>
        </div>
        <div className="dropdown">
          {isDropdownOpen && (
            <div className="dropdown-menu">
              <a href="/profile" className="dropdown-item">
                <FiUser /> Profile
              </a>
              <a href="/settings" className="dropdown-item">
                <FiSettings /> Settings
              </a>
              <button className="dropdown-item logout">
                <FiLogOut /> Logout
              </button>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}

export default DashboardNav;
