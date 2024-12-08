import "./home.css";
function FeaturesSection() {
  const features = [
    {
      icon: "fa-solid fa-user-check",
      title: "Member Management",
      description:
        "Effortlessly track and manage member details, subscriptions, and attendance.",
    },
    {
      icon: "fa-solid fa-chart-line",
      title: "Analytics & Reports",
      description:
        "Gain insights into club performance with detailed analytics and custom reports.",
    },
    {
      icon: "fa-solid fa-calendar-check",
      title: "Event Scheduling",
      description:
        "Plan and manage events with ease, ensuring your members stay informed and engaged.",
    },
  ];

  return (
    <section className="features-section">
      <h2 className="section-title">Why Choose Us?</h2>
      <div className="features-grid">
        {features.map((feature, index) => (
          <div key={index} className="feature-card">
            <i className={`feature-icon ${feature.icon}`}></i>
            <h3 className="feature-title">{feature.title}</h3>
            <p className="feature-text">{feature.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default FeaturesSection;
