#include <stdio.h>
#include <stdlib.h>

int main( int argc, char *argv[] ) {

    int fd1, fd2;

    fd1 = open(agrv[1],O_CREAT | O_RDONLY);
    if(fd1==-1){ //handle error condition
        printf("ERROR: error when opening source file")
    }

    void *buf = (*char) malloc(100);

    int bytes = read(fd1,buf,100);

    printf('bytes copied: %d, buffer: %s', bytes, buf);

    close(fd1);

    fd2 = open(argv[2], O_CREAT | O_WRONLY);
    if(fd2==-1){ //handle error condition
        printf("ERROR: error when opening target file")
    }
    int cpfile;
    while(bytes=read(fd1,buf,100)>0){
        cpfile=write(fd2,buf,100);
    }
    if(cpfile==-1){ //handle error condition
        printf("ERROR: error when writing to target file")
    }

    close(fd2);






}
