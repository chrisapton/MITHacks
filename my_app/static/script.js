$(document).ready(function() {
    $("#post-button").click(function() {
        const url = "http://localhost:5000/post";
        const postInfo = {
            title: $("#title").val(),
            description: $("#description").val()
        };

        $.ajax({
            url: url,
            type: "POST",
            data: JSON.stringify(postInfo),
            processData: false,
            contentType: "application/json; charset=UTF-8",
            complete: function() {
                console.log("request complete!");
                window.location.reload();
            }
        });

    });
});

let crowder;
let question;

function setup() {
  // Code here runs only once
  var canvas = createCanvas(300, 219);
  crowder = loadImage("https://cdn.glitch.com/fc616293-4b24-40ce-a4d1-55b135064e19%2Finset-change_my_mind_meme-001-300x219.jpg?v=1600559576794");
  question = "ONE PLUS ONE EQUALS 11";
  canvas.parent('sketch-holder');
  // resize image to fit more text
}

function draw() {
  background(crowder);
  rotate(-PI/8);
  text(question,50,170,100);
}
