import { useState } from "react";
import "./admin-dashboard.css";
import DynamicForm from "../../components/DynamicForm";
import ExportExcelSheet from "../../components/ExportExcelSheet";
function DashboardTeams() {
  const teams = [
    {
      teamId: 1,
      teamName: "Falcon Warriors",
      city: "New York",
      location: "Manhattan",
      members: [
        { id: 1, name: "Ahmed Ali" },
        { id: 2, name: "Mohammed Yasin" },
      ],
    },
    {
      teamId: 2,
      teamName: "Ocean Explorers",
      city: "Los Angeles",
      location: "Santa Monica",
      members: [
        { id: 3, name: "Omar Hameed" },
        { id: 4, name: "Yusuf Malik" },
        { id: 5, name: "Bilal Abbas" },
      ],
    },
    {
      teamId: 3,
      teamName: "Mountain Climbers",
      city: "Denver",
      location: "Rocky Mountains",
      members: [
        { id: 6, name: "Hassan Rafiq" },
        { id: 7, name: "Abdullah Kareem" },
        { id: 8, name: "Ibrahim Khalid" },
        { id: 9, name: "Zaid Hussain" },
      ],
    },
    {
      teamId: 4,
      teamName: "Desert Rangers",
      city: "Phoenix",
      location: "Sonoran Desert",
      members: [
        { id: 10, name: "Salman Tariq" },
        { id: 11, name: "Ali Rehman" },
      ],
    },
    {
      teamId: 5,
      teamName: "Sky Flyers",
      city: "Seattle",
      location: "Downtown",
      members: [
        { id: 12, name: "Hamza Nadeem" },
        { id: 13, name: "Faisal Ahmed" },
        { id: 14, name: "Imran Farooq" },
        { id: 15, name: "Sami Javed" },
        { id: 16, name: "Ahmed Khan" },
      ],
    },
    {
      teamId: 6,
      teamName: "Tech Titans",
      city: "San Francisco",
      location: "Silicon Valley",
      members: [
        { id: 17, name: "Salahuddin Al-Mujahid" },
        { id: 18, name: "Reza Patel" },
        { id: 19, name: "Tariq Ahmed" },
      ],
    },
    {
      teamId: 7,
      teamName: "River Riders",
      city: "Chicago",
      location: "Riverwalk",
      members: [
        { id: 20, name: "Ali Shams" },
        { id: 21, name: "Mohammad Faisal" },
        { id: 22, name: "Khalid Zain" },
      ],
    },
    {
      teamId: 8,
      teamName: "Forest Rangers",
      city: "Portland",
      location: "Forest Park",
      members: [
        { id: 23, name: "Nashit Aziz" },
        { id: 24, name: "Kareem Al-Hassan" },
      ],
    },
    {
      teamId: 9,
      teamName: "Polar Explorers",
      city: "Anchorage",
      location: "Arctic Center",
      members: [
        { id: 25, name: "Irfan Malik" },
        { id: 26, name: "Zain Rizvi" },
        { id: 27, name: "Omar Khan" },
        { id: 28, name: "Bilal Rehman" },
      ],
    },
    {
      teamId: 10,
      teamName: "Sunset Surfers",
      city: "Miami",
      location: "South Beach",
      members: [
        { id: 29, name: "Junaid Iqbal" },
        { id: 30, name: "Tariq Hussain" },
      ],
    },
  ];

  const [searchSelect, setSearchSelect] = useState("id");
  const [addTeam, setAddTeam] = useState(false);
  const HeaderRowObject = [
    { header: "Team Id", key: "teamId", width: 10 },
    { header: "Team Name", key: "teamName", width: 20 },
    { header: "City", key: "city", width: 15 },
    { header: "Location", key: "location", width: 20 },
    { header: "Members", key: "members", width: 200 },
  ];

  function SelectOnChange(event) {
    document.querySelector(".dashboard-teams-search-bar").value = "";
    const SearchElements = document.querySelectorAll(
      ".dashboard-teams-table tbody tr"
    );
    for (let i = 0; i < SearchElements.length; i++) {
      SearchElements[i].style.display = "table-row";
    }
    setSearchSelect(event.target.value);
  }

  function SearchFunc(event) {
    const searchInput = event.target;
    const SearchElements = document.querySelectorAll(
      ".dashboard-teams-table tbody tr .dashboard-search-element"
    );
    const searchValue = searchInput.value;
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

  return (
    <div className="dashboard-teams-wrapper">
      <h2>Teams</h2>
      <div className="dashboard-teams-header">
        <div className="search-div">
          <input
            type="search"
            placeholder={
              searchSelect === "id"
                ? "Search by id"
                : searchSelect === "name"
                ? "Search by name"
                : searchSelect === "city"
                ? "Search by city"
                : "Search"
            }
            className="dashboard-teams-search-bar"
            onChange={(event) => {
              SearchFunc(event);
            }}
          />
          <select
            id="search-select"
            onChange={(event) => {
              SelectOnChange(event);
            }}
          >
            <option value="id">Id</option>
            <option value="name">Name</option>
            <option value="city">City</option>
          </select>
        </div>
        <div className="dashboard-teams-controls">
          <button
            className="dashboard-teams-add-btn"
            onClick={() => {
              setAddTeam(true);
            }}
          >
            Add Team
          </button>
          <ExportExcelSheet
            FileName="Teams"
            RowsObject={teams}
            HeaderRowObject={HeaderRowObject}
          />
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
                <td
                  className={
                    searchSelect === "id" ? "dashboard-search-element" : null
                  }
                >
                  {team.teamId}
                </td>
                <td
                  className={
                    searchSelect === "name" ? "dashboard-search-element" : null
                  }
                >
                  {team.teamName}
                </td>
                <td
                  className={
                    searchSelect === "city" ? "dashboard-search-element" : null
                  }
                >
                  {team.city}
                </td>
                <td>{team.location}</td>
                <td>
                  {`${team.members[0].name}, ${team.members[1].name}`}{" "}
                  <span
                    style={{
                      backgroundColor: "#e8e8e8",
                      padding: "5px",
                      borderRadius: "100%",
                    }}
                  >
                    +{team.members.length}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {addTeam === true ? (
        <DynamicForm setStatus={setAddTeam} api="" formType="addTeam" />
      ) : null}
    </div>
  );
}

export default DashboardTeams;
