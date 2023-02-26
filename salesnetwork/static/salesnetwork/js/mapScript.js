// getting data from template using json_script django tag and #agency-json
let agencyData = JSON.parse(document.getElementById("agency-json").textContent);
// getting the div element that map is inside it
let map = document.getElementById("map");
// setting map default view
// map = new L.Map('map').setView([33.760882, 53.4375], 5);
// this line just creates an instance of Map
map = new L.Map('map', animate=true);
// the below line is for setting the default map view
map.setView([35.709723, 51.426401], 5);


function moveMap(lat, long, id) {
    map.flyTo([lat, long], 14, {
      animate: true,
      duration: 3.5,
    });
    openPopupByID(id);
}

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// this part is for creating markers:
const coorList = [];

// creating a list of coordinates
for (let i=0; i<agencyData.length; i++) {
    let agencyId = agencyData[i]["id"];
    let latitude = agencyData[i]["latitude"];
    let longitude = agencyData[i]["longitude"];
    coorList.push(
        [
            latitude,
            longitude,
            agencyId,
        ],
    );
}
// trying to open popups dynamically
let markerList = [];
// creating markers using the coorList
for (let dataSet of coorList) {
     let latNumber = parseFloat(dataSet[0]);
     let longNumber = parseFloat(dataSet[1]);
     let marker = L.marker(L.latLng(latNumber, longNumber)).on('click', zoomMarkerLocation);
     marker.addTo(map);
     // listing agency info inside popups
     marker.bindPopup(setMarkerInfo(dataSet[2]));
     //adding each marker to the markerList
     marker["id"] = dataSet[2];
     markerList.push(marker);
}
function zoomMarkerLocation(e) {
    console.log(e);
    map.flyTo([parseFloat(e.latlng.lat), parseFloat(e.latlng.lng)], 14, {
      animate: true,
      duration: 3.5,
    });
}

function openPopupByID (agency_id) {
    for (let item of markerList) {
        if (item["id"] === agency_id) {
            item.openPopup();
        }
    }
}
// this function retrieves agency info and returns it as html code to the bindPopup() function.
function setMarkerInfo(agencyId) {
    let agencyName, agencyPhone, agencyCity, agencyAddress;
    for (let i=0; i<agencyData.length; i++) {
        if (agencyId === agencyData[i]["id"]) {
            agencyName = agencyData[i]["title"];
            agencyPhone = agencyData[i]["mobile"];
            agencyCity = agencyData[i]["city"];
            agencyAddress = agencyData[i]["address"];
        }
    }
    return(
        "<div class='repres-box'>" + "<b>" + agencyName + "</b>" +
            "<span></span>" +
            "<table> <tr> <td>شهر: </td> <td>" + agencyCity + "</td></tr>" +
            "<tr> <td>موبایل:   </td> <td>" + agencyPhone + "</td></tr>" +
            "<tr> <td>آدرس: </td> <td>" + agencyAddress + "</td></tr></table>"
    );
}

// this function is to search and filter the agency list
function searchAgency() {
//    getting agency list:
    let agencyList = document.querySelectorAll("#agencyList li");
//    listening to the search:
    let filter = document.getElementById("searchText");
    let searchText = filter.value.toLowerCase();

//    looping through agencies:
    for (let i of agencyList) {
        let item = i.innerText.toLowerCase();

        if (item.indexOf(searchText) === -1) {
            i.classList.add("visually-hidden")
        } else {
            i.classList.remove("visually-hidden")
        }
    }
}
