from dexy.filter import DexyFilter
import markdown
import logging

class ImpressFilter(DexyFilter):
    aliases = ['impress']
    _settings = {
            "help" : "Wraps each separate paragraph in a div for impress.js"
            }

    def process_text(self, input_text):
        markdown_logger = logging.getLogger('MARKDOWN')
        markdown_logger.addHandler(self.doc.wrapper.log.handlers[-1])

        # initialize markdown parser
        md = markdown.Markdown(extensions=['nl2br'])

        slides = []
        for div_counter, slide in enumerate(input_text.split("\n\n\n")):
            html = md.convert(slide)
            slides.append("""<div class="slide step" id="slide%s">\n%s\n</div>""" % (div_counter, html))

        return "\n".join(slides)
