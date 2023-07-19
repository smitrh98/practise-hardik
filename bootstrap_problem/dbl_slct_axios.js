const getData =() =>{
    axios.get('https://countriesnow.space/api/v0.1/countries/population/cities')
    .then((response)=>{
        console.log(response.data.data);
        let con = [];
        for(i=0;i<response.data.data.length;i++){
            con.push(response.data.data[i].country);;
        }
        let set =new Set(con);
        let country = [...set];
        for(i=0;i<country.length;i++){
            const newElement= document.createElement('option');
            newElement.innerHTML= country[i];
            document.getElementById('selectX').appendChild(newElement);
        }
    })
    .catch((e)=>{
        console.log(e);
    })

}
window.addEventListener('load',getData);
const selectX = document.getElementById('selectX');
const getCity =() =>{
    axios.get('https://countriesnow.space/api/v0.1/countries/population/cities')
    .then((response)=>{
        console.log(selectX.value);
        var dataCity = [];
        let getChild = document.getElementById('selectY');  
        getChild.innerHTML = '';  
        for(i=0;i<response.data.data.length;i++){
            if(response.data.data[i].country == selectX.value){
                dataCity.push(response.data.data[i]);
            }
        }
        console.log(dataCity);
        for(i=0;i<dataCity.length;i++){
            const newElement= document.createElement('option');
            newElement.innerHTML= dataCity[i].city;
            document.getElementById('selectY').appendChild(newElement);
        }
    })
    .catch((e)=>{
        console.log(e);
    })

}
selectX.addEventListener('change',getCity);