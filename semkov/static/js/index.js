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

  // Mobile Menu
  let mobileMenu = document.getElementById("mobile-menu"),
    mobileMenuOpenButton = document.getElementById("open-mobile-menu"),
    mobileMenuCloseButton = document.getElementById("close-mobile-menu")

  mobileMenuOpenButton.onclick = () => {
    mobileMenu.classList.add("active")
    mobileMenuOpenButton.classList.add("hidden")
    mobileMenuCloseButton.classList.remove("hidden")
  }

  mobileMenuCloseButton.onclick = () => {
    mobileMenu.classList.remove("active")
    mobileMenuOpenButton.classList.remove("hidden")
    mobileMenuCloseButton.classList.add("hidden")
  }

  // Contact Form
  let contactModal = document.getElementById("contact-modal"),
    contactOverlay = document.getElementById("contact-overlay"),
    contactForm = document.getElementById("contact-form")

  document.querySelectorAll(".open-contact-modal").forEach((element) => {
    element.onclick = () => {
      contactModal.classList.add("active")
      contactOverlay.classList.add("active")
    }
  })

  contactModal.querySelectorAll(".close").forEach((element) => {
    element.onclick = () => {
      contactModal.classList.remove("active")
      contactOverlay.classList.remove("active")
    }
  })

  document.getElementById("contact-button").onclick = (e) => {
    e.preventDefault()

    grecaptcha.ready(function() {
      grecaptcha.execute(GOOGLE_RECAPTCHA_SITE_KEY, { action: "submit"}).then((token) => {
        let formData = new FormData(contactForm)
        formData.append("token", token)

        fetch(contactForm.attributes.action.value, {
          method: "POST",
          body: formData,
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
      })
    })


  }
})