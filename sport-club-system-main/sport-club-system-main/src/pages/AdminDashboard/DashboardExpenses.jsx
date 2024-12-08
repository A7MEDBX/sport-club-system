import "./admin-dashboard.css";
function DashboardTeams() {
  const teams = [
    {
      teamId: 1,
      teamName: "Falcon Warriors",
      city: "New York",
      location: "Manhattan",
      members: 15,
    },
    {
      teamId: 2,
      teamName: "Ocean Explorers",
      city: "Los Angeles",
      location: "Santa Monica",
      members: 10,
    },
    {
      teamId: 3,
      teamName: "Mountain Climbers",
      city: "Denver",
      location: "Rocky Mountains",
      members: 8,
    },
    {
      teamId: 4,
      teamName: "Desert Rangers",
      city: "Phoenix",
      location: "Sonoran Desert",
      members: 12,
    },
    {
      teamId: 5,
      teamName: "Sky Flyers",
      city: "Seattle",
      location: "Downtown",
      members: 20,
    },
    {
      teamId: 6,
      teamName: "Tech Titans",
      city: "San Francisco",
      location: "Silicon Valley",
      members: 25,
    },
    {
      teamId: 7,
      teamName: "River Riders",
      city: "Chicago",
      location: "Riverwalk",
      members: 18,
    },
    {
      teamId: 8,
      teamName: "Forest Rangers",
      city: "Portland",
      location: "Forest Park",
      members: 9,
    },
    {
      teamId: 9,
      teamName: "Polar Explorers",
      city: "Anchorage",
      location: "Arctic Center",
      members: 6,
    },
    {
      teamId: 10,
      teamName: "Sunset Surfers",
      city: "Miami",
      location: "South Beach",
      members: 14,
    },
  ];
  console.log(document.getElementById("search-select"));
  
  function SearchFunc(event) {
    const searchInput = event.target;
    const SearchElements = document.querySelectorAll(
      ".dashboard-teams-table tbody tr .dashboard-search-element"
    );
    const searchValue = searchInput.value;
    if (typeof searchValue === "string") {
      for (let i = 0; i < SearchElements.length; i++) {
        if (
          SearchElements[i].textContent
            .toLowerCase()
            .includes(searchValue.toLowerCase())
        ) {
          SearchElements[i].parentElement.style.display = "table-row";
        } else {
          SearchElements[i].parentElement.style.display = "none";
        }
      }
    }
  }

  return (
    <div className="dashboard-teams-wrapper">
      <h2>Teams</h2>
      <div className="dashboard-teams-header">
        <div>
          <input
            type="search"
            placeholder="Search for teams"
            className="dashboard-teams-search-bar"
            onChange={(event) => {
              SearchFunc(event);
            }}
          />
          <select id="search-select">
            <option value="id">Search by id</option>
            <option value="name">Search by name</option>
          </select>
        </div>
        <div className="dashboard-teams-controls">
          <button className="dashboard-teams-add-btn">Add Team</button>
          <button className="dashboard-teams-filter-btn">Filter Teams</button>
        </div>
      </div>
      <div className="dashboard-teams-table-wrapper">
        <table className="dashboard-teams-table">
          <thead>
            <tr>
              <th>Team Id</th>
              <th>Team Name</th>
              <th>City</th>
              <th>Location</th>
              <th>Members</th>
            </tr>
          </thead>
          <tbody>
            {teams.map((team) => (
              <tr key={team.teamId}>
                <td className="dashboard-search-element">{team.teamId}</td>
                <td className="dashboard-search-element">{team.teamName}</td>
                <td>{team.city}</td>
                <td>{team.location}</td>
                <td>{team.members}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default DashboardTeams;
