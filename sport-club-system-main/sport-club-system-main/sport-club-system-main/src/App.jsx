import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/home/Home";
import AdminDashboard from "./pages/AdminDashboard/AdminDashboard";
import Login from "./pages/login/Login";
import SignUp from "./pages/sign-up/Sign-up";
import ResetPassword from "./pages/reset-password/ResetPassword";
import Plans from "./pages/plans/Plans";
import About from "./pages/about/About";
import Contact from "./pages/contact/Contact";
import NotFound from "./pages/NotFound/NotFound";

function App() {
  return (
    <BrowserRouter
      future={{ v7_relativeSplatPath: true, v7_startTransition: true }}
    >
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/admin-dashboard/overview" element={<AdminDashboard />} />
        <Route path="/admin-dashboard/teams" element={<AdminDashboard />} />
        <Route path="/admin-dashboard/members" element={<AdminDashboard />} />
        <Route path="/admin-dashboard/subscriptions" element={<AdminDashboard />} />
        <Route path="/admin-dashboard/events" element={<AdminDashboard />} />
        <Route path="/plans" element={<Plans />} />
        <Route path="/about" element={<About/>} />
        <Route path="/contact" element={<Contact/>} />
        <Route path="/login" element={<Login />} />
        <Route path="/sign-up" element={<SignUp />} />
        <Route path="/reset-password" element={<ResetPassword />} />
        {/* Not Found Page (Erorr 404) */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
