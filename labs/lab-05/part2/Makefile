.PHONY: select_target dirs static shared compile archive so clean program_dynamic program_static program_compile_link_static program_compile_link_dynamic

.DEFAULT_TARGET := select_target

select_target:
	@echo 'Use one of the following make targets:'
	@echo 'program_dynamic - compile program and link dynamically to libblock'
	@echo 'program_static - compile program and link statically to libblock'
	@echo 'static - compile libblock as a static library'
	@echo 'shared - compile libblock as a shared library'
	@echo 'clean - remove build directories'

dirs:
	mkdir -p bin/static
	mkdir -p bin/shared
	
program_dynamic: shared program_compile_link_dynamic
program_static: static program_compile_link_static
	
program_compile_link_static:
	gcc program.c -Lbin/static -lblock -o bin/program-static
	
program_compile_link_dynamic:
	gcc program.c -Lbin/shared -lblock -o bin/program-shared

static: dirs compile archive
shared: dirs compile so
	
compile:
	gcc -c source/block.c -o bin/block.o

archive:
	ar rcs bin/static/libblock.a bin/block.o

so:
	gcc -shared bin/block.o -o bin/shared/libblock.so
	
clean:
	rm -rf bin
