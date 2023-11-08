(($) => {

  "use strict";

  $.getCookie = (name, default_value) => {
    let value = document.cookie, start = value.indexOf(" " + name + "="), end

    if (start === -1) start = value.indexOf(name + "=")

    if (start === -1) {
      value = default_value
    } else {
      start = value.indexOf("=", start) + 1
      end = value.indexOf(";", start)

      if (end === -1) end = value.length
      value = decodeURIComponent(value.substring(start, end))
    }

    return value
  }

  $(document).ready(() => {
    $(window).scroll(() => {
      let header = $("header")
      $(window).scrollTop() > 60 ? header.addClass("active") : header.removeClass("active")
    })

    $("#contact-button").on("click", (e) => {
      e.preventDefault()

      let form = $("#contact-form"), data = {"csrfmiddlewaretoken": $.getCookie("csrftoken")}

      $.each(form.find(".form-control"), (i, input) => {
        data[input.name] = input.value
      })

      $.post(form.attr("action"), data, (response) => {
        $('#contact-modal').modal("hide")
          alert(response["message"])
      }).fail(() => {
        alert("Что-то пошло не так, попробуй позже.")
      })
    })
  })

})(jQuery)