const conver = document.querySelector(".btn")
const rate = document.querySelector("#ntr")
const amount = document.querySelector("#mrt")
const output = document.querySelector("#output")


const intrest = rate.value / 100

conver.addEventListener("click", (intrest) => {
    output.textContent = `${intrest * amount.value}`
})