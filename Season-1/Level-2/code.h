// Welcome to Secure Code Game Season-1/Level-2!

// Follow the instructions below to get started:

// 1. Perform code review. Can you spot the bug? 
// 2. Run tests.c to test the functionality
// 3. Run hack.c and if passing then CONGRATS!
// 4. Compare your solution with solution.c

#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_USERNAME_LEN 39
#define SETTINGS_COUNT 10
#define MAX_USERS 100
#define INVALID_USER_ID -1

// Internal counter of user accounts
int userid_next = 0;

// User account structure
typedef struct {
    bool isAdmin;
    long userid;
    char username[MAX_USERNAME_LEN + 1];
    long setting[SETTINGS_COUNT];
} user_account;

// Store of active user accounts
user_account *accounts[MAX_USERS] = {NULL};

// Creates a new user account and returns its unique identifier
int create_user_account(bool isAdmin, const char *username) {
    if (userid_next >= MAX_USERS) {
        fprintf(stderr, "Error: Maximum number of users exceeded.\n");
        return INVALID_USER_ID;
    }    

    if (strlen(username) > MAX_USERNAME_LEN) {
        fprintf(stderr, "Error: Username too long.\n");
        return INVALID_USER_ID;
    }    

    user_account *ua = malloc(sizeof(user_account));
    if (ua == NULL) {
        fprintf(stderr, "Error: Memory allocation failed.\n");
        return INVALID_USER_ID;
    }

    ua->isAdmin = isAdmin;
    ua->userid = userid_next;
    strcpy(ua->username, username);
    memset(ua->setting, 0, sizeof(ua->setting));

    accounts[userid_next] = ua;
    return userid_next++;  // Increment after storing in array
}

// Updates a user setting
bool update_setting(int user_id, const char *index, const char *value) {
    if (user_id < 0 || user_id >= MAX_USERS || accounts[user_id] == NULL)
        return false;

    char *endptr;
    long i = strtol(index, &endptr, 10);
    if (*endptr || i < 0 || i >= SETTINGS_COUNT)
        return false;

    long v = strtol(value, &endptr, 10);
    if (*endptr)
        return false;

    accounts[user_id]->setting[i] = v;
    return true;
}

// Checks if a user is an admin
bool is_admin(int user_id) {
    if (user_id < 0 || user_id >= MAX_USERS || accounts[user_id] == NULL) {
        fprintf(stderr, "Error: Invalid user ID.\n");
        return false;
    }
    return accounts[user_id]->isAdmin;
}

// Retrieves a username by user ID
const char* username(int user_id) {
    if (user_id < 0 || user_id >= MAX_USERS || accounts[user_id] == NULL) {
        fprintf(stderr, "Error: Invalid user ID.\n");
        return NULL;
    }
    return accounts[user_id]->username;
}