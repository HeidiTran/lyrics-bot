const ENTER = 13;
const RESPONSE_DELAY = 1500;
let USERNAME = "USER";

$("#message").keydown((e) => {
  if (e.which == ENTER) {
    let message = $("#message").val();
    $("#chatbox").append(
      `
      <div class="d-flex justify-content-end">
      <div class="card mb-3">
        <div class="card-header">
          <i class="fas fa-user-alt mr-2"></i>
          ${USERNAME}
        </div>
        <div class="card-body">
          <p class="card-text">${message}</p>
        </div>
      </div>
      </div>
      `
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
      success: (data) => { respond(data); }
    });
  }
});

function respond(data) {
  console.log(data);
}

$(document).ready(() => {
  greetUser();
});

function greetUser() {
  botMessage("Hello, I am Lyrics Bot! What is your name?");
}

function botMessage(message) {
  setTimeout(() => {
    $("#chatbox").append(
      `
      <div class="d-flex justify-content-start">
        <div class="card mb-3">
          <div class="card-header">
            <i class="fas fa-robot mr-2"></i>
            LYRICS BOT
          </div>
          <div class="card-body">
            <p class="card-text">${message}</p>
          </div>
        </div>
      </div>
      `
    );
  }, RESPONSE_DELAY);
}

function getQuery() {
  botMessage("What would you like to find?");
}