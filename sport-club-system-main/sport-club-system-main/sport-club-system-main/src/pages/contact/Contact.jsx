import { useState } from "react";
import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";
import "./contact.css";

function Contact() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    message: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert("Your message has been sent successfully!");
    setForm({ name: "", email: "", message: "" });
  };

  return (
    <>
      <Navbar />
      <div className="contact-container">
        <h1 className="contact-header">Contact Us</h1>
        <p className="contact-description">
          Have questions or feedback? Reach out to us, and we’ll get back to you as soon as possible!
        </p>
        <form className="contact-form" onSubmit={(event)=>{handleSubmit(event)}}>
          <input
            type="text"
            name="name"
            value={form.name}
            placeholder="Your Name"
            onChange={(event)=>{handleChange(event)}}
            required
          />
          <input
            type="email"
            name="email"
            value={form.email}
            placeholder="Your Email"
            onChange={(event)=>{handleChange(event)}}
            required
          />
          <textarea
            name="message"
            value={form.message}
            placeholder="Your Message"
            onChange={(event)=>{handleChange(event)}}
            required
          />
          <button type="submit" className="submit-btn">
            Send Message
          </button>
        </form>
      </div>
      <Footer />
    </>
  );
}

export default Contact;
