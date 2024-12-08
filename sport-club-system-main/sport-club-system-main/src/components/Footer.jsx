
const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-about">
          <h3>About Our Club</h3>
          <p>We are a community-driven sports club offering various activities and training. Join us to stay active and healthy!</p>
        </div>
        <div className="footer-links">
          <h3>Membership</h3>
          <ul>
            <li><a href="#membership">Become a Member</a></li>
            <li><a href="#classes">Our Classes</a></li>
            <li><a href="#events">Upcoming Events</a></li>
          </ul>
        </div>
        <div className="footer-contact">
          <h3>Contact Us</h3>
          <ul>
            <li>Email: <a href="mailto:contact@sportclub.com">contact@sportclub.com</a></li>
            <li>Phone: <a href="tel:+123456789">+1 234 567 89</a></li>
          </ul>
        </div>
        {/* <div className="footer-social">
          <h3>Follow Us</h3>
          <ul>
            <li><a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a></li>
            <li><a href="https://facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a></li>
            <li><a href="https://instagram.com" target="_blank" rel="noopener noreferrer">Instagram</a></li>
            <li><a href="https://linkedin.com" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
          </ul>
        </div> */}
      </div>
      <div className="footer-bottom">
        <p>&copy; 2024 SportClub. All Rights Reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
