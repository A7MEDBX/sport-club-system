import "./home.css";
import football_img from "../../assets/pexels-alan-riches-2132817460-29393050.jpg"
import Gym_img from "../../assets/pexels-victorfreitas-2261481.jpg"
import Archery_img from "../../assets/pexels-kampus-6540714.jpg"

const programs = [
  {
    title: "Football Coaching",
    description: "Master your skills with our professional football trainers.",
    image: football_img,
    buttonLabel: "Join Now",
  },
  {
    title: "Gym Sessions",
    description: "State-of-the-art equipment and expert guidance for all levels.",
    image:Gym_img,
    buttonLabel: "Learn More",
  },
  {
    title: "Archery Training",
    description: "Discover the art of precision with our archery classes.",
    image:Archery_img,
    buttonLabel: "Join Now",
  },
];

function TopPrograms() {
  return (
    <section className="programs-section">
      <h2 className="programs-header">Explore Our Top Programs</h2>
      <div className="programs-grid">
        {programs.map((program, index) => (
          <div key={index} className="program-card">
            <img
              src={program.image}
              alt={program.title}
              className="program-image"
            />
            <h3 className="program-title">{program.title}</h3>
            <p className="program-description">{program.description}</p>
            <button className="program-button">{program.buttonLabel}</button>
          </div>
        ))}
      </div>
    </section>
  );
}

export default TopPrograms;
