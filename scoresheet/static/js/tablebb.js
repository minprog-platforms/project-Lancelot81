function Toep(id) {
    if (id == 0) {
    var tab = document.getElementsById("toep-btns");
    }
    else {
        var tab = document.getElementById(id).parentElement.parentElement;
    }
    var on = tab.querySelectorAll("[style='display: block;']"),
        off = tab.querySelectorAll("[style='display: none']");
    on.setAttribute("style", "display: none");
    off.setAttribute("style", "display: block")
}

function Add_Game() {
    game_form = document.getElementById('game_form');
    player_form = document.getElementById('player_form');
    game_form.setAttribute("style", "display: none;");
    player_form.setAttribute("style", "display: block;");
}

function EndGame() {
    setTimeout('', 5000);
    var scores_table = document.getElementById("bb-scoresheet"),
        form = document.getElementById("guesswins"),
        btn = document.getElementById("endgame"),
        btn2 = document.getElementById("add-round"),
        totals = document.getElementById("scores-table"),
        newgame = document.getElementById("newgame");
    scores_table.setAttribute("style", "display: none;");
    form.setAttribute("style", "display: none;");
    btn.setAttribute("style", "display: none;");
    btn2.setAttribute("style", "display: none;");
    totals.setAttribute("style", "text-align: center;")
    newgame.setAttribute("style", "display: block;")
    var winner = document.getElementById("scores-table").rows[0].getElementsByTagName("th")[0].innerHTML;
    alert("Winner: " + winner)
}

function SetupScoresTable(name) {
    var table = document.getElementById("scores-table"),
        table_row = table.insertRow(-1),
        datapoint = document.createElement("td"),
        scoredata = document.createElement("td"),
        txt = document.createTextNode(name);
    datapoint.appendChild(txt);
    table_row.appendChild(datapoint);
    table_row.appendChild(scoredata);
    table.appendChild(table_row);
}

setInterval(function TotalScores() {
    var total = document.getElementById("scores-table");

    // Sort the table
    sortTable(total);
}, 5000)

// Calculates score based on guess and actual wins
function CalculateScore(gs, wns) {
    if (gs == wns) {
        return 6 + gs * 2
    } else if (gs > wns) {
        return (wns-gs) * 2
    } else {
        return (gs-wns) * 2
    }
}


// Retreive player name and add column, display short notification
function AddPlayer() {
    let player_name = document.getElementById("playername").value;
    appendColumn(player_name);
    SetupScoresTable(player_name);
    addedMessage();
    document.getElementById("playername").value = "";
}


// display short notification
function addedMessage() {
    document.getElementById("notification").style.display = 'block';
    setTimeout(function() { document.getElementById("notification").style.display = 'none'; }, 1500)
}


// append row to the HTML table
function appendRow() {
    var tbl = document.getElementById('bb-scoresheet'); // table reference

    // Process previous round scores
    if (tbl.rows.length >= 2) {
        const cells = tbl.getElementsByClassName(tbl.rows.length - 1);
        for (var i = 0; i < cells.length; i++) {
            const selections = cells[i].getElementsByTagName("select");
            const player_guess = selections[0].value,
                player_wins = selections[1].value;
            cells[i].innerHTML = "";
            var scoretxt = document.createTextNode(CalculateScore(player_guess, player_wins));
            cells[i].appendChild(scoretxt);

            // Make and submit form for data retreival
            // Player id is given by: i + 1
            var player_id = i + 1;
            var form = document.createElement("form");
            var input = document.createElement("input"),
                id_input = document.createElement("input");
            form.setAttribute("action", "/");
            form.setAttribute("method", "post");
            input.setAttribute("name", "score");
            input.setAttribute("value", CalculateScore(player_guess, player_wins));
            id_input.setAttribute("name", "player_id");
            id_input.setAttribute("value", i+1);
            form.appendChild(input);
            form.appendChild(id_input);
            form.submit();
        }
    }

    var row = tbl.insertRow(-1),      // append table row
        i;
    // insert round number
    createCell(row.insertCell(0), 'roundnumber', tbl.rows.length - 1)
    // insert table cells to the new row
    for (i = 1; i < tbl.rows[0].cells.length; i++) {
        createCell(row.insertCell(i), tbl.rows.length - 1);
    }
}
 

