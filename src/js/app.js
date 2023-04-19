
const input = document.querySelector('input');

let dateActuelle = new Date();
let options = { year: 'numeric', month: '2-digit', day: '2-digit' };
let dateFormatee = dateActuelle.toLocaleDateString('fr-FR', options).split('/').reverse().join('-');

// ajouter un écouteur d'événements pour la modification de la valeur de l'entrée de date
input.addEventListener('change', (event) => {
    // mettre à jour la variable "dateFormatee" avec la nouvelle valeur
    dateFormatee = event.target.value;
  
    // appel de la fonction exportDate() et exportTemp() avec la nouvelle dateFormatee
    exportDate()
    exportTemp()
  });



async function exportDate() {
    return fetch(`./data/output/temp-${dateFormatee}.json`)
    .then(res => res.json())
    .then(data => {
        return data.map(element => {
            return element.date
        });
    })
};

async function exportTemp() {
    return fetch(`./data/output/temp-${dateFormatee}.json`)
    .then(res => res.json())
    .then(data => {
        return data.map(element => {
            return element.temp
        });
    })
};

export { exportDate, exportTemp };

// ####################

async function exportAll() {
    const data = await fetch(`./data/output/temp-${dateFormatee}.json`)
      .then(res => res.json());
  
    let dateActuelle = new Date();
    let options = { year: 'numeric', month: '2-digit', day: '2-digit' };
    let today = dateActuelle.toLocaleDateString('fr-FR', options).split('/').reverse().join('-');
    const tempsToday = [];
    for (let i = 0; i < data.length; i++) {
      if (data[i].date.slice(0, 10) === today) {
        tempsToday.push(data[i].temp);
    }
}
  
    const minTempToday = Math.min(...tempsToday);
    const maxTempToday = Math.max(...tempsToday);
    const lastTempToday = tempsToday[tempsToday.length - 1];
    
    const temp = [minTempToday, maxTempToday, lastTempToday];
  
    return temp;
  };

// ####################

async function getMinTemp() {
    const temp = await exportAll();
    return temp[0];
};

async function getMaxTemp() {
    const temp = await exportAll();
    return temp[1];
};
async function getLastTemp() {
    const temp = await exportAll();
    return temp[2];
};

async function AllTemp() {
    const minTemp = await getMinTemp();
    const lastTemp = await getLastTemp();
    const maxTemp = await getMaxTemp();

    const weatherDown = document.querySelector('#weather-down');
    weatherDown.innerHTML = `${minTemp}°C`;

    const weatherTemp = document.querySelector('#weather-temp');
    weatherTemp.innerHTML = `${lastTemp}°C`;

    const weatherUp = document.querySelector('#weather-up');
    weatherUp.innerHTML = `${maxTemp}°C`;
};

AllTemp();

// ####################

