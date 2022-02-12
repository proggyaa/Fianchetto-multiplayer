# Multiplayer-Chess-Api

1. One person can play only one game at a time

### Routes
```
1. challenge?username=<username>&opponent_username=<op_username> [http/https]

Result - unique_game_id
```
```
2. play?player=<player_username>&game_id=<unique_game_id> [ws/wss]



// Every time a new move is made, the [move] data is sent through this websocket
```