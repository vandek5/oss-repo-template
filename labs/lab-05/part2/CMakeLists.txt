project(program)
option(STATIC "link statically to libblock" ON)

if(STATIC)
    add_library(block STATIC source/block.c)
else()
    add_library(block SHARED source/block.c)
endif()

add_executable(program program.c)

target_link_libraries(program block)
