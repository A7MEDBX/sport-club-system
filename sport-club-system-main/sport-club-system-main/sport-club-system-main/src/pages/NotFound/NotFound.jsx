/* eslint-disable react/no-unescaped-entities */
import { Link } from 'react-router-dom';

const NotFound = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.header}>404 - Page Not Found</h1>
      <p style={styles.message}>
        Oops! The page you're looking for doesn't exist.
      </p>
      <Link to="/" style={styles.link}>
        Go back to Home
      </Link>
    </div>
  );
};

const styles = {
  container: {
    textAlign: 'center',
    marginTop: '10%',
    color: '#333',
    fontFamily: 'Arial, sans-serif',
  },
  header: {
    fontSize: '3rem',
    color: '#007f00', // Adjust to your green theme
  },
  message: {
    fontSize: '1.5rem',
    margin: '20px 0',
  },
  link: {
    fontSize: '1.2rem',
    color: '#007f00',
    textDecoration: 'underline',
    cursor: 'pointer',
  },
};

export default NotFound;
