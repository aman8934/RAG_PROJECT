const API_URL = 'http://localhost:8000';

async function uploadFiles() {
  const fileInput = document.getElementById("fileInput");
  const statusDiv = document.getElementById("uploadStatus");

  for(let file of fileInput.files){
    const formData = new FormData();
    formData.append("file",file);

    try{
      const response = await fetch(`${API_URL}/documents/upload`,{
        method: "POST",
        body: formData
      });
      print("enter in upload files")
      const data = await response.json();
      print("exited from 1 upload file")
      if (data.status === "success"){
        statusDiv.className = "success"
        statusDiv.textContent = `✓ Uploaded: ${data.filename} (${data.chunks_created} chunks)`
      }
      else{
        statusDiv.className = "error";
                statusDiv.textContent = `✗ Error: ${data.message}`;
      }
      print("exited from 2 upload file")
    }
    catch(error) {
      statusDiv.className = "error";
      statusDiv.textContent = `✗ Upload failed: ${error.message}`;
    }
  }
  fileInput.value = "";
}

async function sendQuery() {
  const queryInput = document.getElementById("queryInput");
  const chatBox = document.getElementById("chatMessages");
  const query = queryInput.value.trim(); 

  if(!query) return;
  const userMsg = document.createElement("div");
  userMsg.className = "message user-message";
  userMsg.textContent = query;
  chatBox.appendChild(userMsg);  
  queryInput.value = "";

  try {
        const response = await fetch(`${API_URL}/chat/query`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({query: query, top_k: 5})
        });
        const data = await response.json();
        
        // Add assistant message
        const assistantMsg = document.createElement("div");
        assistantMsg.className = "message assistant-message";
        assistantMsg.innerHTML = `
            <div>${data.answer}</div>
            <div class="sources">Sources: ${data.sources.join(", ")}</div>
        `;
            chatBox.appendChild(assistantMsg);
        
        // Auto-scroll
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        const errorMsg = document.createElement("div");
        errorMsg.className = "message assistant-message";
        errorMsg.textContent = `Error: ${error.message}`;
        chatBox.appendChild(errorMsg);
    }
}