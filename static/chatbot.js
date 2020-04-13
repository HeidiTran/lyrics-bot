const OUTPUT_MAX = 10;
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

function respond(userResponse) {
  const n = userResponse["results"].length;
  let message;
  const songPlural = (n == 1) ? "song" : "songs";

  if (userResponse["intent"] == "quit") {
    message = `Okay, see you next time, ${USERNAME}!`;
  } else if (n == 0) {
    message = `Sorry ${USERNAME}, I couldn't find anything :(`
  } else if (userResponse["intent"] == "getSongsContainingPhrase") {
    const phrase = userResponse["entity"];
    message = `Hey ${USERNAME}, I found ${n} ${songPlural} with the phrase \"${phrase}\":`;
  } else if (userResponse["intent"] == "getSongsFromArtist") {
    const artist = userResponse["entity"];
    message = `Hey ${USERNAME}, I found ${n} ${songPlural} by ${artist}:`;
  } else if (userResponse["intent"] == "getRandomSongs") {
    message = `Hey ${USERNAME}, I found ${n} ${songPlural} for you to listen to:`;
  } else if (userResponse["intent"] == "noIntentFound") {
    message = `Hey ${USERNAME}, I'm not quite sure what you mean. Could you say that again?`;
  }

  let outputSize = 0;
  let moreToShow = false;
  if (n <= 10) {
    outputSize = n;
  } else {
    outputSize = OUTPUT_MAX;
    moreToShow = true;
  }

  let song;
  for (let i = 0; i < outputSize; i++) {
    song = userResponse["results"][i][0];
    artist = userResponse["results"][i][1];
    message += `<br>- \"${song}\" by ${artist}`;
  }

  botMessage(message);

  if (moreToShow) {
    N = n;
    USER_RESPONSES = userResponse;
    NUM_SONGS_DISPLAYED = 10;
    createButtonMessage();
  } else {
    botMessage("What else can I do for you?");
  }
}

function createButtonMessage() {
  let button = (
    `<button id="yes" type="button" class="btn btn-outline-success mx-2" onclick="userClickedYes()">
      Yes
    </button>
    <button id="no" type="button" class="btn btn-outline-danger" onclick="userClickedNo()">
      No
    </button>`
  );

  botMessage(`Do you want to see more results?${button}`);
}

let N;
let USER_RESPONSES;
let NUM_SONGS_DISPLAYED;

function userClickedYes() {
  let song;
  let artist;
  let message;
  let songsToShow;
  let songPlural;
  
  if (NUM_SONGS_DISPLAYED + 10 < N) {
    songsToShow = NUM_SONGS_DISPLAYED + 10;
    message = "Displaying 10 more songs:";

    for (let i = NUM_SONGS_DISPLAYED; i < songsToShow; i++) {
      song = USER_RESPONSES["results"][i][0];
      artist = USER_RESPONSES["results"][i][1];
      message += `<br>- \"${song}\" by ${artist}`;
    }

    NUM_SONGS_DISPLAYED += 10;
  } else {
    songsToShow = N;
    songPlural = (N - NUM_SONGS_DISPLAYED == 1) ? "song" : "songs";
    message = `Displaying ${N - NUM_SONGS_DISPLAYED} more ${songPlural}:`;

    for (let i = NUM_SONGS_DISPLAYED; i < songsToShow; i++) {
      song = USER_RESPONSES["results"][i][0];
      artist = USER_RESPONSES["results"][i][1];
      message += `<br>- \"${song}\" by ${artist}`;
    }

    NUM_SONGS_DISPLAYED = N;
  }
  botMessage(message);
  if (NUM_SONGS_DISPLAYED != N) {
    createButtonMessage();
  } else {
    botMessage("What else can I do for you?");
  }
}

function userClickedNo() {
  N = 0;
  USER_RESPONSES = null;
  NUM_SONGS_DISPLAYED = 0;
  botMessage("What else can I do for you?");
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