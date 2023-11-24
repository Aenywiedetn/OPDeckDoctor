const chartDatas = [
  {
    
    // OP05 - OCG
    labels: ["Red ", "Green ", "Blue ", "Purple ", "Black ", "Yellow"],
    data: [18.1, 8.9, 12.3, 27.0, 10.4, 23.3],
    colors: ["#b3111e", "#238d6c", "#167bb6", "#793c89", "#1a1a1a", "#e6dc62"],
  },
  {
    
    // OP04 - TCG
    labels: ["Red ", "Green ", "Blue ", "Purple ", "Black ", "Yellow"],
    data: [39.0, 18.5, 10.3, 8.9, 3.4, 19.9],
    colors: ["#b3111e", "#238d6c", "#167bb6", "#793c89", "#1a1a1a", "#e6dc62"],
  },
  {
    // OP04 - OCG
    labels: ["Red ", "Green ", "Blue ", "Purple ", "Black ", "Yellow"],
    data: [36.6, 12.9, 13.8, 10.7, 6.9, 19.1],
    colors: ["#b3111e", "#238d6c", "#167bb6", "#793c89", "#1a1a1a", "#e6dc62"],
  },
  {
    // OP03 - TCG
    labels: ["Red ", "Green ", "Blue ", "Purple ", "Black ", "Yellow"],
    data: [51.0, 14.6, 9.8, 2.4, 8.6, 13.6],
    colors: ["#b3111e", "#238d6c", "#167bb6", "#793c89", "#1a1a1a", "#e6dc62"],
  },
  {
    // OP03 - OCG
    labels: ["Red ", "Green ", "Blue ", "Purple ", "Black ", "Yellow"],
    data: [49.3, 10.7, 9.9, 3.7, 12.2, 14.2],
    colors: ["#b3111e", "#238d6c", "#167bb6", "#793c89", "#1a1a1a", "#e6dc62"],
  },
  {
    // OP02 - TCG
    labels: ["Red ", "Green ", "Blue ", "Purple ", "Black "],
    data: [52.0, 27.3, 6.5, 6.5, 7.7],
    colors: ["#b3111e", "#238d6c", "#167bb6", "#793c89", "#1a1a1a"],
  },
  {
    // OP02 - OCG
    labels: ["Red ", "Green ", "Blue ", "Purple ", "Black "],
    data: [33.7, 33.1, 10.8, 12.4, 10],
    colors: ["#b3111e", "#238d6c", "#167bb6", "#793c89", "#1a1a1a"],
  },
  {
    // OP01 - TCG
    labels: ["Red ", "Green ", "Blue ", "Purple "],
    data: [24.9, 28.4, 22.8, 23.9],
    colors: ["#b3111e", "#238d6c", "#167bb6", "#793c89"],
  },
  {
    // OP01 - OCG
    labels: ["Red ", "Green ", "Blue ", "Purple "],
    data: [25.8, 39.6, 8.8, 25.8],
    colors: ["#b3111e", "#238d6c", "#167bb6", "#793c89"],
  },
];

document.querySelectorAll(".my-chart").forEach((chart, index) => {
  const ul = chart.parentElement.nextElementSibling.querySelector("ul");
  const currentData = chartDatas[index];

  new Chart(chart, {
    type: "doughnut",
    data: {
      labels: currentData.labels,
      datasets: [
        {
          label: "  %",
          data: currentData.data,
          backgroundColor: currentData.colors,
        },
      ],
    },
    options: {
      borderWidth: 10,
      borderRadius: 2,
      hoverBorderWidth: 0,
      plugins: {
        legend: {
          display: false,
        },
      },
    },
  });

  const populateUl = () => {
    currentData.labels.forEach((label, i) => {
      let li = document.createElement("li");
      li.innerHTML = `${label}: <span class='percentage'>${currentData.data[i]}%</span>`;
      ul.appendChild(li);
    });
  };

  populateUl();
});