let modal = document.getElementById("myModal");

// Get the button that opens the modal
let btns = document.querySelectorAll(".book_ID");
let add_reviews = document.querySelectorAll('add_review');
let current_book = document.getElementById('current');

btns.forEach((button) => {
    button.addEventListener('click', openModal)
})

add_reviews.forEach((button) => {
    button.addEventListener('click', preventRefresh)}) 

// current_book.addEventListener('click', review_id);

function preventRefresh(event){
    event.preventDefault();
    console.log('no refresh');
    }

function openModal() {
  current_book.value = this.value;
    console.log(this)
    console.log(current_book);
}    


// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btns.forEach((button) => {
    button.addEventListener('click', () => {
        modal.style.display = "block";
    })})
 

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