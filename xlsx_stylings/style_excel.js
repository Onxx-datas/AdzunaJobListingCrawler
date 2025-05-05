const Excel = require('exceljs');
const path = require('path');
async function styleExcel() {
  try {
    const filePath = path.join(__dirname, 'Results.xlsx');
    console.log(`Trying to read: ${filePath}`);

    const workbook = new Excel.Workbook();
    await workbook.xlsx.readFile(filePath);

    const worksheet = workbook.getWorksheet(1);
    if (!worksheet) {
      console.error("Worksheet not found!");
      return;
    }

    const header = worksheet.getRow(1);
    header.font = { bold: true, color: { argb: 'FFFFFFFF' } };
    header.fill = {
      type: 'pattern',
      pattern: 'solid',
      fgColor: { argb: 'FF4CAF50' },
    };
    header.alignment = { horizontal: 'center', vertical: 'middle' };
    header.height = 20;
    header.commit();

    worksheet.columns = [{ width: 40 }];
    worksheet.autoFilter = { from: 'A1', to: 'A1' };

    const outPath = path.join(__dirname, 'Styled_Results.xlsx');
    await workbook.xlsx.writeFile(outPath);

    console.log("Styled Excel file saved as Styled_Results.xlsx");
  } catch (err) {
    console.error("Error during styling:", err);
  }
}

styleExcel();
