import { useState, useEffect } from "react";
import "./home.css";

function UpcomingEvents() {
  const events = [
    {
      title: "Football Competition",
      date: new Date("2024-12-01T15:00:00"),
      location: "Main Football Field",
    },
    {
      title: "Gym Session",
      date: new Date("2024-12-02T18:00:00"),
      location: "Club Gym Center",
    },
    {
      title: "Archery",
      date: new Date("2024-12-03T10:00:00"),
      location: "Archery Range",
    },
  ];

  const [timeLeft, setTimeLeft] = useState(calculateTimeLeft(events[0].date));

  function calculateTimeLeft(eventDate) {
    const now = new Date();
    const difference = eventDate - now;
    if (difference > 0) {
      return {
        days: Math.floor(difference / (1000 * 60 * 60 * 24)),
        hours: Math.floor((difference / (1000 * 60 * 60)) % 24),
        minutes: Math.floor((difference / 1000 / 60) % 60),
        seconds: Math.floor((difference / 1000) % 60),
      };
    } else {
      return null;
    }
  }

  useEffect(() => {
    const timer = setInterval(() => {
      setTimeLeft(calculateTimeLeft(events[0].date));
    }, 1000);

    return () => clearInterval(timer);
  });

  return (
    <div className="upcoming-events">
      <h3 className="events-title">Upcoming Events</h3>

      {timeLeft ? (
        <div className="event-timer" style={{ border: "none" }}>
          <h4>Next Event Starts In:</h4>
          <p>
            {timeLeft.days}d {timeLeft.hours}h {timeLeft.minutes}m{" "}
            {timeLeft.seconds}s
          </p>
        </div>
      ) : (
        <p className="no-events">No events currently available.</p>
      )}

      <div className="events-grid">
        {events.map((event, index) => {
          return (
            <div key={index} className="event-card">
              <h4 className="event-title">{event.title}</h4>
              <p className="event-date">{event.date.toLocaleDateString("en-GB")}</p>
              <p className="event-date">{event.date.toLocaleTimeString()}</p>
              <p className="event-location">{event.location}</p>
              {calculateTimeLeft(event.date) ? (
                <div className="event-timer">
                  <h4>Event Starts In:</h4>
                  <p>
                    {calculateTimeLeft(event.date).days}d{" "}
                    {calculateTimeLeft(event.date).hours}h{" "}
                    {calculateTimeLeft(event.date).minutes}m{" "}
                    {calculateTimeLeft(event.date).seconds}s
                  </p>
                </div>
              ) : (
                <p className="no-events">No events currently available.</p>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default UpcomingEvents;
