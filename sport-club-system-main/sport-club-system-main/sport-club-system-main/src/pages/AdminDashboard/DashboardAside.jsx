/* eslint-disable react/prop-types */
import { LuPanelLeftClose } from "react-icons/lu";
import { Link, useLocation } from "react-router-dom";
import logo from "../../assets/4843042_ball_game_play_sport_tennis_icon.png";
import "./admin-dashboard.css";
import { useEffect } from "react";

function DashboardAside({ asideShow, setAsideShow }) {
  const location = useLocation();
  useEffect(() => {
    function calculatePageWidth() {
      const func_width = window.innerWidth;
      if (func_width > 1100) {
        setAsideShow(true);
      } else {
        setAsideShow(false);
      }
      window.addEventListener("resize", calculatePageWidth);
    }
    calculatePageWidth();
  }, [setAsideShow]);

  return (
    <aside
      className="admin-dashboard-aside"
      style={asideShow ? { left: "0" } : { left: "-100%" }}
    >
      <div className="admin-aside-header">
        <LuPanelLeftClose
          className="aside-header-close-icon"
          onClick={() => setAsideShow(false)}
        />
        <img src={logo} alt="Logo" />
        <h2>Sport Club System</h2>
      </div>
      <ul>
        <li
          style={
            location.pathname === "/admin-dashboard/overview"
              ? { backgroundColor: "#4CAF50" }
              : null
          }
        >
          <Link to="/admin-dashboard/overview">Overview</Link>
        </li>
        <li
          style={
            location.pathname === "/admin-dashboard/events"
              ? { backgroundColor: "#4CAF50" }
              : null
          }
        >
          <Link to="/admin-dashboard/events">Events</Link>
        </li>
        <li
          style={
            location.pathname === "/admin-dashboard/members"
              ? { backgroundColor: "#4CAF50" }
              : null
          }
        >
          <Link to="/admin-dashboard/members">Members</Link>
        </li>
        <li
          style={
            location.pathname === "/admin-dashboard/subscriptions"
              ? { backgroundColor: "#4CAF50" }
              : null
          }
        >
          <Link to="/admin-dashboard/subscriptions">Subscriptions</Link>
        </li>
        <li
          style={
            location.pathname === "/admin-dashboard/teams"
              ? { backgroundColor: "#4CAF50" }
              : null
          }
        >
          <Link to="/admin-dashboard/teams">Teams</Link>
        </li>
      </ul>
      <p className="dashboard-version">Version: 1.0.0</p>
    </aside>
  );
}

export default DashboardAside;
