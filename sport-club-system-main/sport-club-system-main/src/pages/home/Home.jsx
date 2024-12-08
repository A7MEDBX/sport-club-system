// import ApiReq from "../../hooks/useApiReq"
import Navbar from "../../components/Navbar";
import Footer from "../../components/Footer";
import HeroSection from "./HeroSection";
import FeaturesSection from "./FeaturesSection";
import UpcomingEvents from "./UpComingEvents";
import TopPrograms from "./TopPrograms";
import FAQ from "./FAQ";
import "./home.css";
// import { useState } from "react";

function HomePage() {
  // const [hideFlow,setHideFlow] = useState(false);
  // ApiReq("https://fakestoreapi.com/products", "GET").then((apiData) => {
  //   console.log(apiData);
  // });
  // if (hideFlow) {
  //   document.querySelector("#root").style.overflow = "hidden";
  // }
  return (
    <>
      <Navbar />  
      <div className="home-container"> {/* setBodyFlow={setHideFlow} */}
        <HeroSection />
        <FeaturesSection />
        <TopPrograms/>
        <UpcomingEvents/>
        <FAQ/>
      </div>
      <Footer />
    </>
  );
}

export default HomePage;
