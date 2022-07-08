const report = document.getElementById("report");
const solved = document.getElementById("solved");

document.querySelector(".found-list").classList.add("toRemove");
document.querySelector('#report').classList.add("selected");
document.querySelector('#solved').classList.add('unselected');

solved.addEventListener("click", () => {
  document.querySelector(".found-list").classList.remove("toRemove");
  document.querySelector(".report-list").classList.add("toRemove");
  document.querySelector('#report').classList.remove("selected");
  document.querySelector('#solved').classList.remove('unselected');
  document.querySelector('#solved').classList.add('selected');
  document.querySelector('#report').classList.add("unselected");

});

report.addEventListener("click", () => {
    document.querySelector(".report-list").classList.remove("toRemove");
    document.querySelector(".found-list").classList.add("toRemove");
    document.querySelector('#report').classList.remove("unselected");
  document.querySelector('#solved').classList.remove('selected');
  document.querySelector('#solved').classList.add('unselected');
  document.querySelector('#report').classList.add("selected");
  
  });
  
