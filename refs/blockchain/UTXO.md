# UTXO: unspent transactions outputs

              tx0
    +---------------------+
    | Input 0    Output 0 |------+
    |                     |      |
    | Input 1    Output 1 |      |
    +---------------------+      |
                                 |
                                 |
              tx1                |                  tx3
    +---------------------+      |       +----------------------+                  tx4
    |            Output 0 |      +------>| Input 0              |        +--------------------+
    | Input 0             |              |             Output 0 |        | Input 0            |
    |            Output 1 |------------->| Input 1              |        |           Output 1 |
    +---------------------+              |             Output 1 |------->| Input 1            |
                                  +----->| Input 2              |        +--------------------+
                                  |      +----------------------+
              tx2                 |
    +---------------------+       |
    | Input 0             |       |
    |                     |       |
    | Input 1    Output 0 |-------+
    |                     |
    | Input 2             |
    +---------------------+

# NOTE

1. TX input must have output
2. TX output may not have input
3. TX input may have multiple outputs