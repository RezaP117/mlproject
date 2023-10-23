// JavaScript code to update the content based on the result

var resultElement = document.getElementById("result_container");

// Access the value from the data attribute
var result = resultElement.getAttribute("data-result");
// console.log("RESULT", typeof result);

function updateHtml(result) {
  // Check the result value and update the element accordingly
  if (result === "0.0") {
    resultElement.innerText = `Result ${result}. You do not have heart disease`;
  } else if (result === "1.0") {
    resultElement.innerText = `Result: ${result}. You likely have heart disease, consult your physician`;
  }
}

updateHtml(result);
