EXECUTABLES=assignment

EXPENSIVE_JUNK += $(EXECUTABLES)

SRC = assignment.c

JUNK +=

CFLAGS += -O3 -Wall -W --std=c11 -lm
OMP_CFLAGS = $(CFLAGS) -fopenmp
MPI_CFLAGS = $(CFLAGS) -lmpi

help:
	@echo "help\tShow this help text"
	@echo "all\tMake all executables"
	@echo "clean\tThrow away all files that are easy to produce again"
	@echo "empty\tThrow away all files that can be produced again"

all: $(EXECUTABLES)

clean:
	rm -rf $(JUNK)

empty:
	rm -rf $(JUNK) $(EXPENSIVE_JUNK)

assignment: assignment
	mpiCC $(OMP_CFLAGS) $(MPI_CFLAGS) -o assignment assignment.c

