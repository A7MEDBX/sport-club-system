import { useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";

function ResetPassword() {
  const [email, setEmail] = useState("");
  const [resetCode, setResetCode] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [otpSent, setOtpSent] = useState(false);

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleResetCodeChange = (e) => {
    setResetCode(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleConfirmPasswordChange = (e) => {
    setConfirmPassword(e.target.value);
    if (e.target.value !== password) {
      setErrorMessage("Passwords do not match!");
    } else {
      setErrorMessage("");
    }
  };

  const requestResetCode = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/api/request-otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      const result = await response.json();
      if (result.status === "Success") {
        setOtpSent(true);
        alert(result.message);
      } else {
        setErrorMessage(result.message);
      }
    } catch (error) {
      console.error("Error requesting OTP:", error);
    }
  };

  const resetPassword = async () => {
    if (password !== confirmPassword) {
      setErrorMessage("Passwords do not match!");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/api/reset-password", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, otpCode: resetCode, password }),
      });
      const result = await response.json();
      if (result.status === "Success") {
        alert(result.message);
        
      } else {
        setErrorMessage(result.message);
      }
    } catch (error) {
      console.error("Error resetting password:", error);
    }
  };

  return (
    <>
      <Navbar />
      <form>
        <h2>Reset Password</h2>
        {errorMessage && (
          <div style={{ color: "white", backgroundColor: "red", padding: "10px" }}>
            {errorMessage}
          </div>
        )}
        <div className="email-check">
          <input
            type="email"
            placeholder="Your Email"
            onChange={handleEmailChange}
            required
          />
          <button type="button" onClick={requestResetCode} disabled={!email}>
            Check Email
          </button>
        </div>
        {otpSent && (
          <>
            <input
              type="text"
              placeholder="Enter the OTP code"
              onChange={handleResetCodeChange}
              required
            />
            <div className="password-div">
              <input
                type={showPassword ? "text" : "password"}
                placeholder="New Password"
                onChange={handlePasswordChange}
                required
              />
              <input
                type={showPassword ? "text" : "password"}
                placeholder="Confirm Password"
                onChange={handleConfirmPasswordChange}
                required
              />
              <i
                className="fa-regular fa-eye"
                onClick={() => setShowPassword(!showPassword)}
              ></i>
            </div>
            <button type="button" onClick={resetPassword}>
              Reset Password
            </button>
          </>
        )}
        <Link to="/login">Back to Login</Link>
      </form>
      <Footer />
    </>
  );
}

export default ResetPassword;
