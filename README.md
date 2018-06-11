# nbastats
A simple python package that can be used to retrive any NBA player's current season statistics.
This is a glorified scraper that I built for ***nba-predict*** and later used in all my other basketball related projects. 

### Step 1: Installation (python 3)
```bash
$ pip install nbanumbers
```

Below is how the tensor is catalogued. 
###### A singular stat can be retrieved with a two dimensional index. For example, if the player tensor was titled PLAYER_STATS, then the player's PER would be found at PLAYER_STATS[1][2].

|  -  |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |  11  |  12  |  13  |  14  |  15  |  16  |  17  |  18  |  19  |  20  |  21  |  22  |  23  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|  **0**  | GS | MP | FG | FGA | FG% | 3P | 3PA | 3P% | 2P | 2PA | 2P% | eFG% | FT | FTA | FT% | ORB | DRB | TRB | AST | STL | BLK | TOV | PF | PTS |
|  **1**  | G | MP | PER | TS% | 3PAr | FTr | ORB% | DRB% | TRB% | AST% | STL% | BLK% | TOV% | USG% |  -  |OWS | DWS | WS | WS/48 |  -  | OBPM | DBPM | BPM | VORP | PF | PTS |