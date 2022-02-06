# Multiplayer-Chess-Api

1. One person can play only one game at a time

### Routes
```
1. challenge?opponent_username=<op_username> [http/https]

Request :- 
{
    username : "challenger_username"
}
```
```
2. play?player=<username> [ws/wss]

// Every time a new move is made, the move data is sent through this websocket
```