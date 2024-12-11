import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";

function SignUp() {
  const [userName, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [number, setNumber] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [otpCode, setOtpCode] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [isOtpSent, setIsOtpSent] = useState(false);
  const [otpVerified, setOtpVerified] = useState(false);
  const [loading, setLoading] = useState(false); // Added loading state

  const validateUserName = (value) =>
    value.length < 7 ? "Username should be at least 7 characters long" : null;

  const validatePassword = (value) =>
    value.length < 6 ? "Password should be at least 6 characters long" : null;

  const validateConfirmPassword = (value) =>
    password !== value ? "Passwords do not match" : null;

  const validateEmail = (value) =>
    /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(value)
      ? null
      : "Invalid email address";

  const validateNumber = (value) =>
    value.length < 10 || isNaN(value) ? "Invalid phone number" : null;

  const handleChange =
    (setter, validator = null) =>
    (e) => {
      const value = e.target.value;
      setter(value);
      if (validator) {
        const error = validator(value);
        setErrorMessage(error || "");
      }
    };

  const handleOtpRequest = async () => {
    try {
      if (!email) {
        setErrorMessage("Email is required to send OTP.");
        return;
      }

      setLoading(true); // Show loading spinner
      const response = await axios.post("http://localhost:5000/api/request-otp", {
        email,
      });

      if (response.data.status === "Success") {
        setSuccessMessage("OTP sent to your email.");
        setIsOtpSent(true);
      } else {
        setErrorMessage(response.data.message);
      }
    } catch (error) {
      console.error("Error during OTP request:", error);
      setErrorMessage("Failed to send OTP. Please try again.");
    } finally {
      setLoading(false); // Hide loading spinner
    }
  };

  const handleOtpVerification = async () => {
    try {
      if (!otpCode || !email) {
        setErrorMessage("Email and OTP are required.");
        return;
      }

      setLoading(true); // Show loading spinner
      const response = await axios.post("http://localhost:5000/api/verify-otp", {
        email,
        otpCode,
      });

      if (response.data.status === "Success") {
        setOtpVerified(true);
        setSuccessMessage("OTP verified successfully!");
      } else {
        setErrorMessage(response.data.message);
      }
    } catch (error) {
      console.error("Error during OTP verification:", error);
      setErrorMessage("Failed to verify OTP. Please try again.");
    } finally {
      setLoading(false); // Hide loading spinner
    }
  };

  const handleSignUp = async (e) => {
    e.preventDefault();
    if (!otpVerified) {
      setErrorMessage("Please verify the OTP before signing up.");
      return;
    }

    try {
      setLoading(true); // Show loading spinner
      const response = await axios.post("http://localhost:5000/api/signup", {
        userName,
        email,
        number,
        birthDate,
        password,
      });
      if (response.data.status === "Success") {
        setSuccessMessage("Registration successful!");
        
      } else {
        setErrorMessage(response.data.message);
      }
    } catch {
      setErrorMessage("Sign up failed. Try again.");
     
    } finally {
      setLoading(false); // Hide loading spinner
    }
  };

  return (
    <>
      <Navbar />
      <form onSubmit={handleSignUp} className="sign-up-form">
        <h2>Sign Up</h2>
        {errorMessage && <div className="error-message">{errorMessage}</div>}
        {successMessage && <div className="success-message">{successMessage}</div>}
        {loading && <div className="loading-spinner">Loading...</div>} {/* Show spinner if loading */}

        {[{ id: "username", label: "Username", value: userName, setValue: setUserName, validate: validateUserName, type: "text" },
          { id: "email", label: "Email Address", value: email, setValue: setEmail, validate: validateEmail, type: "email" },
          { id: "number", label: "Phone Number", value: number, setValue: setNumber, validate: validateNumber, type: "text" },
          { id: "birthdate", label: "Birth Date", value: birthDate, setValue: setBirthDate, type: "date" }]
          .map(({ id, label, value, setValue, validate, type }) => (
            <div key={id} className="input-container">
              <input type={type} id={id} value={value} onChange={handleChange(setValue, validate)} required placeholder=" " />
              <label htmlFor={id}>{label}</label>
            </div>
          ))}

        <div className="input-container" style={{ display: "flex", gap: "10px" }}>
          <input type="number" id="otpCode" value={otpCode} onChange={handleChange(setOtpCode)} required placeholder=" " />
          <label htmlFor="otpCode">OTP Code</label>
          <button type="button" className="otp-btn" onClick={handleOtpRequest}>
            {isOtpSent ? "Resend Code" : "Get Code"}
          </button>
          <button type="button" className="verify-btn" onClick={handleOtpVerification}>
            Verify OTP
          </button>
        </div>

        <div className="input-container">
          <input type={showPassword ? "text" : "password"} id="password" value={password} onChange={handleChange(setPassword, validatePassword)} required placeholder=" " />
          <label htmlFor="password">Password</label>
          <i
            className={`fa-regular ${showPassword ? "fa-eye-slash" : "fa-eye"}`}
            onClick={() => setShowPassword((prev) => !prev)}
            style={{ position: "absolute", right: "10px", top: "50%", transform: "translateY(-50%)", cursor: "pointer" }}
          />
        </div>

        <div className="input-container">
          <input type={showPassword ? "text" : "password"} id="confirmPassword" value={confirmPassword} onChange={handleChange(setConfirmPassword, validateConfirmPassword)} required placeholder=" " />
          <label htmlFor="confirmPassword">Confirm Password</label>
        </div>

        <div>
          <input type="submit" value="Sign Up" disabled={!!errorMessage || !otpVerified || loading} />
        </div>
        <div>
          <Link to="/login">Already have an account? Login</Link>
        </div>
      </form>
      <Footer />
    </>
  );
}

export default SignUp;