// create DIV element and append to the table cell
function createCell(cell, style, text = undefined) {
    var div = document.createElement('div'); // create DIV element
    if (text == undefined) {
        // create guess dropdown
        const sel1 = document.createElement("select", {class: "guess"});
        for (var i = 0; i < 16; i++) {
            var opt = document.createElement("option", {value: i}),
                txt = document.createTextNode(i);
            opt.appendChild(txt);
            sel1.appendChild(opt);
        }
        // create wins dropdown
        const sel2 = document.createElement("select", {class: "wins"});
        for (var i = 0; i < 16; i++) {
            var opt = document.createElement("option", {value: i}),
                txt = document.createTextNode(i);
            opt.appendChild(txt);
            sel2.appendChild(opt);
        }
        const lbl1 = document.createElement("lable"),
            labeltext1 = document.createTextNode("Guess: "),
            lbl2 = document.createElement("label"),
            labeltext2 = document.createTextNode("Wins: ");
        lbl1.appendChild(labeltext1);
        lbl2.appendChild(labeltext2);
        div.appendChild(lbl1);
        div.appendChild(sel1);
        div.appendChild(lbl2);
        div.appendChild(sel2);
    } else {
        var txt = document.createTextNode(text);
        div.appendChild(txt);
    }                   // append text node to the DIV
    div.setAttribute('class', style);        // set DIV class attribute
    div.setAttribute('className', style);    // set DIV class attribute for IE (?!)
    cell.appendChild(div);                   // append DIV to the table cell
}


// append column to the HTML table
function appendColumn(name) {
    var tbl = document.getElementById('bb-scoresheet'), // table reference
        i;
    // open loop for each row and append cell
    for (i = 0; i < tbl.rows.length; i++) {
        createCell(tbl.rows[i].insertCell(tbl.rows[i].cells.length), name, name);
    }
}


// delete table rows with index greater then 0
function deleteRows() {
    var tbl = document.getElementById('bb-scoresheet'); // table reference
    if (tbl.rows.length > 2) {
        var lastRow = tbl.rows.length - 1;            // set the last row index
        // delete last row with index greater then 0
        tbl.deleteRow(lastRow);
        tbl.deleteRow(lastRow - 1);

        var row = tbl.insertRow(-1),      // append table row
            i;
        // insert round number
        createCell(row.insertCell(0), 'roundnumber', tbl.rows.length - 1)
        // insert table cells to the new row
        for (i = 1; i < tbl.rows[0].cells.length; i++) {
            createCell(row.insertCell(i), tbl.rows.length - 1);
        }
    }
}

 
// delete table columns with index greater then 0
function deleteColumns() {
    var tbl = document.getElementById('bb-scoresheet'), // table reference
        lastCol = tbl.rows[0].cells.length - 1,    // set the last column index
        i, j;
    // delete cells with index greater then 0 (for each row)
    for (i = 0; i < tbl.rows.length; i++) {
        for (j = lastCol; j > 0; j--) {
            tbl.rows[i].deleteCell(j);
        }
    }
}

function sortTable(table) {
    var table = document.getElementById('scores-table');
    var rows, switching, i, x, y, shouldSwitch;
    switching = true;
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
      // Start by saying: no switching is done:
      switching = false;
      rows = table.rows;
      /* Loop through all table rows: */
      for (i = 0; i < (rows.length - 1); i++) {
        // Start by saying there should be no switching:
        shouldSwitch = false;
        /* Get the two elements you want to compare,
        one from current row and one from the next: */
        x = rows[i].getElementsByTagName("td")[0];
        y = rows[i + 1].getElementsByTagName("td")[0];
        // Check if the two rows should switch place:
        if (parseInt(x.innerHTML, 10) < parseInt(y.innerHTML, 10)) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
      if (shouldSwitch) {
        /* If a switch has been marked, make the switch
        and mark that a switch has been done: */
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
      }
    }
  }