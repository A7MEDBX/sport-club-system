import { useState } from "react";
import "./admin-dashboard.css";
import DynamicForm from "../../components/DynamicForm";
import ExportExcelSheet from "../../components/ExportExcelSheet";

function DashboardMembers() {
  const members = [
    {
      id: 1,
      name: "Ahmed Ali",
      email: "ahmed.ali@example.com",
      phoneNumber: "123-456-7890",
      subscriptionStatus: "active",
    },
    {
      id: 2,
      name: "Mohammed Yasin",
      email: "mohammed.yasin@example.com",
      phoneNumber: "234-567-8901",
      subscriptionStatus: "inactive",
    },
    {
      id: 3,
      name: "Omar Hameed",
      email: "omar.hameed@example.com",
      phoneNumber: "345-678-9012",
      subscriptionStatus: "overdue",
    },
    {
      id: 4,
      name: "Yusuf Malik",
      email: "yusuf.malik@example.com",
      phoneNumber: "456-789-0123",
      subscriptionStatus: "active",
    },
    {
      id: 5,
      name: "Bilal Abbas",
      email: "bilal.abbas@example.com",
      phoneNumber: "567-890-1234",
      subscriptionStatus: "overdue",
    },
    {
      id: 6,
      name: "Hassan Rafiq",
      email: "hassan.rafiq@example.com",
      phoneNumber: "678-901-2345",
      subscriptionStatus: "active",
    },
    {
      id: 7,
      name: "Abdullah Kareem",
      email: "abdullah.kareem@example.com",
      phoneNumber: "789-012-3456",
      subscriptionStatus: "inactive",
    },
    {
      id: 8,
      name: "Ibrahim Khalid",
      email: "ibrahim.khalid@example.com",
      phoneNumber: "890-123-4567",
      subscriptionStatus: "active",
    },
    {
      id: 9,
      name: "Zaid Hussain",
      email: "zaid.hussain@example.com",
      phoneNumber: "901-234-5678",
      subscriptionStatus: "overdue",
    },
    {
      id: 10,
      name: "Salman Tariq",
      email: "salman.tariq@example.com",
      phoneNumber: "012-345-6789",
      subscriptionStatus: "active",
    },
    {
      id: 11,
      name: "Ali Rehman",
      email: "ali.rehman@example.com",
      phoneNumber: "123-456-7890",
      subscriptionStatus: "inactive",
    },
    {
      id: 12,
      name: "Hamza Nadeem",
      email: "hamza.nadeem@example.com",
      phoneNumber: "234-567-8901",
      subscriptionStatus: "active",
    },
    {
      id: 13,
      name: "Faisal Ahmed",
      email: "faisal.ahmed@example.com",
      phoneNumber: "345-678-9012",
      subscriptionStatus: "active",
    },
    {
      id: 14,
      name: "Imran Farooq",
      email: "imran.farooq@example.com",
      phoneNumber: "456-789-0123",
      subscriptionStatus: "overdue",
    },
    {
      id: 15,
      name: "Sami Javed",
      email: "sami.javed@example.com",
      phoneNumber: "567-890-1234",
      subscriptionStatus: "inactive",
    },
  ];

  const [searchSelect, setSearchSelect] = useState("id");
  const [addMember, setAddMember] = useState(false);

  const HeaderRowObject = [
    { header: "Member Id", key: "id", width: 10 },
    { header: "Member Name", key: "name", width: 25 },
    { header: "Email", key: "email", width: 30 },
    { header: "Phone Number", key: "phoneNumber", width: 20 },
    { header: "Subscription Status", key: "subscriptionStatus", width: 20 },
  ];

  function SelectOnChange(event) {
    document.querySelector(".dashboard-members-search-bar").value = "";
    const SearchElements = document.querySelectorAll(
      ".dashboard-members-table tbody tr"
    );
    for (let i = 0; i < SearchElements.length; i++) {
      SearchElements[i].style.display = "table-row";
    }
    setSearchSelect(event.target.value);
  }

  function SearchFunc(event) {
    const searchInput = event.target;
    const SearchElements = document.querySelectorAll(
      ".dashboard-members-table tbody tr .dashboard-search-element"
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
    <div className="dashboard-members-wrapper">
      <h2>Members</h2>
      <div className="dashboard-members-header">
        <div className="search-div">
          <input
            type="search"
            placeholder={
              searchSelect === "id"
                ? "Search by id"
                : searchSelect === "name"
                ? "Search by name"
                : searchSelect === "email"
                ? "Search by email"
                : searchSelect === "phone-number"
                ? "Search by phone number"
                : searchSelect === "subscription-status"
                ? "Search by subscription status"
                : "Search"
            }
            className="dashboard-members-search-bar"
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
            <option value="email">Email</option>
            <option value="phone-number">Phone Number</option>
            <option value="subscription-status">Subscription Status</option>
          </select>
        </div>
        <div className="dashboard-members-controls">
          <button
            className="dashboard-members-add-btn"
            onClick={() => {
              setAddMember(true);
            }}
          >
            Add Member
          </button>
          <ExportExcelSheet
            FileName="Members"
            RowsObject={members}
            HeaderRowObject={HeaderRowObject}
          />
        </div>
      </div>
      <div className="dashboard-members-table-wrapper">
        <table className="dashboard-members-table">
          <thead>
            <tr>
              <th>Member Id</th>
              <th>Member Name</th>
              <th>Email</th>
              <th>Phone Number</th>
              <th>Subscription Status</th>
            </tr>
          </thead>
          <tbody>
            {members.map((member) => (
              <tr key={member.id}>
                <td
                  className={
                    searchSelect === "id" ? "dashboard-search-element" : null
                  }
                >
                  {member.id}
                </td>
                <td
                  className={
                    searchSelect === "name" ? "dashboard-search-element" : null
                  }
                >
                  {member.name}
                </td>
                <td
                  className={
                    searchSelect === "email" ? "dashboard-search-element" : null
                  }
                >
                  {member.email}
                </td>
                <td
                  className={
                    searchSelect === "phone-number"
                      ? "dashboard-search-element"
                      : null
                  }
                >
                  {member.phoneNumber}
                </td>
                <td
                  className={
                    searchSelect === "subscription-status"
                      ? "dashboard-search-element"
                      : null
                  }
                >
                  {member.subscriptionStatus}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {addMember === true ? (
        <DynamicForm setStatus={setAddMember} api="" formType="addMember" />
      ) : null}
    </div>
  );
}

export default DashboardMembers;