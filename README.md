# Multiplayer-Chess-Api

1. One person can play only one game at a time

### Routes
```
1. challenge?opponent_username=<op_username> [http/https]

Request :- 
{
    username : "challenger_username"
}

Result - unique_game_id
```
```
2. play?player=<username>&game_id=<unique_game_id> [ws/wss]

Request :- 
{
    challenger : "challenger_username",

}


// Every time a new move is made, the [move, outcome] data is sent through this websocket
```