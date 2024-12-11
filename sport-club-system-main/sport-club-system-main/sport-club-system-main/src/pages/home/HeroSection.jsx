/* eslint-disable react/no-unescaped-entities */
import { Link } from "react-router-dom";
import "./home.css";

function HeroSection() {
  return (
    <section className="hero-container">
      <div className="hero-content">
        <h1 className="hero-title">JOIN OUR CLUB,</h1>
        <h2 className="hero-subtitle">ACHIEVE YOUR FITNESS GOALS</h2>
        <p className="hero-description">
          Take the first step towards a healthier, more active lifestyle. Our
          sport club system offers personalized training programs, access to
          state-of-the-art facilities, and exclusive member perks. Whether
          you're a beginner or an experienced athlete, we have everything you
          need to excel. Start your journey with us today!
        </p>
        <div className="hero-buttons">
          <Link to="/login" className="hero-button hero-login">
            Login
          </Link>
          <Link to="/sign-up" className="hero-button hero-sign-up">
            Sign Up
          </Link>
        </div>
      </div>
    </section>
  );
}

export default HeroSection;
