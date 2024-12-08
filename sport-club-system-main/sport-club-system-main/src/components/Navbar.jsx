/* eslint-disable react/prop-types */
import { Link, useLocation } from "react-router-dom";
import logo from "../assets/4843042_ball_game_play_sport_tennis_icon.png";
import { useState } from "react";
import FlowDiv from "./FlowDiv";

function Navbar() {  // {setBodyFlow}
  const [showAside, setShowAside] = useState(false);
  const currentRoute = useLocation();

  function showAsideFunction() {
    if (showAside) {
      setShowAside(false);
      // setBodyFlow(true)
    } else {
      setShowAside(true);
    }
  }

  return (
    <>
      <nav className="main-nav">
        <div
          className="left-aside"
          style={showAside === true ? { left: "0" } : { left: "-100%" }}
        >
          <div className="left-aside-header">
            <Link to="/">
              <img className="logo" src={logo} alt="Logo" />
            </Link>
            <span>Sport Club</span>
          </div>
          <ul className="nav-links">
          <li>
            <Link
              className={currentRoute.pathname === "/" ? "active-link" : null}
              to="/"
              style={
                currentRoute.pathname === "/"
                  ? {
                      backgroundColor: "rgba(238, 238, 238, 0.727)",
                      overflow: "auto",
                    }
                  : null
              }
            >
              Home
            </Link>
          </li>
          <li>
            <Link
              className={
                currentRoute.pathname === "/plans" ? "active-link" : null
              }
              to="/plans"
              style={
                currentRoute.pathname === "/plans"
                  ? {
                      backgroundColor: "rgba(238, 238, 238, 0.727)",
                      overflow: "auto",
                    }
                  : null
              }
            >
              Plans
            </Link>
          </li>
          <li>
            <Link
              className={
                currentRoute.pathname === "/about" ? "active-link" : null
              }
              to="/about"
              style={
                currentRoute.pathname === "/about"
                  ? {
                      backgroundColor: "rgba(238, 238, 238, 0.727)",
                      overflow: "auto",
                    }
                  : null
              }
            >
              About
            </Link>
          </li>
          <li>
            <Link
              className={
                currentRoute.pathname === "/contact" ? "active-link" : null
              }
              to="/contact"
              style={
                currentRoute.pathname === "/contact"
                  ? {
                      backgroundColor: "rgba(238, 238, 238, 0.727)",
                      overflow: "auto",
                    }
                  : null
              }
            >
              Contact
            </Link>
          </li>
        </ul>
        </div>
        {showAside === true ? <FlowDiv controller={setShowAside}/> :null}
        <i
          onClick={() => {
            showAsideFunction();
          }}
          className="fa-solid fa-bars"
        ></i>
        <div className="logo">
          <img src={logo} alt="Logo" />
        </div>
        <ul className="nav-links">
          <li>
            <Link
              className={currentRoute.pathname === "/" ? "active-link" : null}
              to="/"
              style={
                currentRoute.pathname === "/"
                  ? {
                      backgroundColor: "rgba(238, 238, 238, 0.727)",
                      overflow: "auto",
                    }
                  : null
              }
            >
              Home
            </Link>
          </li>
          <li>
            <Link
              className={
                currentRoute.pathname === "/plans" ? "active-link" : null
              }
              to="/plans"
              style={
                currentRoute.pathname === "/plans"
                  ? {
                      backgroundColor: "rgba(238, 238, 238, 0.727)",
                      overflow: "auto",
                    }
                  : null
              }
            >
              Plans
            </Link>
          </li>
          <li>
            <Link
              className={
                currentRoute.pathname === "/about" ? "active-link" : null
              }
              to="/about"
              style={
                currentRoute.pathname === "/about"
                  ? {
                      backgroundColor: "rgba(238, 238, 238, 0.727)",
                      overflow: "auto",
                    }
                  : null
              }
            >
              About
            </Link>
          </li>
          <li>
            <Link
              className={
                currentRoute.pathname === "/contact" ? "active-link" : null
              }
              to="/contact"
              style={
                currentRoute.pathname === "/contact"
                  ? {
                      backgroundColor: "rgba(238, 238, 238, 0.727)",
                      overflow: "auto",
                    }
                  : null
              }
            >
              Contact
            </Link>
          </li>
        </ul>
        <div className="auth-btns">
          <Link to="/login">Login</Link>
          <Link
            to="/sign-up"
            style={{ color: "white", backgroundColor: "green" }}
          >
            Sign up
          </Link>
        </div>
      </nav>
      
    </>
  );
}

export default Navbar;
