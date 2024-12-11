/* eslint-disable react/prop-types */
import ExcelJS from "exceljs";

function ExportExcelSheet({ FileName, RowsObject, HeaderRowObject }) {
  // Handle Excel export
  const exportToExcel = async () => {
    const workbook = new ExcelJS.Workbook();
    const worksheet = workbook.addWorksheet(FileName);

    // Add header row
    worksheet.columns = HeaderRowObject;

    // Add rows for each team
    RowsObject.forEach((team) => {
      worksheet.addRow(team);
    });

    // Export the Excel file
    const buffer = await workbook.xlsx.writeBuffer();
    const file = new Blob([buffer], { type: "application/octet-stream" });
    const fileURL = URL.createObjectURL(file);
    const link = document.createElement("a");
    link.href = fileURL;
    link.download = `${FileName}.xlsx`;
    link.click();
  };
  return (
    <button
      className="export-exel-sheet-btn"
      onClick={() => {
        exportToExcel(FileName, RowsObject, HeaderRowObject);
      }}
    >
      Export Sheet
    </button>
  );
}
export default ExportExcelSheet;
