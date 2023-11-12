
function filterResults() {
  console.log("attempting to filter results")
  // Declare variables
  var input = document.getElementById('query');
  var filter = input.value.toUpperCase();
  var ul = document.getElementById('user-list');
  var li = ul.getElementsByTagName('user-item');

  // Loop through all list items, and hide those who don't match the search query
  for (var i = 0; i < li.length; i++) {
    var label = li[i].getElementsByTagName("label")[0];
    var txtValue = label.textContent || label.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}