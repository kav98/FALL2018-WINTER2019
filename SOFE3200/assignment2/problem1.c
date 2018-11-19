#include <stdio.h>

int main( int argc, char *argv[] ) {

    int fd1, fd2;

    fd1 = open(agrv[1],O_CREAT | O_RDONLY);
    if(fd1==-1){ //handle error condition
        printf("ERROR: error when opening file")
    }

    

}
