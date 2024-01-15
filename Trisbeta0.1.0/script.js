let gameOver = false;
let currentPlayer = "X";
var testo = document.getElementById('cell'); // Aumentiamo la dimensione del font di 2px
testo.style.fontSize = '100px';
testo.style.textAlign = "center"; ;

const cells = document.querySelectorAll(".cell");

for (let i = 0; i < cells.length; i++) {
  cells[i].addEventListener("click", clickHandler);
}

function clickHandler(event) {
  if (gameOver) {
    return;
  }

  let cell = event.target;

  if (cell.textContent === "") {
    if (!cell.classList.contains("disabled")) {
      cell.textContent = currentPlayer;
      cell.classList.add("disabled");

      currentPlayer = (currentPlayer === "X") ? "O" : "X";

      setTimeout(()=>{
      checkWinner();
      },100);
    } else {
      alert("Cella già selezionata!");
    }
  } else {
    alert("Cella occupata!");
  }
}

function checkWinner() {
  setTimeout(()=> {
  if (cells[0].textContent === cells[4].textContent && cells[0].textContent === cells[8].textContent && cells[0].textContent !== "") {
    gameOver = true;
    if (cells[0].textContent === "X") {
      alert("X ha vinto!");
    } else {
      alert("O ha vinto!");
    }
    resetGame();
    return;
  }

  if (cells[2].textContent === cells[4].textContent && cells[2].textContent === cells[6].textContent && cells[2].textContent !== "") {
    gameOver = true;
    if (cells[2].textContent === "X") {
      alert("X ha vinto!");
    } else {
      alert("O ha vinto!");
    }
    resetGame();
    return;
  }

  for (let i = 0; i < 3; i++) {
    if (cells[i * 3].textContent === cells[i * 3 + 1].textContent && cells[i * 3].textContent === cells[i * 3 + 2].textContent && cells[i * 3].textContent !== "") {
      gameOver = true;
      if (cells[i * 3].textContent === "X") {
        alert("X ha vinto!");
      } else {
        alert("O ha vinto!");
      }
      resetGame();
      return;
    }

    if (cells[i].textContent === cells[i + 3].textContent && cells[i].textContent === cells[i + 6].textContent && cells[i].textContent !== "") {
      gameOver = true;
      if (cells[i].textContent === "X") {
        alert("X ha vinto!");
      } else {
        alert("O ha vinto!");
      }
      resetGame();
      return;
    }
  }

  if (allCellsFilled()) {
    gameOver = true;
    alert("Pareggio!");
    resetGame();
    return;
   }
  }, 100);
}

function allCellsFilled() {
  for (const cell of cells) {
    if (cell.textContent === "") {
      return false;
    }
  }
  return true;
}


function resetGame() {
  for (let i = 0; i < cells.length; i++) {
    cells[i].textContent = "";
    cells[i].classList.remove("disabled");
  }

  gameOver = false;
  currentPlayer = "X";
}
