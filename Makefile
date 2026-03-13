PREFIX ?= ${HOME}/.local

install:
	pip install .
	mkdir -p $(PREFIX)/share/applications
	cp assets/calcu.desktop $(PREFIX)/share/applications/
	mkdir -p $(PREFIX)/share/icons/hicolor/256x256/apps
	cp assets/calcu.png $(PREFIX)/share/icons/hicolor/256x256/apps/
	mkdir -p $(PREFIX)/share/man/man1
	cp docs/calcu.1 $(PREFIX)/share/man/man1/
	update-desktop-database $(PREFIX)/share/applications || true

uninstall:
	pip uninstall -y calcu
	rm -f $(PREFIX)/share/applications/calcu.desktop
	rm -f $(PREFIX)/share/icons/hicolor/256x256/apps/calcu.png
	rm -f $(PREFIX)/share/man/man1/calcu.1
	update-desktop-database $(PREFIX)/share/applications || true
