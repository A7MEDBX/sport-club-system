import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";
import Cookies from "js-cookie";


function Login() {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate(); // For navigation after successful login

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!userName || !password) {
      setErrorMessage("Both fields are required.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username: userName, Password: password }),
        credentials: "include", 
      });
      

      const result = await response.json();

      if (response.ok) {
        const { Member_ID, Member_Name, Member_Role } = result.data;

        // Store user data in cookies
        Cookies.set("member_id", Member_ID, { expires: 7 });
        Cookies.set("member_name", Member_Name, { expires: 7 });
        Cookies.set("member_role", Member_Role, { expires: 7 });

        alert("Login Successful");
        navigate("/dashboard"); // Redirect to dashboard or another page
      } else {
        setErrorMessage(result.message || "Login failed.");
      }
    } catch (error) {
      console.error("Error:", error);
      setErrorMessage("An error occurred. Please try again.");
    }
  };

  return (
    <>
      <Navbar />
      <form onSubmit={handleSubmit} className="login-form">
        <h2>Login</h2>

        {errorMessage && <div className="login-error-message">{errorMessage}</div>}

        <div className="login-input-container">
          <input
            type="text"
            id="login-username"
            className={`login-input ${userName ? "not-empty" : ""}`}
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
            required
          />
          <label htmlFor="login-username" className="login-label">
            Email
          </label>
        </div>

        <div className="login-input-container">
          <input
            type={showPassword ? "text" : "password"}
            id="login-password"
            className={`login-input ${password ? "not-empty" : ""}`}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <label htmlFor="login-password" className="login-label">
            Password
          </label>
          <i
            className={`fa-regular ${showPassword ? "fa-eye-slash" : "fa-eye"}`}
            onClick={() => setShowPassword((prev) => !prev)}
            style={{
              position: "absolute",
              right: "10px",
              top: "15px",
              cursor: "pointer",
            }}
          />
        </div>

        <div>
          <input type="submit" value="Login" className="login-submit" />
        </div>

        <div className="login-links">
          <Link to="/sign-up">Register</Link>
          <Link to="/reset-password">Forgot Password</Link>
        </div>
      </form>
      <Footer />
    </>
  );
}

export default Login;
