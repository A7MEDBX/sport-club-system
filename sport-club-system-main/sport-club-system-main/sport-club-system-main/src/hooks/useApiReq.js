import axios from "axios";

function ApiReq(api_link, method) {
  return axios({
    headers: {
      "Content-Type": "application/json",
    },
    method: method,
    url: api_link,
  })
    .then((response) => {
      console.log(response.data);
      return response.data;
    })
    .catch((error) => {
      console.error("Error:", error);
      return null;
    });
}
export default ApiReq;
