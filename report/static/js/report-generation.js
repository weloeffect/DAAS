const contBtn = document.getElementById("continue")
const prevBtn = document.querySelectorAll("#previous")
const nextBtn = document.querySelectorAll("#next")
const progress = document.getElementById("progress")
const fsteps = document.querySelectorAll(".step")
const psteps = document.querySelectorAll(".progress-step")
const intro = document.getElementById("intro")
const check = document.getElementById("check")
const main = document.getElementById("main")
const process = document.getElementById("process")
const result = document.getElementById("result")
const confirmBtn = document.getElementById("confirm")
const genBtn = document.getElementById("generate")
const data = document.getElementById("data")

// let formStepsNum = 0;
let formStepsNum = 1;

contBtn.addEventListener("click", function(){
  main.style.visibility = "hidden"
  main.style.display = "none"
  process.style.visibility =" visible"
  intro.classList.remove("step-active")
  data.classList.add("step-active")

})
nextBtn.forEach((btn) => {
    btn.addEventListener("click", () => {
      formStepsNum++;
      updateFormSteps();
      updateProgressbar();
    });
  });
  prevBtn.forEach((btn) => {
    btn.addEventListener("click", () => {
      formStepsNum--;
      updateFormSteps();
      updateProgressbar();
    });
  });
  confirmBtn.addEventListener("click", function(){
    process.style.visibility = "hidden"
    process.style.display = "none"
    result.style.visibility =" visible"
    check.classList.remove("step-active")
    // intro.classList.remove("step-active")
    // data.classList.add("step-active")
  
  })
  // genBtn.addEventListener("click", function(){
  //   result.style.visibility = "hidden"
  //   result.style.display = "none"
  //   // main.style.visibility =" visible"
  //   // check.classList.remove("step-active")
  //   // intro.classList.remove("step-active")
  //   // data.classList.add("step-active")
  
  // })
function updateFormSteps() {
    fsteps.forEach((formStep) => {
      formStep.classList.contains("step-active") &&
        formStep.classList.remove("step-active");
    });
    fsteps[formStepsNum].classList.add("step-active");
  }  

  function updateProgressbar() {
    psteps.forEach((progressStep, idx) => {
      if (idx < formStepsNum  ) {
        progressStep.classList.add("progress-active");
      } else {
        progressStep.classList.remove("progress-active");
      }
    });
  
    const progressActive = document.querySelectorAll(".progress-active");
  
    progress.style.width =
      ((progressActive.length - 1) / (psteps.length - 1)) * 100 + "%";
  }