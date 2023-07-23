#ifndef __MAP_H
#define __MAP_H

#include <stdbool.h>

typedef struct map* map;



//创建一个map
map map_create();

//销毁一个map
void map_destroy(map m);

//获得一个map的size
int map_size();

//根据一个键获取值
bool map_contains(const map m, const char* key);

void map_set(map m, const char* key);

const char* map_first(map m);
const char* map_next(map m, const char *key);

#endif