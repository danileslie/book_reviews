let modal = document.getElementById("reviewModal");

// Get the button that opens the modal
let btns = document.querySelectorAll(".book_ID");
// get information on currently selected book
let current_book = document.getElementById('current');
// Get the <span> element that closes the modal
let close = document.querySelector(".close");

btns.forEach((button) => {
    button.addEventListener('click', openModal);
})

close.addEventListener('click', closeModal);

// When the user clicks the button, open the modal 
function openModal() {
  current_book.value = this.value;
  modal.style.display='block';
}    

function closeModal(){
  modal.style.display = "none";
}
// When the user clicks on button, close the modal
// close.onclick = function() {
//   console.log('close clicked');
//   // modal.style.display = "none";
// }

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}