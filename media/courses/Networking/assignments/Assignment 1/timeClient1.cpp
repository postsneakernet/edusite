// Elliot Hutchinson
// CNT 4104 Software Projects in Computer Networks - Fall 2014
// Assignment 1: timeClient1.cpp
// Requests the time from two different servers and
// displays the time and their difference

#include <stdio.h>
#include <cstdlib>
#include <unistd.h>
#include <errno.h>
#include <string>
#include <netdb.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <iostream>
#include <cmath>

#define TIME_1 "198.60.73.8"
#define TIME_2 "216.228.192.69"
#define SIZE 64

int connectTime(int, struct sockaddr_in);
char getTime(int, char[]);
int getDiff(char[], char[]);

int main(int argc, const char * argv[]) {
    int sock1, sock2;
    struct sockaddr_in serv1, serv2;
    char buf1[SIZE], buf2[SIZE];
    std::string time1 = TIME_1;
    std::string time2 = TIME_2;

    if (argc == 3) {
		time1 = argv[1];
		time2 = argv[2];
	}
    else {
    	std::cout << "No arguments provided, using default servers" << std::endl;
    	std::cout << "Run timeClient1 <ip_addr_1> <ip_addr_2> to specify servers\n" << std::endl;
    }

    sock1 = socket(AF_INET, SOCK_STREAM, 0);
    if (sock1 < 0) {
        std::cerr << "Error creating socket" << std::endl;
        exit(1);
    }

    sock2 = socket(AF_INET, SOCK_STREAM, 0);
	if (sock2 < 0) {
		std::cerr << "Error creating socket" << std::endl;
		exit(1);
	}

    serv1.sin_addr.s_addr = inet_addr(time1.c_str());
	serv1.sin_family = AF_INET;
	serv1.sin_port = htons(13);

	connectTime(sock1, serv1);
	getTime(sock1, buf1);

	close(sock1);

    serv2.sin_addr.s_addr = inet_addr(time2.c_str());
    serv2.sin_family = AF_INET;
	serv2.sin_port = htons(13);

    connectTime(sock2, serv2);
    getTime(sock2, buf2);

    close(sock2);

    getDiff(buf1, buf2);
    return 0;
}

int connectTime(int sock, struct sockaddr_in serv) {
	if (connect(sock, (struct sockaddr *) &serv, sizeof(serv)) < 0) {
		std::cerr << "There was an error connecting to the server" << std::endl;
		exit(1);
	}

	std::cout << "Connected to server: " << inet_ntoa(serv.sin_addr) << std::endl;
	return 0;
}

char getTime(int sock, char buf[]) {
	if (recv(sock, buf, SIZE, 0) < 0) {
		std::cerr << "There was an getting time" << std::endl;
		exit(1);
	}

	std::cout << "Got time: " << buf << std::endl;
	return *buf;
}

int getDiff(char buf1[], char buf2[]) {
	int diff = 0;
	int t1 = ((int) buf1[22]) * 10 + buf1[23];
	int t2 = ((int) buf2[22]) * 10 + buf2[23];
	diff = std::abs(t1-t2);

	std::cout << "Got time difference: " << diff << std::endl;
	return diff;
}
