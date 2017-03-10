/*
 * LICENSE: GPL
 *
 * t_kill.c
 *
 * Send a signal using kill(2) and analyze the return status of the call.
 */
#include <signal.h>
#include "tlpi_hdr.h"

int main(int argc, char *argv[])
{
	int s, sig;

	if (argc != 3 || strcmp(argv[1], "--help") == 0)
		usageErr("%s pid sig-num\n", argv[0]);

	sig = getInt(argv[2], 0, "sig-num");

	s = kill(getLong(argv[1], 0, "pid"), sig);

	if (sig != 0) {
		if (s == -1)
			errExit("kill");

	} else {                    /* Null signal: process existence check */
		if (s == 0) {
			printf("Process exists and we can send it a signal\n");
		} else {
			if (errno == EPERM)
				printf("Process exists, but we don't have "
				       "permission to send it a signal\n");
			else if (errno == ESRCH)
				printf("Process does not exist\n");
			else
				errExit("kill");
		}
	}

	exit(EXIT_SUCCESS);
}
