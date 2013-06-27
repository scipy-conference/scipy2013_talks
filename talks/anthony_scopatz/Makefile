notebook = scopatz_scipy2013
nbcdir = ~/nbconvert

all:
	cp -r $(nbcdir)/reveal . $<
	rm -rf reveal/.git* $<
	mkdir -p js $<
	cp $(nbcdir)/js/mathjax-onload.js js
	cp classy.css reveal/css/theme/ $<
	python $(nbcdir)/nbconvert.py -f reveal $(notebook).ipynb $<
	sed -i 's:reveal/css/theme/simple.css:reveal/css/theme/classy.css:' $(notebook)_slides.html $<
	sed -i 's:class="fragment" class="text_cell_render:class="fragment text_cell_render:' $(notebook)_slides.html $<
	sed -i 's/.rendered_html ul{list-style:disc;margin:1em 2em;}/.rendered_html ul{list-style:disc;margin:0em 2em;}/' $(notebook)_slides.html $<
	sed -i '/<\!-- Social buttons -->/,/<\!-- End of social buttons -->/d' $(notebook)_slides.html $<
	sed -i 's/background: #3F3F3F;/background: #4A363D;/' reveal/lib/css/zenburn.css $<

clean:
	rm -f *.pdf *.html *.zip

%.ps :%.eps
	convert $< $@

%.png :%.eps
	convert $< $@

zip:
	zip paper.zip *.html *.bib

.PHONY: all clean
