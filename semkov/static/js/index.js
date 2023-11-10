"use strict"

document.addEventListener("DOMContentLoaded", () => {
  // Floating Header
  let header = document.querySelector("header")
  if (header) {
    let prev_y = window.scrollY, curr_y = window.scrollY

    setInterval(() => {
      curr_y = window.scrollY
      if (prev_y === curr_y) return

      curr_y < 60 ? header.classList.remove("active") : header.classList.add("active")
      prev_y = curr_y
    }, 250)
  }

  // Contact Form
  const showContactModalButton = document.getElementById("open-contact-modal"),
    contactModal = document.getElementById("contact-modal"),
    contactOverlay = document.getElementById("contact-overlay"),
    contactButton = document.getElementById("contact-button"),
    contactForm = document.getElementById("contact-form")

  showContactModalButton.onclick = () => {
    contactModal.classList.add("active")
    contactOverlay.classList.add("active")
  }

  contactModal.querySelectorAll(".close").forEach((element) => {
    element.onclick = () => {
      contactModal.classList.remove("active")
      contactOverlay.classList.remove("active")
    }
  })

  contactButton.onclick = (e) => {
    e.preventDefault()
    fetch(contactForm.attributes.action.value, {
      method: "POST",
      body: new FormData(contactForm),
    }).then(response => {
      if (response.status === 200) {
        response.json().then(data => {
          alert(data.message)
        })
      } else {
        alert("Что-то пошло не так, попробуй позже.")
      }
      contactModal.classList.remove("active")
      contactOverlay.classList.remove("active")
    })
  }
})