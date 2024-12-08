import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";
import "./about.css";

function AboutUs() {
  return (
    <>
      <Navbar />
      <div className="about-container">
        <section className="about-hero">
          <h1 className="about-title">About Our Club</h1>
          <p className="about-subtitle">
            Where passion meets performance, and community builds champions.
          </p>
        </section>

        <section className="about-content">
          <div className="about-section">
            <h2 className="about-heading">Our Mission</h2>
            <p className="about-text">
              Our mission is to provide a state-of-the-art platform for managing
              and enhancing the experience of our sport club members. We strive
              to empower athletes, teams, and fitness enthusiasts by fostering a
              sense of community and achievement.
            </p>
          </div>

          <div className="about-section">
            <h2 className="about-heading">Who We Are</h2>
            <p className="about-text">
              Founded on the principles of teamwork, health, and excellence, we
              are a dedicated team of professionals passionate about helping our
              members achieve their goals. Whether you’re a seasoned athlete or
              just starting your fitness journey, we have the tools and
              resources to support you every step of the way.
            </p>
          </div>

          <div className="about-section">
            <h2 className="about-heading">Why Choose Us</h2>
            <ul className="about-list">
              <li>
                <span className="check-icon">✔</span> Comprehensive member
                management tools.
              </li>
              <li>
                <span className="check-icon">✔</span> A tailored experience for
                clubs, teams, and individual users.
              </li>
              <li>
                <span className="check-icon">✔</span> Streamlined subscription
                systems for easy access to premium features.
              </li>
              <li>
                <span className="check-icon">✔</span> Secure and user-friendly
                platform.
              </li>
              <li>
                <span className="check-icon">✔</span> A vibrant community of
                like-minded individuals.
              </li>
            </ul>
          </div>
        </section>

        <section className="about-stats">
          <h2 className="about-heading">Our Impact</h2>
          <div className="stats-grid">
            <div className="stat-card">
              <h3 className="stat-number">10K+</h3>
              <p className="stat-description">Members Served</p>
            </div>
            <div className="stat-card">
              <h3 className="stat-number">500+</h3>
              <p className="stat-description">Clubs Managed</p>
            </div>
            <div className="stat-card">
              <h3 className="stat-number">5 Years</h3>
              <p className="stat-description">Of Excellence</p>
            </div>
          </div>
        </section>
      </div>
      <Footer />
    </>
  );
}

export default AboutUs;
