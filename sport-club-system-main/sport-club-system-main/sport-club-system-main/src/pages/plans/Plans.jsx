import { useState } from "react";
import Footer from "../../components/Footer";
import Navbar from "../../components/Navbar";
import "./plans.css";

function Plans() {
  const [activePlan, setActivePlan] = useState("monthly");

  const packages = [
    {
      title: "Basic",
      description: "Ideal for small clubs or personal use.",
      features: [
        { text: "Member Management: Basic profiles", icon: "✅" },
        { text: "Booking System: Limited to 5 bookings per month", icon: "✅" },
        { text: "Class Schedules: View only", icon: "✅" },
        { text: "Event Management: Organize 1 event per quarter", icon: "✅" },
        { text: "Admin Dashboard: Basic view", icon: "✅" },
      ],
      pricing: { monthly: "$10", quarterly: "$25", yearly: "$90" },
    },
    {
      title: "Standard",
      description: "Perfect for mid-sized clubs with a variety of sports.",
      features: [
        { text: "Member Management: Advanced profiles", icon: "✅" },
        { text: "Booking System: Up to 20 bookings per month", icon: "✅" },
        { text: "Class Schedules: View and manage classes", icon: "✅" },
        {
          text: "Event Management: Organize up to 3 events per quarter",
          icon: "✅",
        },
        { text: "Admin Dashboard: Full access to club data", icon: "✅" },
        { text: "Notifications: Email/SMS updates for members", icon: "✅" },
      ],
      pricing: { monthly: "$25", quarterly: "$60", yearly: "$220" },
    },
    {
      title: "Premium",
      description:
        "Best for large sports clubs with multiple teams and activities.",
      features: [
        {
          text: "Member Management: Advanced profiles with activity tracking",
          icon: "✅",
        },
        { text: "Booking System: Unlimited bookings", icon: "✅" },
        {
          text: "Class Schedules: Full control, including member sign-ups",
          icon: "✅",
        },
        { text: "Event Management: Organize unlimited events", icon: "✅" },
        { text: "Admin Dashboard: Advanced analytics and reports", icon: "✅" },
        {
          text: "Reports & Analytics: Detailed member, booking, and financial reports",
          icon: "✅",
        },
        {
          text: "Team Management: Manage multiple teams, stats, and performance",
          icon: "✅",
        },
        {
          text: "Discounts & Promotions: Ability to create promotions and discount codes",
          icon: "✅",
        },
        {
          text: "Payment Integration: Full integration for payments",
          icon: "✅",
        },
      ],
      pricing: { monthly: "$50", quarterly: "$130", yearly: "$480" },
    },
  ];
  function seeFeatures(event) {
    if (event.target.previousElementSibling.style.height !== "fit-content") {
      event.target.previousElementSibling.style.height = "fit-content";
    } else {
      event.target.previousElementSibling.style.height = "200px";
    }
  }

  return (
    <>
      <Navbar />
      <div className="plans-container">
        <h2 className="plans-header">Our Pricing Plans</h2>
        <div className="plan-button-container">
          <button
            onClick={() => setActivePlan("monthly")}
            className={`plan-button ${
              activePlan === "monthly" ? "active" : ""
            }`}
          >
            Monthly
          </button>
          <button
            onClick={() => setActivePlan("quarterly")}
            className={`plan-button ${
              activePlan === "quarterly" ? "active" : ""
            }`}
          >
            Quarterly
          </button>
          <button
            onClick={() => setActivePlan("yearly")}
            className={`plan-button ${activePlan === "yearly" ? "active" : ""}`}
          >
            Yearly
          </button>
        </div>

        <div className="plans">
          {packages.map((pkg) => (
            <div key={pkg.title} className="plan-card">
              <h3 className="plan-title">{pkg.title}</h3>
              <p className="plan-description">{pkg.description}</p>
              <ul className="plan-features">
                {pkg.features.map((feature, index) => (
                  <li key={index} className="plan-feature">
                    <span className="feature-icon">{feature.icon}</span>{" "}
                    {feature.text}
                  </li>
                ))}
              </ul>
              <span
                className="see-features-btn"
                onClick={(event) => {
                  seeFeatures(event);
                }}
              >
                See more
              </span>
              <div className="plan-pricing">
                <p className="price">
                  {activePlan.charAt(0).toUpperCase() + activePlan.slice(1)}:{" "}
                  {pkg.pricing[activePlan]}
                </p>
              </div>
              <button className="subscription-btn">Choose Plan</button>
            </div>
          ))}
        </div>
      </div>
      <Footer />
    </>
  );
}

export default Plans;
