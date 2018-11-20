#include <stdio.h>
#include <stdlib.h>
#include <syscall.h>
#include <unistd.h>
#include <fcntl.h>


int main( int argc, char *argv[] ) {

    int fd1, fd2;
    char buf[1024];
    long int cpfile;
    int bytes 

    fd1 = open(argv[1], O_RDONLY)
    if(fd1==-1){ //handle error condition
        perror("ERROR: error when opening source file");  
        exit(1);
    }

    printf('%s/n,%d', buf, fd1);
    

    fd2 = open(argv[2], O_CREAT | O_WRONLY);
    if(fd2==-1){ //handle error condition
        perror("ERROR: error when opening target file");
        exit(1);
    }

    
    while((bytes=read(fd1,buf,1024))>0){
        cpfile=write(fd2,buf,1024);
    }
    if(cpfile==-1){ //handle error condition
        printf("ERROR: error when writing to target file");
    }
    close(fd1);
    close(fd2);






}
