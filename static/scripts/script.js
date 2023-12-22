let modal = document.getElementById("reviewModal");

// Get the button that opens the modal
let btns = document.querySelectorAll(".book_ID");
// get information on currently selected book
let current_book = document.getElementById('current');
// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0];

btns.forEach((button) => {
    button.addEventListener('click', openModal)
})

// When the user clicks the button, open the modal 
function openModal() {
  current_book.value = this.value;
  modal.style.display='block';
}    

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}