
all:
	CC=clang meson builddir
	ninja -C builddir
	cp builddir/python3 .

.PHONY: all
