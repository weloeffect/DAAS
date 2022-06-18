const startBtn = document.getElementById("start")
const produceBtn = document.getElementById("produce")
const reproduceBtn = document.getElementById("reproduce")
const welcome = document.querySelector("#Report-1")
const generate = document.querySelector("#Report-2")
const result = document.querySelector("#Report-3")


startBtn.addEventListener('click', () =>{

    generate.style.display = "block"   
    welcome.style.display = "none"
    
})
produceBtn.addEventListener('click', () =>{

    result.style.display = "block"
    generate.style.display = "none"
    welcome.style.display = "none"   
})
