const container = document.querySelector("#card-container");
const card = document.querySelector(".card");

async function getData() {
  let response = await fetch("https://jsonplaceholder.typicode.com/todos");
  let data = await response.json();
  data.forEach(element => {
    container.innerHTML += `
    <div class="card">
        <h2>${element.title}</h2>
        <p>Completed: ${element.completed}</p>
    </div>
    `;
  });

  let dataLoadedEvent = new CustomEvent("dataLoaded");
  document.dispatchEvent(dataLoadedEvent);
}

function hidePreloader() {
    let promise = new Promise((resolve, reject) => {
    let dataReady = false;
  
      document.addEventListener("dataLoaded", () => {
        dataReady = true;
      });
  
      setTimeout(() => {
        if (dataReady) {
          resolve();
        }
        else {
          reject("Data loading timeout");
        }
      }, 2000);
    });
  
    promise
      .then(() => {
        document.getElementById("preloader").style.display = "none";
      })
      .catch((error) => {
        console.error(error);
      });
  }
  
hidePreloader();
getData();
  