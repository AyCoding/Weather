// Using this code for Chart Generator
// Function File

import { exportDate, exportTemp } from './app.js';

let myChart;

async function buildChart() {
  const ctx = document.getElementById('graph').getContext('2d');
  
  const myDate = await exportDate();
  const myTemp = await exportTemp();

  myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: myDate,
      datasets: [{
        label: 'Température',
        data: myTemp,
        borderWidth: 3,
        pointRadius: 0,
        fill: true,
        backgroundColor: 'rgba(0, 168, 235, 0.5)',
        borderColor: 'rgba(0, 168, 235, 1)',
        tension: 0
      }]
    },
    options: {
      scales: {
        x: {
          display: false
        },
        y: {
          beginAtZero: true
        }
      }
    }
  });
  
  // Call updateChart with initial date
    const initialDate = document.querySelector('input').value;
    await updateChart(initialDate);
}

buildChart()

async function updateChart() {
    const newDate = await exportDate();
    const newTemp = await exportTemp();
    
    myChart.data.labels = newDate;
    myChart.data.datasets[0].data = newTemp;
    myChart.update();
}

const inputDate = document.querySelector('input');

    inputDate.addEventListener('change', async (e) => {
    // const newDate = e.target.value;
    // await updateChart(newDate);
    await updateChart();
});


  



