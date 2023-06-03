function sortTable(columnIndex, isNumeric = false) {
  var table, rows, switching, i, x, y, shouldSwitch, shouldReverse;
  table = document.getElementById("myTable");
  switching = true;
  shouldReverse = table.getAttribute("data-sort-direction") === "asc";

  while (switching) {
    switching = false;
    rows = table.getElementsByTagName("tr");

    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("td")[columnIndex];
      y = rows[i + 1].getElementsByTagName("td")[columnIndex];

      var xContent = x.innerHTML.toLowerCase().trim();
      var yContent = y.innerHTML.toLowerCase().trim();

      if (isNumeric) {
        xContent = parseFloat(xContent.replace('zł', ''));
        yContent = parseFloat(yContent.replace('zł', ''));
      }

      if (shouldReverse) {
        if (xContent < yContent) {
          shouldSwitch = true;
          break;
        }
      } else {
        if (xContent > yContent) {
          shouldSwitch = true;
          break;
        }
      }
    }

    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }

  if (shouldReverse) {
    table.setAttribute("data-sort-direction", "desc");
  } else {
    table.setAttribute("data-sort-direction", "asc");
  }
}
