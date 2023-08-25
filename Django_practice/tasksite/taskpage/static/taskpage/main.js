const getData = () => {
    axios
      .get("https://restcountries.com/v3.1/all")
      .then((response) => {
        console.log(response.data);
        console.log(response.data.length);
        for (i = 0; i < response.data.length; i++) {
          const newElement = document.createElement("option");
          newElement.innerHTML = response.data[i].name.common;
          document.getElementById("selectX").appendChild(newElement);
        }
      })
      .catch((e) => {
        console.log(e + e.message);
      });
  };
  window.addEventListener("load", getData);
  var x = 1;
  const reMove = () => {
    if (x == 1) {
      document.getElementById("op1").remove();
      x--;
    }
  };
  document.getElementById("selectX").addEventListener("click", reMove);
  