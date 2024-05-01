const board = document.querySelector('.tetris-board');
const block = document.createElement('div');
block.classList.add('block');

let interval;

function drawBoard() {
 for (let i = 0; i < 200; i++) {
    const square = document.createElement('div');
    square.classList.add('square');
    board.appendChild(square);
 }
}

function randomTetromino() {
 // Create a random tetromino shape
}

function clearIntervals() {
 clearInterval(interval);
}

document.addEventListener('keydown', (event) => {
 if (event.key === 'ArrowDown') {
    // Move tetromino down
 } else if (event.key === 'ArrowLeft') {
    // Move tetromino left
 } else if (event.key === 'ArrowRight') {
    // Move