document.getElementById("generateBtn").addEventListener("click", async () => {
    const text = document.getElementById("inputText").value;
    const numPoints = document.getElementById("numPoints").value;
    const resultDiv = document.getElementById("outputNotes");

    resultDiv.innerHTML = "<b>Generating notes...</b>";

    try {
        const response = await fetch(window.location.origin + "/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text, num_points: numPoints })
        });

        const data = await response.json();

        if (data.notes) {
            resultDiv.innerHTML = "<ul>" + data.notes.map(n => `<li>${n}</li>`).join("") + "</ul>";
        } else {
            resultDiv.innerHTML = "<b style='color:red'>No notes returned. Try again.</b>";
        }
    } catch (error) {
        resultDiv.innerHTML = "<b style='color:red'>Error — backend not reachable.</b>";
        console.error(error);
    }
});


