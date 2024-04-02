var modal = document.getElementById("myModal");

var quitBtn = document.getElementById("give-up-button");
var closePopUp = document.getElementById("left-button");
// When the user clicks the button, open the modal
quitBtn.onclick = function() {
    modal.showModal()
}
closePopUp.onclick = function() {
  modal.close()
}

var modal2 = document.getElementById("myModal2");
var submitBtn = document.getElementById("submit-button");
var closePopUp2 = document.getElementById("left-button2");
submitBtn.onclick = function() {
  modal2.showModal()
}
closePopUp2.onclick = function() {
  modal2.close()
}

//checkbox acting like a radio button
function func() {
  var x = document.getElementsByClassName("checkbox-box");
  var i;
  for (i = 0; i < x.length; i++) {
      x[i].checked = false;
  }
  event.target.checked = true;
}