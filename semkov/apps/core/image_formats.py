from wagtail.images.formats import Format, register_image_format

register_image_format(Format("t1200px", "1200px", "richtext-image post-image", "max-1200x1200"))
