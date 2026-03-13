PREFIX ?= ${HOME}/.local

install:
	pip install .
	mkdir -p $(PREFIX)/share/applications
	cp calcu.desktop $(PREFIX)/share/applications/
	mkdir -p $(PREFIX)/share/icons/hicolor/scalable/apps
	cp calcu.svg $(PREFIX)/share/icons/hicolor/scalable/apps/
	mkdir -p $(PREFIX)/share/man/man1
	cp calcu.1 $(PREFIX)/share/man/man1/
	update-desktop-database $(PREFIX)/share/applications || true

uninstall:
	pip uninstall -y calcu
	rm -f $(PREFIX)/share/applications/calcu.desktop
	rm -f $(PREFIX)/share/icons/hicolor/scalable/apps/calcu.svg
	rm -f $(PREFIX)/share/man/man1/calcu.1
	update-desktop-database $(PREFIX)/share/applications || true
