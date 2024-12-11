/* eslint-disable react/prop-types */
function FlowDiv({ controller }) {
  return (
    <div
      className="flow-div"
      onClick={() => {
        controller(false);
      }}
    ></div>
  );
}

export default FlowDiv;
