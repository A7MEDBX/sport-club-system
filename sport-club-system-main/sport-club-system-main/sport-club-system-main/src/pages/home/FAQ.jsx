import { useState } from "react";
import "./home.css";

const faqData = [
  {
    question: "What are the membership options available?",
    answer:
      "We offer monthly, quarterly, and yearly memberships tailored to your needs.",
  },
  {
    question: "Do you offer personal training sessions?",
    answer:
      "Yes, we provide customized training programs designed by our certified trainers.",
  },
  {
    question: "How can I participate in club events?",
    answer:
      "Simply check the 'Upcoming Events' section on our website and register for events of your choice.",
  },
  {
    question: "What facilities are available at the club?",
    answer:
      "Our club includes a fully-equipped gym, football fields, swimming pools, and an archery range.",
  },
];

function FAQ() {
  const [activeIndex, setActiveIndex] = useState(null);

  const toggleFAQ = (index) => {
    setActiveIndex(index === activeIndex ? null : index);
  };

  return (
    <section className="faq-section">
      <h2 className="faq-header">Frequently Asked Questions</h2>
      <div className="faq-list">
        {faqData.map((faq, index) => (
          <div
            key={index}
            className={`faq-item ${activeIndex === index ? "active" : ""}`}
            onClick={() => toggleFAQ(index)}
          >
            <h3 className="faq-question">{faq.question}</h3>
            {activeIndex === index && <p className="faq-answer">{faq.answer}</p>}
          </div>
        ))}
      </div>
    </section>
  );
}

// eslint-disable-next-line react-refresh/only-export-components
export default FAQ;
