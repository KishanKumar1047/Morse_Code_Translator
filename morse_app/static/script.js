async function convert(mode) {
  let text = document.getElementById("inputText").value;

  let res = await fetch("/convert", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({text, mode})
  });

  let data = await res.json();
  document.getElementById("output").innerText = data.output;

  let sugDiv = document.getElementById("suggestions");
  sugDiv.innerHTML = "";
  if (data.suggestions && data.suggestions.length > 0) {
    sugDiv.innerHTML = "<h3>Did you mean?</h3>";
    data.suggestions.forEach(word => {
      let btn = document.createElement("button");
      btn.innerText = word;
      btn.onclick = () => {
        document.getElementById("inputText").value = word;
        convert("eng");
      };
      sugDiv.appendChild(btn);
    });
  }
}

// 🎤 Speech recognition (browser built-in)
function startSpeech() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";
  recognition.start();

  recognition.onresult = function(event) {
    document.getElementById("inputText").value = event.results[0][0].transcript;
  };
}
