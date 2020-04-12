const ENTER = 13;
const RESPONSE_DELAY = 1500;
let USERNAME = "USER";

$("#message").keydown((e) => {
  if (e.which == ENTER) {
    let message = $("#message").val();
    $("#chatbox").append(
      `<div class="card">
        <div class="card-body>
          <h5 class="card-title">
            <i class="fas fa-user-alt mr-2"></i>
            ${USERNAME}
          </h5>
          <p class="user card-body">${message}</p>
        </div>
      </div>`
    );
    $("#message").val("");
    e.preventDefault();

    if (USERNAME == "USER") {
      USERNAME = message;
      botMessage(`Hi ${USERNAME}, nice to meet you!`);
      setTimeout(() => { getQuery(); }, 1000);
      e.preventDefault();
      return;
    }

    let jsonData = {"username": USERNAME, "message": message};

    $.ajax({
      type: "POST",
      url: "/",
      data: JSON.stringify(jsonData),
      contentType: "application/json",
      dataType: "json",
      success: (data) => { console.log(data) }
    });
  }
});

$(document).ready(() => {
  greetUser();
});

function greetUser() {
  botMessage("Hello, I am Lyrics Bot! What is your name?");
}

function botMessage(message) {
  setTimeout(() => {
    $("#chatbox").append(
      `<div class="card">
        <div class="card-body>
          <h5 class="card-title">
            <i class="fas fa-robot mr-2"></i>
            LYRICS BOT
          </h5>
          <p class="bot card-body">${message}</p>
        </div>
      </div>`
    );
  }, RESPONSE_DELAY);
}

function getQuery() {
  botMessage("What would you like to find?");
}