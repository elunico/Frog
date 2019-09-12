#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifndef ROUNDS
#define ROUNDS 10000000
#endif

static char *s_spots = "0123456789";

int random_choice(int length) {
  return (int)(((double)rand() / (RAND_MAX + 1L)) * length);
}

void show_status(long long round, long long rounds) {
  long double amount = (((long double)round) / rounds) * 80;
  for (int i = 0; i < amount; i++) printf("#");
  for (int i = 0; i < amount; i++) printf("%c", '\x08');
  fflush(stdout);
}

int main(int argc, char const **argv) {
  srand(time(NULL));
  long long steps = 0;
  printf("Running simulation for %ld rounds\n", ROUNDS);
  for (long long i = 0; i < ROUNDS; i++) {
    if (i % (ROUNDS / 200) == 0) show_status(i, ROUNDS);
    char *spots = s_spots;
    int num_spots = 10;
    int next_spot_idx = -1;
    char next_spot = '\0';
    while (next_spot != '9') {
      next_spot_idx = random_choice(num_spots);
      next_spot = *(spots + next_spot_idx);
      num_spots -= (next_spot_idx + 1);
      spots += (next_spot_idx + 1);
      steps += 1;
    }
  }
  printf("\n");
  printf("Average number of steps is %Lf\n", steps / (long double)ROUNDS);
}
