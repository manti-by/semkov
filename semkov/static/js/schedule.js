"use strict"

document.addEventListener("DOMContentLoaded", () => {
  let tabHeaders = document.querySelectorAll(".tab-header")

  tabHeaders.forEach((element) => {
    element.onclick = (event) => {
      document.querySelectorAll(".tab").forEach((element) => {
        element.style.display = "none"
      })
      document.getElementById(element.getAttribute("data-id")).style.display = "block"

      tabHeaders.forEach((element) => {
        element.classList.remove("active")
      })
      event.currentTarget.classList.add("active")
    }
  })
})
